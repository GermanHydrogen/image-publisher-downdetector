import requests
from image_publish_downdetector.notifier import Notifier


def test_notifier(mocker):
    mocker.patch("requests.post")
    topic = "abc"
    server = "https://example.com"
    notifier = Notifier(topic, server)
    message = "Hello World!"

    notifier.send_notification(message)

    requests.post.assert_called_once_with("https://example.com/abc", data=message.encode(encoding='utf-8'))