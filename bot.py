# Импортируем нужные компоненты, импорт обработчика команд, обработчик текстовых сообщений
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# Будем записывать отчет о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("908634581:AAEZYDLx0qq4MIcbfdonViKeQgY6J3MsOpM", request_kwargs=PROXY)
    # Команды в чате Telegram выглядят как "/команда".
    # Научим бота реагировать на команду /start - она автоматически выполняется при подключении к боту.
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    # Добавим новый handler в main()
    mybot.start_polling()
    mybot.idle()

# Создадим функцию greet_user
# Она будет вызываться,
# когда пользователь в чате напишет /start вручную или подключится к боту в первый раз.
def greet_user(bot, update):
    text = 'Привет, как дела?'
    print(text)
    update.message.reply_text(text)

# Добавим функцию, которая будет "отвечать" пользователю
def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

# Вызываем функцию - эта строчка собственно запускает бота
main()

