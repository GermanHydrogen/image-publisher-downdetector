import requests


class Notifier:
    def __init__(self, topic: str, server: str = "ntfy.sh"):
        self._topic = topic
        self._server = server

    def send_notification(self, message: str):
        requests.post(f"https://{self._server}/{self._topic}", data=message.encode(encoding='utf-8'))
