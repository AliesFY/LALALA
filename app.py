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
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, MessageAction,URIAction,PostbackEvent,ButtonsTemplate,
    TemplateSendMessage,PostbackAction
)



app = Flask(__name__)

line_bot_api = LineBotApi('oVkk0/VILASxZlIMGTIZB96O9MZmqNDibC5pDGQWqMxlyX+uYdX4gVOcNNn/NbTKRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61PzfvqHM62Te5nKq8xwWFEGqfLxI8B6nTJKSu8dPK4b/7RSCQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')


f = open('testFlex.json', 'r',encoding='utf-8')
flex_message_json_dict = json.load(f)
#line_bot_api.broadcast(TextSendMessage(text ="ああああああああああああああああああ" ))

rich_menu_to_create = RichMenu(
            size = RichMenuSize(width=1598, height=540),
            selected = True,
            name = "Nice richmenu",
            chat_bar_text = "メニュー",
            areas = [
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=0, width=533, height=540),
                    action=MessageAction(text="レシピ")
                ),
                RichMenuArea(
                    bounds=RichMenuBounds(x=533, y=0, width=533, height=540),
                    action=MessageAction(text="クーポン")
                ),
                RichMenuArea(
                    bounds=RichMenuBounds(x=1066, y=0, width=533, height=540),
                    action=MessageAction(text="お問い合わせ")
                )
            ]
        )
    
richmenuid = line_bot_api.create_rich_menu(rich_menu = rich_menu_to_create)

# RichMenu用の画像

path = r"eeyan22.png"

# 画像をRichMenuに指定
with open(path, 'rb') as f:
    line_bot_api.set_rich_menu_image(richmenuid, "image/png", f)

# デフォルトのRichMenuに設定する
line_bot_api.set_default_rich_menu(richmenuid)



@app.route("/callback", methods=['POST'])
def callback():
    # いじらない
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    #line_bot_api.broadcast(TextSendMessage(text="💩"))
    # postbackがあるかないか探してjsonファイルのdataを取り出す
    body_json_data = json.loads(body)
    """
    try:
        body_json_data = body_json_data["events"][0].get("postback")
        if body_json_data != None:
            if body_json_data == {'data': 'ホールケーキ'}:
                print("制作中")
            elif body_json_data == {'data': 'シュークリーム'}:
                print("制作中")
            elif body_json_data == {'data': 'ティラミス'}:
                print("制作中")
    except IndexError:
        print("検証")
    """

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
    """
    sakura = event.source.user_id
    if sakura == "U2bdc11c13e81f999b6ac23e366eec1ce":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="さくらはうんち"))
    """
    if event.message.text == "レシピ":
        print(type(flex_message_json_dict))
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text='ホールケーキ、シュークリーム、ティラミス',
                #contentsパラメタに, dict型の値を渡す
                contents=flex_message_json_dict
            )
        )
    elif event.message.text == "クーポン":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="ないよ！！"
            )
        )
    elif event.message.text == "お問い合わせ":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="こちらのメールアドレスまで！\n ○○○○＠○○"
            )
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="レシピと送信してね"))
    #line_bot_api.broadcast(TextSendMessage(text=event.message.text))

#作る！を押した後
@handler.add(PostbackEvent)
def postback_massage(event):
    post_data = event.postback.data
    if post_data == "ホールケーキ":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="君には無理だ。他のを作ろう"
            )
        )
    elif post_data == "シュークリーム":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="これのほうが無理だよ・・・"
            )
        )
    elif post_data == "ティラミス":
        """
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="全部無理だね　諦めよっか"
            )
        )
        """
        buttons_template = ButtonsTemplate(
                title='味を選んでいくよ!好みを教えてね!', text='まずは甘さから!', actions=[
                    PostbackAction(label='激アマ', data='激アマ'),
                    PostbackAction(label='甘め', data='甘め'),
                    PostbackAction(label='甘さ控えめ', data='甘さ控えめ')
            ])
        template_message = TemplateSendMessage(
                alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    
    if post_data =="激アマ":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="激アマ？引くわぁぁ…"
            )
        )
    elif post_data =="甘め":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="甘め？ケーキ作りなよ"
            )
        )
    elif post_data =="甘さ控えめ":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="甘さ控えめ…？ならスイーツやめたほうがいいんじゃない…？"
            )
        )





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

