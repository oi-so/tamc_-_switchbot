from get_all_data import get_all_data
import gspread
from google.oauth2.service_account import Credentials
import datetime
from pprint import pprint
import os

def main():
    data = get_all_data()
    device_count = len(data)
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")


    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]


    credentials = Credentials.from_service_account_file(
        "./system/tamc-get-tmp-7093a68fc710.json",
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
