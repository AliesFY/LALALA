from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import PostbackEvent
import reply,select_likes,recipi,testcount

line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')

def postbacksec(event):
    post_data = event.postback.data
    if testcount.select_count == 0:
        if post_data == "ホールケーキ" or post_data == "シュークリーム" or post_data == "ティラミス":
            if post_data == "ホールケーキ":
                select_ho = select_likes.choice_taste("ホールケーキ")
                select_ho.select1(event)
                testcount.recipi_count = select_ho
            elif post_data == "シュークリーム":
                select_syu = select_likes.choice_taste("シュークリーム")
                select_syu.select1(event)
                testcount.recipi_count = select_syu
            elif post_data== "ティラミス":
                select_thi = select_likes.choice_taste("ティラミス")
                select_thi.select1(event)
                testcount.recipi_count = select_thi
        else:
            reply.reply_message(event, "ざんねんエラーです(´；ω；`)\nもう一度レシピから選択してね！")
    elif testcount.select_count == 1:
        if post_data == "ホールケーキ" or post_data == "シュークリーム" or post_data == "ティラミス":
            testcount.select_count = 0
            reply.reply_message(event, "ざんねんエラーです(´；ω；`)\nもう一度レシピから選択してね！")
        else:
            if post_data == "激アマ":
                testcount.recipi_count.select2(event)
                testcount.sweet_count = 0
            elif post_data == "甘め":
                testcount.recipi_count.select2(event)
                testcount.sweet_count = 1
            elif post_data == "甘さ控えめ":
                testcount.recipi_count.select2(event)
                testcount.sweet_count = 2

            elif post_data == "1":
                testcount.amount_count = 0
                testcount.recipi_count.result(event)
            elif post_data == "2":
                testcount.amount_count = 1
                testcount.recipi_count.result(event)
            elif post_data == "3":
                testcount.amount_count = 2
                testcount.recipi_count.result(event)

            elif post_data == "いいよ！":
                reply.reply_message(event, recipi.holecake())
            elif post_data == "やり直す":
                testcount.select_count = 0
                reply.reply_message(event, "OK(*^-^*)\nもう一度レシピから選択してね！")

    else:
        reply.reply_message(event, "エラー")