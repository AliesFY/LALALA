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

from select_likes import choice_taste
import richmenu, reply, testcount



app = Flask(__name__)

line_bot_api = LineBotApi('oVkk0/VILASxZlIMGTIZB96O9MZmqNDibC5pDGQWqMxlyX+uYdX4gVOcNNn/NbTKRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61PzfvqHM62Te5nKq8xwWFEGqfLxI8B6nTJKSu8dPK4b/7RSCQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')

count = 0

#FlexMessageのjsonの読み込み
f = open(r'json/testFlex.json', 'r',encoding='utf-8')
flex_message_json_dict = json.load(f)

#Richmenuの読み込み
rich_menu_list = line_bot_api.get_rich_menu_list()
if not rich_menu_list:
    result = richmenu.createRichmeu()
    if not result:
        print("失敗")

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
    """
    sakura = event.source.user_id
    if sakura == "U2bdc11c13e81f999b6ac23e366eec1ce":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="さくらはうんち"))
    """
    match event.message.text:
        case "レシピ":
            print(type(flex_message_json_dict))
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text='ホールケーキ、シュークリーム、ティラミス',
                    #contentsパラメタに, dict型の値を渡す
                    contents=flex_message_json_dict
                )
            )
        case "クーポン":
            reply.reply_message(event, "ないよ！！")
        case "お問い合わせ":
            reply.reply_message(event, "こちらのメールアドレスまで！\n○○○○@○○")
        case _:
            reply.reply_message(event, "レシピと送信してね！")
            #line_bot_api.broadcast(TextSendMessage(text=event.message.text))

#作る！を押した後
@handler.add(PostbackEvent)
def postback_massage(event):
    post_data = event.postback.data
    
    match post_data:
        case "ホールケーキ":
            select_ho = choice_taste("ホールケーキ")
            select_ho.select1(event)
            testcount.count0 = select_ho
        case "シュークリーム":
            select_syu = choice_taste("シュークリーム")
            select_syu.select1(event)
            testcount.count0 = select_syu
        case  "ティラミス":
            select_thi = choice_taste("ティラミス")
            select_thi.select1(event)
            testcount.count0 = select_thi
    
    match post_data:
        case "激アマ":
            testcount.count0.select2(event)
            testcount.count1 = 0
        case "甘め":
            testcount.count0.select2(event)
            testcount.count1 = 1
        case"甘さ控えめ":
            testcount.count0.select2(event)
            testcount.count1 = 2

    match post_data:
        case "1":
            testcount.count2 = 0
            reply.reply_message(event, testcount.count0.result())
        case "2":
            testcount.count2 = 1
            reply.reply_message(event, testcount.count0.result())

        case "3":
            testcount.count2 = 2
            reply.reply_message(event, testcount.count0.result())

    


#スタンプ送信用

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

    sticker_messagetest = StickerSendMessage(
        package_id="6325",
        sticker_id="10979922"
    )

    #line_bot_api.broadcast(sticker_message)
    line_bot_api.reply_message(
            event.reply_token,
            sticker_messagetest)




#友達追加時メッセージ的な
@handler.add(FollowEvent)# FollowEventをimportするのを忘れずに！
def follow_message(event):# event: LineMessagingAPIで定義されるリクエストボディ
    # print(event)

    if event.type == "follow":# フォロー時のみメッセージを送信
        line_bot_api.reply_message(
            event.reply_token,# イベントの応答に用いるトークン
            TextSendMessage(text="フォローありがとうございます！\nレシピ一覧は'レシピ'で見れるよ!!"))



if __name__ == "__main__":
    #port = int(os.getenv("PORT"))
    app.run(debug=True)


#実行コマンド↓
#flask run --debugger --reload
