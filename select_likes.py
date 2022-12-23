from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (ButtonsTemplate, PostbackAction, TemplateSendMessage)

import app

line_bot_api = LineBotApi('oVkk0/VILASxZlIMGTIZB96O9MZmqNDibC5pDGQWqMxlyX+uYdX4gVOcNNn/NbTKRPbLHl1jW+mSy2Xy9N+hKtYgLVrPtNFCBECy61PzfvqHM62Te5nKq8xwWFEGqfLxI8B6nTJKSu8dPK4b/7RSCQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33c053fe8f9f91cb370128a7f77f95e5')
class choice_taste:
    def select1(self, event):
        buttons_template = ButtonsTemplate(
                    title='味を選んでいくよ!好みを教えてね!', text='まずは甘さから!', actions=[
                        PostbackAction(label='激アマ', data='激アマ'),
                        PostbackAction(label='甘め', data='甘め'),
                        PostbackAction(label='甘さ控えめ', data='甘さ控えめ')
                ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        return line_bot_api.reply_message(event.reply_token, template_message)