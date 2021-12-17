from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, Dispatcher, CommandHandler, CallbackContext
from telegram.ext.updater import Updater

from channels.channel_interface import Channel


class Telegram(Channel):
    name: str = "Telegram"

    updater: Updater
    message_handler: MessageHandler
    dispatcher: Dispatcher
    update: Update

    def start(self, update: Update, context: CallbackContext):
        self.update = update
        print(self.update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def echo(self, update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def __init__(self):
        self.updater = Updater("1647754237:AAGo-sBhgQvyyZjm6Y94_pjENirXpwmqiDE")
        self.dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.start)
        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(echo_handler)

        self.updater.start_polling()

    def get_input(self) -> str:
        pass

    def output(self, output: str):
        self.updater.bot.send_message(chat_id=self.update.effective_chat.id, text="I'm a bot, please talk to me!")
        pass

    def __del__(self):
        self.updater.stop()
