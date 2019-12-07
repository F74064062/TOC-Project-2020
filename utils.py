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


def send_T(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
    alt_text='蔡英文候選人',
    template=ButtonsTemplate(
        thumbnail_image_url='https://image.peoplenews.tw/news/b14c1624-fc77-4531-8b62-47fdcf4e9236.jpg',
        title='Menu',
        text='Please select',
        actions=[
            URITemplateAction(
                label='她是誰',
                uri='https://zh.wikipedia.org/wiki/%E8%94%A1%E8%8B%B1%E6%96%87'
            ),
            URITemplateAction(
                label='她做了什麼',
                uri='https://iing.tw/achievements'
            ),
            URITemplateAction(
                label='我想支持她',
                uri='https://donate.iing.tw/'
            )
        ]
    )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_H(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
    alt_text='韓國瑜候選人',
    template=ButtonsTemplate(
        thumbnail_image_url='https://image.peoplenews.tw/news/b14c1624-fc77-4531-8b62-47fdcf4e9236.jpg',
        title='Menu',
        text='Please select',
        actions=[
            URITemplateAction(
                label='他是誰',
                uri='https://zh.wikipedia.org/wiki/%E8%94%A1%E8%8B%B1%E6%96%87'
            ),
            URITemplateAction(
                label='他做了什麼',
                uri='https://iing.tw/achievements'
            ),
            URITemplateAction(
                label='我想支持他',
                uri='https://donate.iing.tw/'
            )
        ]
    )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_S(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
    alt_text='宋楚瑜候選人',
    template=ButtonsTemplate(
        thumbnail_image_url='https://image.peoplenews.tw/news/b14c1624-fc77-4531-8b62-47fdcf4e9236.jpg',
        title='Menu',
        text='Please select',
        actions=[
            URITemplateAction(
                label='他是誰',
                uri='https://zh.wikipedia.org/wiki/%E8%94%A1%E8%8B%B1%E6%96%87'
            ),
            URITemplateAction(
                label='他做了什麼',
                uri='https://iing.tw/achievements'
            ),
            URITemplateAction(
                label='我想支持他',
                uri='https://donate.iing.tw/'
            )
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
