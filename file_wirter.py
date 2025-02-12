from writer import Iwriter
import json

class FileWriter(Iwriter):

    def send_data(self,data):

        try:
            with open("DB.json",'r') as file:
                exists_data = json.load(file)
        except:
            exists_data = {}

        exists_data.update(data)

        with open("DB.json",'w') as file:
            json.dump(exists_data,file,indent=4)

