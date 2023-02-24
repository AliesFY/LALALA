from flask import Flask, request, abort
import os
import json
import random

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,FollowEvent,StickerMessage, StickerSendMessage,
    MessageAction,URIAction,PostbackEvent,
)

#from pythonfile.select_likes import choice_taste
import richmenu, reply, testcount,postbacklist,select_likes,recipi



app = Flask(__name__)

line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')

count = 0


#FlexMessageのjsonの読み込み
f = open(r'../json/testFlex.json', 'r',encoding='utf-8')
"""
g = open(r'../json/coffee.json', 'r',encoding='utf-8')
h = open(r'../json/greentea.json', 'r',encoding='utf-8')
i = open(r'../json/juice.json', 'r',encoding='utf-8')
j = open(r'../json/wain.json', 'r',encoding='utf-8')
"""

flex_message_json_dict = json.load(f)
"""
flex_message_coffee = json.load(g)
flex_message_greentea = json.load(h)
flex_message_juice = json.load(i)
flex_message_wain = json.load(j)
"""
#Richmenuの読み込み
richmenu.init_menu()

# いじらない
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    #line_bot_api.broadcast(TextSendMessage(text="💩"))
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


#レシピ送信用
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "レシピ":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text='ロールケーキ、チョコレートケーキ、ティラミス、ショートケーキ、パウンドケーキ、ガトーショコラ、カステラ',
                    #contentsパラメタに, dict型の値を渡す
                    contents=flex_message_json_dict
                )
            )
    elif event.message.text =="ドリンク":
        testcount.drink_count = 1
        select_likes.drink(event)
    elif event.message.text =="ジュース":
        testcount.drink_count = 0
        reply.flex(event,flex_message_juice)
    elif event.message.text =="コーヒー":
        testcount.drink_count = 0
        reply.flex(event,flex_message_coffee)
    elif event.message.text =="緑茶":
        testcount.drink_count = 0
        reply.flex(event,flex_message_greentea)
    elif event.message.text =="ワイン":
        testcount.drink_count = 0
        reply.flex(event,flex_message_wain)
    
    elif event.message.text == "お問い合わせ":
            reply.reply_message(event, "こちらのメールアドレスまで！\n○○○○@○○")
    else:
            reply.reply_message(event, "レシピと送信してね！\n登録と送信するとみんなになにかいうことができるよ！！")
            #print(event.source.user_id)


#作る！を押した後
@handler.add(PostbackEvent)
def postback_massage(event):
    postbacklist.postbacksec(event)

#スタンプ送信用

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    reply.reply_stanp(event)



#友達追加時メッセージ的な
@handler.add(FollowEvent)
def follow_message(event):
    if event.type == "follow":# フォロー時のみメッセージを送信
        reply.reply_message(event, "フォローありがとうございます！\nレシピ一覧は'レシピ'で見れます!\nよいお菓子ライフを!")


if __name__ == "__main__":
    #port = int(os.getenv("PORT"))
    app.run(debug=True)


#実行コマンド↓
#flask run --debugger --reload
