from writer import Iwriter
import requests

class NetworkWriter(Iwriter):

    def __init__(self):
        self.urls = ["http://127.0.0.1:5000/api/upload"]

    def send_data(self,data):
        response = requests.post(self.urls[0],json=data)
        #בדיקה אם הצליח השליחה