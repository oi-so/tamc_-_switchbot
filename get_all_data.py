from get import get
from sensor import sensor
import json
from pprint import pprint


def get_all_data():
    file = open("./data/devices.json")
    devices_json = json.load(file)
    file.close()

    devices_id = {}
    all_data = {}
    for device in devices_json["body"]["deviceList"]:
        id = device["deviceId"]
        name = device["deviceName"]
        if name == "tamc_hub": continue
        devices_id[name] = id

    for device_name, device_id in devices_id.items():
        get(device_id)
        data_file = open(f"./data/status_{device_id}.json")
        data_json = json.load(data_file)

        all_data[device_name] = {
            "id": device_id,
            "name": device_name,
            "temperature": data_json["body"]["temperature"],
            "humidity": data_json["body"]["humidity"],
            "battery": data_json["body"]["battery"]
        }
    
    return all_data


if __name__ == "__main__":
    pprint(get_all_data())