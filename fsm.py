from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_template, send_T, send_H, send_S


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "我想認識"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "韓國瑜"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "蔡英文"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "宋楚瑜"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "想看看其他人"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_button_template(reply_token, "總統候選人")

    def on_exit_state1(self, evnet):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_H(reply_token, "韓國瑜")

    def on_exit_state2(self, event):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_T(reply_token, "蔡英文")

    def on_exit_state3(self, event):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        send_S(reply_token, "宋楚瑜")

    def on_exit_state4(self, event):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")
        self.go_back()

    def on_exit_state5(self, event):
        print("Leaving state5")