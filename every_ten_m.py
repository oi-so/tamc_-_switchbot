import time
from write_spread_sheet import main
import datetime

i = 0

def job(i):  # 実行させたい関数を定義
    i += 1
    try:
        main()
        print(f"{datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")} completed! (count: {i})")
    except:
        print(f"Error index: {i}, time: {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}")
    return i

while True:
    i = job(i)
    time.sleep(600 - 10.5)