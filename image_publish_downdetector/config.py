import os


class Config(object):
    def __init__(self):
        self.service_name = os.environ.get("SERVICE_NAME", "Service")
        self.server = os.environ.get("SERVER")
        self.pull_time = os.environ.get("PULL_TIME")

        self.nfty_topic = os.environ.get("NFTY_TOPIC")
        self.nfty_server = os.environ.get("NFTY_SERVER", "https://ntfy.sh")
