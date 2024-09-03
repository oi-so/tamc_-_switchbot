# https://qiita.com/akeome/items/e1e0fecf2e754436afc8より
import requests
import os

def main():
    send_line_notify('てすとてすと')

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = os.environ["LINE_TOKEN"]
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'\n{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
