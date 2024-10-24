# 台中市空氣品質指標(AQI)的Flask API程式
資料來源: https://taqm.epb.taichung.gov.tw/TQAMNEWAQITABLE.ASPX

## 安裝必要的套件
安裝所有必要的 Python 套件：
```
pip install flask requests beautifulsoup4 lxml
```
## 執行 Flask 應用
```
python scraper-app.py
```
## 使用 API 端點
使用瀏覽器、curl 或任何 HTTP 客戶端（如 Postman）來訪問 /scrape 端點，並獲取包含發佈時間和表格資料的 JSON 回應。
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


# Air Quality Index (AQI) Scraper API

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Flask Application](#running-the-flask-application)
  - [API Endpoint](#api-endpoint)
    - [Endpoint URL](#endpoint-url)
    - [Query Parameters](#query-parameters)
    - [Example Request](#example-request)
    - [Example Response](#example-response)
- [Error Handling](#error-handling)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **Air Quality Index (AQI) Scraper API** is a Flask-based web service designed to scrape and provide air quality data from the Taichung Environmental Protection Bureau's AQI table. It extracts both the AQI data table and the publication time, returning the information in a structured JSON format through a simple API endpoint.

## Features

- **Web Scraping**: Extracts AQI data from a specified webpage.
- **Dynamic Header Parsing**: Handles complex table headers with multiple rows, `rowspan`, and `colspan`.
- **Publication Time Extraction**: Retrieves the AQI data publication timestamp.
- **API Access**: Provides a RESTful API endpoint to access the scraped data.
- **Error Handling**: Returns meaningful error messages for failed requests or parsing issues.

## Prerequisites

- Python 3.7 or higher
- `pip` package manager

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/aqi-scraper-api.git
   cd aqi-scraper-api
2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt 

   If you don't have a requirements.txt, you can install the necessary packages directly:
4. **
 
   
5. 
