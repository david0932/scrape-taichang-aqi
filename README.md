## 台中市空氣品質(AQI)的Flask API程式
資料來源: https://taqm.epb.taichung.gov.tw/TQAMNEWAQITABLE.ASPX

##安裝必要的套件
確保你已經安裝了所有必要的 Python 套件：
```
pip install flask requests beautifulsoup4 lxml
```
##執行 Flask 應用
```
python app.py
```
## 使用 API 端點
你現在可以通過瀏覽器、curl 或任何 HTTP 客戶端（如 Postman）來訪問 /scrape 端點，並獲取包含發佈時間和表格資料的 JSON 回應。
```
curl http://localhost:5000/scrape
```
## 範例回應
```
{
    "publish_time": "2024年10月24日 21時",
    "data": [
        {
            "測站名稱": "測站A",
            "對健康影響等級": "良好",
            "AQI指標值": 50,
            "指標污染物": "PM2.5",
            "二氧化硫(SO2)_小時濃度(ppb)": 5,
            "二氧化硫(SO2)_8小時移動平均濃度(ppm)": 4.5,
            "一氧化碳(CO)_小時濃度(ppb)": 0.8,
            "一氧化碳(CO)_8小時移動平均濃度(ppb)": 0.7,
            "臭氧(O3)_小時濃度(ppb)": 30,
            "臭氧(O3)_移動平均濃度(μg/m3)": 28,
            "二氧化氮(NO2)_小時濃度(ppb)": 15,
            "二氧化氮(NO2)_移動平均濃度(μg/m3)": 14,
            "懸浮微粒(PM10)_小時濃度(ppb)": 40,
            "懸浮微粒(PM10)_移動平均濃度(μg/m3)": 38,
            "細懸浮微粒(PM2.5)_小時濃度(ppb)": 25,
            "細懸浮微粒(PM2.5)_移動平均濃度(μg/m3)": 24
        },
        ...
    ]
}
```
