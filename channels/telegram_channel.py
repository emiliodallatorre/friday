import time

from telegram import Update
from telegram.ext import MessageHandler, Filters, CallbackContext
from telegram.ext.updater import Updater

from channels.channel_interface import Channel


class Telegram(Channel):
    name: str = "Telegram"

    updater: Updater
    update: Update

    last_message: str = None

    def save_message(self, update: Update, context: CallbackContext):
        self.update = update
        self.last_message = update.message.text

    def __init__(self):
        self.updater = Updater("1647754237:AAGo-sBhgQvyyZjm6Y94_pjENirXpwmqiDE")

        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.save_message)
        self.updater.dispatcher.add_handler(echo_handler)

        self.updater.start_polling()

    def get_input(self) -> str:
        last_message = self.last_message

        while True:
            time.sleep(1)
            if last_message != self.last_message:
                return self.last_message

    def output(self, output: str):
        self.updater.bot.send_message(chat_id=self.update.effective_chat.id, text=output)
