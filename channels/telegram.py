from telegram.ext import Updater, MessageHandler, Filters

from channels.channel_interface import Channel


class Telegram(Channel):
    name: str = "Telegram"

    updater: Updater
    message_handler: MessageHandler

    def __init__(self):
        self.updater = Updater("1647754237:AAGo-sBhgQvyyZjm6Y94_pjENirXpwmqiDE")
        self.message_handler = MessageHandler(Filters.text)

    def get_input(self) -> str:
        pass

    def output(self, output: str):
        self.updater.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
        pass

    def __del__(self):
        self.updater.stop()