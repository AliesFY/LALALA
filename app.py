from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
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
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,FollowEvent,StickerMessage, StickerSendMessage
)



app = Flask(__name__)

line_bot_api = LineBotApi('oVkk0/VILASxZlIMGTIZB96O9MZmqNDibC5pDGQWqMxlyX+uYdX4gVOcNNn/NbTKRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61PzfvqHM62Te5nKq8xwWFEGqfLxI8B6nTJKSu8dPK4b/7RSCQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')


f = open('testFlex.json', 'r',encoding='utf-8')
flex_message_json_dict = json.load(f)
#line_bot_api.broadcast(TextSendMessage(text ="スタ爆したらやばいよ♡" ))

@app.route("/callback", methods=['POST'])
def callback():
    # いじらない
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    #line_bot_api.broadcast(TextSendMessage(text="💩"))
    # postbackがあるかないか探してjsonファイルのdataを取り出す
    body_json_data = json.loads(body)
    body_json_data = body_json_data["events"][0].get("postback")
    if body_json_data != None:
        if body_json_data == {'data': 'ホールケーキ'}:
            print("制作中")
        elif body_json_data == {'data': 'シュークリーム'}:
            print("制作中")
        elif body_json_data == {'data': 'ティラミス'}:
            print("制作中")

    # いじらない
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
        print(type(flex_message_json_dict))
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text='alt_text',
                #contentsパラメタに, dict型の値を渡す
                contents=flex_message_json_dict
            )
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="レシピと送信してね"))
    #line_bot_api.broadcast(TextSendMessage(text=event.message.text))


#スタンプ送信用
"""
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):

    # https://developers.line.biz/media/messaging-api/sticker_list.pdf
    sticker_ids = [
        '52002734','52002735','52002736','52002737','52002738','52002739','52002740','52002741','52002742','52002743',
    ]
    random.shuffle(sticker_ids)

    sticker_message = StickerSendMessage(
        package_id='11537',
        sticker_id=sticker_ids[0]
    )


    line_bot_api.broadcast(sticker_message)
"""


#友達追加時メッセージ的な
@handler.add(FollowEvent)# FollowEventをimportするのを忘れずに！
def follow_message(event):# event: LineMessagingAPIで定義されるリクエストボディ
    # print(event)

    if event.type == "follow":# フォロー時のみメッセージを送信
        line_bot_api.reply_message(
            event.reply_token,# イベントの応答に用いるトークン
            TextSendMessage(text="フォローありがとうございます！\nレシピ一覧は'うんち'で見れるよ!!"))




if __name__ == "__main__":
    #port = int(os.getenv("PORT"))
    app.run(debug=True)
