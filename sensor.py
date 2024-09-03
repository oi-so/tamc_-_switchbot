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
from get import get_json

def sensor():
    dir_name = "../responses"
    if not exists(dir_name):
        os.makedirs(dir_name)

    token_data = get_json()
    token = token_data["token"]
    secret = token_data["secret"]

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

    response = requests.get("https://api.switch-bot.com/v1.1/devices", headers=apiHeader)
    devices = response.json()

    response_file = f"./data/devices.json"
    with open(response_file, "w") as f:
        json.dump(devices, f)


if __name__ == "__main__":
    sensor()
    print("made a file that is about devices.")
