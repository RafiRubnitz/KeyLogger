

class Encryptor:

    def __init__(self):
        self.key = "A"

    def xor(self,data):

        def _xor(string):
            return "".join([chr((ord(i) ^ ord(self.key)) + 65) for i in string])

        encrypt_data = {}
        for window_name,value in data.items():
            new_window_name = _xor(window_name)
            encrypt_data[new_window_name] = {}
            for time_line,str_value in value.items():
                new_time_line = _xor(time_line)
                new_str_value = _xor(str_value)
                encrypt_data[new_window_name][new_time_line] = new_str_value

        return encrypt_data
