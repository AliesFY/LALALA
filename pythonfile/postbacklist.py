import json
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
        if post_data == "ロールケーキ" or post_data == "チョコレートケーキ" or post_data == "ティラミス" or post_data == "ショートケーキ" or post_data == "パウンドケーキ" or post_data == "ガトーショコラ" or post_data == "カステラ":
            if post_data == "ロールケーキ":
                select_ho = select_likes.choice_taste("ロールケーキ")
                select_ho.select1(event)
                testcount.recipi_count = select_ho
                testcount.recipi_kind = recipi.holecake
            elif post_data == "チョコレートケーキ":
                select_cho = select_likes.choice_taste("チョコレートケーキ")
                select_cho.select1(event)
                testcount.recipi_count = select_cho
                testcount.recipi_kind = recipi.chococake
            elif post_data== "ティラミス":
                select_thi = select_likes.choice_taste("ティラミス")
                select_thi.select1(event)
                testcount.recipi_count = select_thi
                testcount.recipi_kind = recipi.thiramisu
            elif post_data== "ショートケーキ":
                select_sho = select_likes.choice_taste("ショートケーキ")
                select_sho.select1(event)
                testcount.recipi_count = select_sho
                testcount.recipi_kind = recipi.shortcake
            elif post_data== "パウンドケーキ":
                select_po = select_likes.choice_taste("パウンドケーキ")
                select_po.select1(event)
                testcount.recipi_count = select_po
                testcount.recipi_kind = recipi.poundcake
            elif post_data== "ガトーショコラ":
                select_ga = select_likes.choice_taste("ガトーショコラ")
                select_ga.select1(event)
                testcount.recipi_count = select_ga
                testcount.recipi_kind = recipi.gateauchocolat
            elif post_data== "カステラ":
                select_ca = select_likes.choice_taste("カステラ")
                select_ca.select1(event)
                testcount.recipi_count = select_ca
                testcount.recipi_kind = recipi.castella
        else:
            reply.reply_message(event, "ざんねんエラーです(´；ω；`)\nもう一度レシピから選択してね！")
    elif testcount.select_count == 1:
        if post_data == "ロールケーキ" or post_data == "チョコレートケーキ" or post_data == "ティラミス" or post_data == "ショートケーキ" or post_data == "パウンドケーキ" or post_data == "ガトーショコラ":
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

            elif post_data == "濃いめ":
                testcount.amount_count = 0
                testcount.recipi_count.result(event)
            elif post_data == "普通":
                testcount.amount_count = 1
                testcount.recipi_count.result(event)

            elif post_data == "いいよ！":
                reply.reply_message(event, testcount.recipi_kind())
            elif post_data == "やり直す":
                testcount.select_count = 0
                reply.reply_message(event, "OK(*^-^*)\nもう一度レシピから選択してね！")

    else:
        reply.reply_message(event, "エラー")