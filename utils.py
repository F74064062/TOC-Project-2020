import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate, MessageTemplateAction, TemplateSendMessage, URITemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_template(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    alt_text = "Confirm template",
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://static.rti.org.tw/assets/thumbnails/2019/11/26/87572fecc77bafbeae1fe79d0c36f4d5.jpg',
        title='Menu',
        text='Please select',
        actions=[
            MessageTemplateAction(
                label='蔡英文',
                text='蔡英文'
            ),
            MessageTemplateAction(
                label='韓國瑜',
                text='韓國瑜'
            ),
            MessageTemplateAction(
                label='宋楚瑜',
                text='宋楚瑜'
            ),

        ]
    )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"



"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
