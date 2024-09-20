from get_all_data import get_all_data
import gspread
from google.oauth2.service_account import Credentials
import datetime
from zoneinfo import ZoneInfo
from pprint import pprint
import os

def main():
    data = get_all_data()
    device_count = len(data)
    date = datetime.datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y/%m/%d")
    time = datetime.datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y/%m/%d %H:%M:%S")


    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # 環境変数からJSONデータを取得
    service_account_info = os.getenv("SERVICE_ACCOUNT_KEY")  # 修正された環境変数名
    # 文字列として取得したJSONを辞書に変換
    service_account_dict = json.loads(service_account_info)
    credentials = Credentials.from_service_account_file(
        service_account_dict
        scopes=scopes
    )


    gc = gspread.authorize(credentials)
    # spreadsheetのurlを設定
    spreadsheet_url = os.environ["SPREAD_SHEET_URL"]
    spreadsheet = gc.open_by_url(spreadsheet_url)
    ws = spreadsheet.worksheet("保存先")
    last_row = len(ws.col_values(2)) + 1

    input_list = []
    for device in data.values():
        input_list.append([device["id"], device["name"], date, time, device["temperature"], device["humidity"] / 100, device["battery"] / 100])


    ws.update(f"A{last_row}:G{last_row + device_count - 1}", input_list)



if __name__ == "__main__":
    main()
