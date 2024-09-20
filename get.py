import os
import time
import json
import hashlib
import hmac
import base64
import uuid
import requests
import json
import datetime
from os.path import exists
from notify import send_line_notify



def get(device_id):
    dir_name = "../responses"

    if not exists(dir_name):
        os.makedirs(dir_name)

    token_data = get_json()
    token = os.environ("TOKEN")
    secret = os.environ("SECRET")

    nonce = str(uuid.uuid4())
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )

    apiHeader = {}
    apiHeader["Authorization"] = token
    apiHeader["Content-Type"] = "application/json"
    apiHeader["charset"] = "utf8"
    apiHeader["t"] = str(t)
    apiHeader["sign"] = str(sign, "utf-8")
    apiHeader["nonce"] = nonce

    try:
        response = requests.get(
            f"https://api.switch-bot.com/v1.1/devices/{device_id}/status",
            headers=apiHeader,
        )
    except Exception as e:
        print("requestでエラーが発生しました。")
        print(f"エラー内容: {e}\n対象の機械id{device_id}")

        notifyMessage = f"requestでエラーが発生しました。\n時刻: {datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n対象の機械id{device_id}\nエラー内容: {e}"
        send_line_notify(notifyMessage)

    
    devices = response.json()

    # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.makedirs("./data", exist_ok=True)
    response_file = f"./data/status_{device_id}.json"
    with open(response_file, "w") as f:
        json.dump(devices, f)


def get_json():
    token_data = {"token": os.environ["TOKEN"], "secret": os.environ["SECRET"]}
    return token_data


if __name__ == "__main__":
    get("id")
    # print("made a file that is stratus.json.")
