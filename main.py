import requests
from bs4 import BeautifulSoup
import time
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

###使用者自行調製###
#data_center名稱
data_center = "Aegis"
#line相關設定
Channel_access_token = "自行修改"
Your_user_ID = "自行修改"
return_message = "FF14 " + data_center + " 可以新增腳色了~"
#間隔多久檢查一次
delay_time = 10

###系統預設不建議修改###
Unavailable_str = "Creation of New Characters Unavailable"
FF14_worldstatus_URL = "https://na.finalfantasyxiv.com/lodestone/worldstatus/"


def work():
    flag = True
    print("start test")
    while True:
        response = requests.get(FF14_worldstatus_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("li", class_="item-list")
        flag_DC_check = True
        for i in result:
            if data_center in str(i):
                flag_DC_check = False
                if not Unavailable_str in str(i):
                    line_bot_api = LineBotApi(Channel_access_token)
                    line_bot_api.push_message(
                        Your_user_ID, TextSendMessage(text=return_message))
                    return
        if flag_DC_check:
            print("找不到data center")
            return
        time.sleep(delay_time)


if __name__ == "__main__":
    work()