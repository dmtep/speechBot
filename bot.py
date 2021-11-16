# 
import logging

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters
)
import setting

# Логи предоставляют разработчикам дополнительный набор глаз, 
# которые постоянно смотрят на поток, через который проходит приложение.
logging.basicConfig(filename = "bot.log", level = logging.INFO)

from voice import text_to_file

TOKEN = setting.API_KEY

print('Bot RUNING')

def hello(update,context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_handler(update, context):
    help_text = """Для того, чтобы преобразовать текст в аудиосообщение - используйте наш Бот.Пришлите любой текст обычным сообщением и он превратится в аудио сообщение!"""
    update.message.reply_text(help_text)

def reply(update, context):
    file_name = text_to_file(update.message.text)
    # update.message.reply_text("Проговорим текст: " +update.message.text)
    update.message.reply_voice(voice = open(file_name, "rb"))
    
updater = Updater(TOKEN)

ud = updater.dispatcher

ud.add_handler(CommandHandler("hello", hello))
ud.add_handler(CommandHandler("help", help_handler))
ud.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
logging.info("Bot is started")
updater.start_polling()
updater.idle()
