from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (ButtonsTemplate, PostbackAction, TemplateSendMessage)

import shutil
import testcount


line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')

sweet_all = ["激アマ", "甘め", "甘さ控えめ"]

ho_guranyu1 = ["45", "35", "24"]
ho_guranyu_me = ["70", "60", "45"]
ho_guranyu2 = ["25", "15", "10"]
def holecake():
    testcount.select_count = 0
    file_name = "../recipi_txt/holecake.txt"
    back_name = file_name + ".bak"
    shutil.copy(file_name,back_name)

    with open("../recipi_txt/holecake.txt",'r', encoding='UTF-8') as h:
        s = h.read()

    s = s.replace("guranyu1", ho_guranyu1[testcount.sweet_count]).replace("guranyu_me", ho_guranyu_me[testcount.sweet_count]).replace("guranyu2", ho_guranyu2[testcount.sweet_count]).replace("sweet", sweet_all[testcount.sweet_count])
    with open("../recipi_txt/holecake.txt.bak",'w', encoding='UTF-8') as h:
        h.write(s)
    return s


cho_guranyu1 = ["140", "120", "100"]
cho_choko = ["(ミルクチョコレート)", " ", "(ブラックチョコレート)"]
def chococake():
    testcount.select_count = 0
    file_name = "../recipi_txt/chococake.txt"
    back_name = file_name + ".bak"
    shutil.copy(file_name,back_name)

    with open("../recipi_txt/chococake.txt",'r', encoding='UTF-8') as h:
        s = h.read()

    s = s.replace("guranyu", cho_guranyu1[testcount.sweet_count]).replace("choco", cho_choko[testcount.sweet_count]).replace("sweet", sweet_all[testcount.sweet_count])
    with open("../recipi_txt/chococake.txt.bak",'w', encoding='UTF-8') as h:
        h.write(s)
    return s



thi_sugar = ["65", "40", "28"]
def thiramisu():
    testcount.select_count = 0
    file_name = "../recipi_txt/thiramisu.txt"
    back_name = file_name + ".bak"
    shutil.copy(file_name,back_name)

    with open("../recipi_txt/thiramisu.txt",'r', encoding='UTF-8') as h:
        s = h.read()

    s = s.replace("sugar", thi_sugar[testcount.sweet_count]).replace("sweet", sweet_all[testcount.sweet_count])
    with open("../recipi_txt/thiramisu.txt.bak",'w', encoding='UTF-8') as h:
        h.write(s)
    return s