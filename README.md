# tamc_気象班_switchbot

## Overview
switchbotから気温と湿度を10分ごとに取得し、それをスプレッドシートに出力するプログラムです。

## Requirement
- python 3.12.4
- windows

## Features
### sensor.py
-sensor()関数があり、switchbotにひもづけられているすべてのセンサーのidなどを取得し、devices.json ファイルを作ります。
*センサー名などを変更したら、必ず実行してください。*
### get.py
-get(id)関数があり、idにセンサーのidを入れることで、センサー情報を取得し、data/status_{id}.json ファイルを作ります。
### get_all_data.py
-get_all_data()関数があり、devices.json ファイルと get(id) 関数を利用して、hubを除くすべてのセンサー情報を取得します。取得した辞書型が戻り値に設定されています。
### write_spread_sheet.py
-main()関数があり、指定されたスプレッドシートに、気温や湿度をセンサーidや時刻とともに出力します。
### notify.py
-send_line_notify(message)関数があり、message変数に入れられているメッセージをLINEグループに送信します。
-main()関数があり、LINEグループに「てすとてすと」と送られます。
### every_ten_m.py
-パソコン上で実行するとき、10分ごとに温度湿度を取得し、それをスプレッドシートに記入するという全工程を行ってくれます。
*自動でスリープにならないように実行してください。*
