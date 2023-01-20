from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage

import testcount,reply

line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')

def nameregister(event):
    if testcount.name_count == 0:
        reply.reply_message(event,"名前を入力してください")
        testcount.name_count = 1
    elif testcount.name_count == 1:
        global user
        global name
        user = event.source.user_id
        name = event.message.text
        reply.reply_message(event,name + "\nこの名前で登録します\nこれからあなたの発言は、名前込みで当チャンネルフォロワーに発信されます\n使用が終わり次第、解除と送信してください")
        testcount.name_count = 2

def sakurapush(event):
    if testcount.sakura_count == 0:
        global user
        user = event.source.user_id
        reply.reply_message(event,"さくら送信モードに切り替えます")
        testcount.sakura_count = 1
    elif testcount.sakura_count ==1:
        reply.push_sakura(event.message.text)