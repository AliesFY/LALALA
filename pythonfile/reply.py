from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)



line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')


def reply_message(event, message):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text=message
        )
    )

def reply_stanp(event):
    sticker_messagetest = StickerSendMessage(
        package_id="6325",
        sticker_id="10979922"
    )
    line_bot_api.reply_message(
        event.reply_token,sticker_messagetest
    )

def push_sakura(message):
    userid = "U2bdc11c13e81f999b6ac23e366eec1ce"
    line_bot_api.push_message(
        userid,
        TextSendMessage(
            text=message
        )

    )