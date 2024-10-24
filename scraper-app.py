from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

def fetch_and_parse_table(url, table_id, num_header_rows=2):
    # 發送GET請求
    response = requests.get(url)
    response.encoding = 'utf-8'  # 根據網站編碼設置

    # 檢查請求是否成功
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    # 使用 BeautifulSoup 解析 HTML 內容
    soup = BeautifulSoup(response.text, 'lxml')

    # 找到目標表格
    table = soup.find('table', {'id': table_id})
    if not table:
        raise Exception(f"No table found with id '{table_id}'")

    # 解析表頭
    header_rows = table.find_all('tr')[:num_header_rows]
    span_map = []
    merged_headers = []

    for row_idx, row in enumerate(header_rows):
        cells = row.find_all(['th', 'td'])
        col_idx = 0  # 當前列索引

        for cell in cells:
            # 跳過被 rowspan 占用的列
            while col_idx < len(span_map) and span_map[col_idx] > 0:
                col_idx += 1

            cell_text = cell.get_text(separator=" ", strip=True)
            colspan = int(cell.get('colspan', 1))
            rowspan = int(cell.get('rowspan', 1))

            for i in range(colspan):
                # 確保 merged_headers 列表足夠長
                if len(merged_headers) <= col_idx:
                    merged_headers.append("")

                # 合併標題
                if row_idx == 0:
                    merged_headers[col_idx] += cell_text
                else:
                    if cell_text:
                        merged_headers[col_idx] += f"_{cell_text}"

                # 處理 rowspan
                if rowspan > 1:
                    if len(span_map) <= col_idx:
                        span_map.append(rowspan - 1)
                    else:
                        span_map[col_idx] = rowspan - 1

                col_idx += 1

        # 減少每個被 rowspan 占用的列的計數
        span_map = [span - 1 if span > 0 else 0 for span in span_map]

    # 清理標題，去除可能的前後下劃線
    merged_headers = [header.strip('_') for header in merged_headers]

    # 解析資料行
    data_rows = table.find_all('tr')[num_header_rows:]
    data = []

    for row in data_rows:
        cells = row.find_all(['td', 'th'])
        if len(cells) < len(merged_headers):
            # 跳過不完整的行
            continue

        row_data = {}
        for header, cell in zip(merged_headers, cells):
            cell_text = cell.get_text(separator=" ", strip=True)
            # 嘗試將數值轉換為數字類型
            try:
                cell_text_clean = cell_text.replace(',', '')  # 移除千分位逗號
                if '.' in cell_text_clean:
                    cell_value = float(cell_text_clean)
                else:
                    cell_value = int(cell_text_clean)
            except ValueError:
                cell_value = cell_text
            row_data[header] = cell_value
        data.append(row_data)

    return data

def fetch_publish_time(soup):
    # 查找具有 id="Label2" 的 <span> 標籤
    span = soup.find('span', {'id': 'Label2'})
    if not span:
        raise Exception("No span found with id 'Label2'")

    publish_text = span.get_text(separator=" ", strip=True)
    # 範例格式："空氣品質指標(AQI)發布時間：2024年10月24日 21時"
    # 我們需要提取 "2024年10月24日 21時"

    try:
        # 分割字符串，提取發布時間
        publish_time = publish_text.split('：')[-1]
    except IndexError:
        raise Exception("Failed to parse publish time from the span text")

    return publish_time

@app.route('/scrape', methods=['GET'])
def scrape():
    # 你可以根據需要通過查詢參數動態設置 URL 或 table_id
    # 例如：/scrape?url=...&table_id=...
    url = request.args.get('url', 'https://taqm.epb.taichung.gov.tw/TQAMNEWAQITABLE.ASPX')
    table_id = request.args.get('table_id', 'GridView1')
    num_header_rows = int(request.args.get('num_header_rows', 2))

    try:
        # 發送GET請求並解析HTML
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            raise Exception(f"Failed to load page {url}")
        soup = BeautifulSoup(response.text, 'lxml')

        # 抓取表格資料
        table = soup.find('table', {'id': table_id})
        if not table:
            raise Exception(f"No table found with id '{table_id}'")

        data = fetch_and_parse_table(url, table_id, num_header_rows)

        # 抓取發佈時間
        publish_time = fetch_publish_time(soup)

        if not data:
            return jsonify({"message": "No data found."}), 404

        # 結合表格資料和發佈時間
        response_data = {
            "publish_time": publish_time,
            "data": data
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
