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


guranyu1 = ["45", "35", "24"]
guranyu_me = ["70", "60", "45"]
guranyu2 = ["25", "15", "10"]
def holecake():
    testcount.select_count = 0
    file_name = "../holecake.txt"
    back_name = file_name + ".bak"
    shutil.copy(file_name,back_name)

    with open("../holecake.txt",'r', encoding='UTF-8') as h:
        s = h.read()

    s = s.replace("guranyu1", guranyu1[testcount.sweet_count]).replace("guranyu_me", guranyu_me[testcount.sweet_count]).replace("guranyu2", guranyu2[testcount.sweet_count])
    with open("../holecake.txt.bak",'w', encoding='UTF-8') as h:
        h.write(s)
    return s




def thiramisu():
    testcount.select_count = 0
    file_name = "../thiramisu.txt"
    back_name = file_name + ".bak"
    shutil.copy(file_name,back_name)

    with open("../thiramisu.txt",'r', encoding='UTF-8') as h:
        s = h.read()

    s = s.replace("hakurikiko", "1000")
    with open("../thiramisu.txt.bak",'w', encoding='UTF-8') as h:
        h.write(s)
    return s