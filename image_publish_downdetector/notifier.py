import requests


class Notifier:
    def __init__(self, topic: str, server: str):
        self._topic = topic
        self._server = server

    def send_notification(self, message: str):
        requests.post(f"{self._server}/{self._topic}", data=message.encode(encoding='utf-8'))
