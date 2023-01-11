from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, MessageAction, PostbackTemplateAction
)

def init_menu(line_bot_api):
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

    path = r"image/eeyan22.png"

    # 画像をRichMenuに指定
    with open(path, 'rb') as f:
        line_bot_api.set_rich_menu_image(richmenuid, "image/png", f)

    # デフォルトのRichMenuに設定する
    line_bot_api.set_default_rich_menu(richmenuid)