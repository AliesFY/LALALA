from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (ButtonsTemplate, PostbackAction, TemplateSendMessage)

import app, testcount, reply

line_bot_api = LineBotApi('g40p1VQDlWGVMHyMd7pL2kZXGj/Qxx0g35zTCf7+NhIN/cUm/8aQLAYzMoTsaY/cRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61Pzfvp4j1gxY/C4LoKe46fzT1shWO08PkQxz3Up0MBnk9910QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')
taste_flevor = ["激アマ", "甘め", "甘さ控えめ"]
people_count = ["1人分", "2人分", "3人分"]

class choice_taste:
    def __init__(self, name):
        self.name = name


    def select1(self, event):
        buttons_template = ButtonsTemplate(
                    title="作るもの：" +self.name +'\n\n味を選んでいくよ!\nあなたの好みを教えてね!', text='まずは甘さから!', actions=[
                        PostbackAction(label='激アマ', data='激アマ'),
                        PostbackAction(label='甘め', data='甘め'),
                        PostbackAction(label='甘さ控えめ', data='甘さ控えめ')
                ])
        template_message = TemplateSendMessage(
            alt_text='甘さを選んでね', template=buttons_template)
        testcount.select_count = 1
        return line_bot_api.reply_message(event.reply_token, template_message)

    def select2(self, event):
        buttons_template = ButtonsTemplate(
                    title='なん人分作るか教えてね!', text='わくわく( *´艸｀)', actions=[
                        PostbackAction(label='1人分', data='1'),
                        PostbackAction(label='2人分', data='2'),
                        PostbackAction(label='3人分', data='3')
                ])
        template_message = TemplateSendMessage(
            alt_text='何人分か選んでね', template=buttons_template)
        return line_bot_api.reply_message(event.reply_token, template_message)

    def result(self):
        testcount.select_count = 0
        return "あなたは" + testcount.recipi_count.name + "の、味は" + taste_flevor[testcount.sweet_count] + "で、" + people_count[testcount.amount_count] + "を選びました"