# Импортируем нужные компоненты, импорт обработчика команд, обработчик текстовых сообщений
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import API_KEY

# Будем записывать отчет о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# Настройки прокси
# PROXY = {'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {
#         'username': settings.PROXY_USERNAME,
#         'password': settings.PROXY_PASSWORD
#     }
# }


# Создадим функцию greet_user
# Она будет вызываться,
# когда пользователь в чате напишет /start вручную или подключится к боту в первый раз.
def greet_user(update, context):
    text = 'Привет! Я бот-дразнилка.\nКак у тебя дела?'
    update.message.reply_text(text)


# Добавим функцию, которая будет "отвечать" пользователю
def talk_to_me(update, context):
    user_text = update.message.text
    ask_bot = ('Это у меня ' + user_text.lower() + '!\n' + 'А у тебя как?')
    update.message.reply_text(ask_bot)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
if __name__ == "__main__":
    def main():
        # для использования прокси
        # mybot = Updater(settings.API_KEY, request_kwargs=PROXY)
        mybot = Updater(API_KEY, use_context=True)
        # Команды в чате Telegram выглядят как "/команда".
        # Научим бота реагировать на команду /start - она автоматически выполняется при подключении к боту.
        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start", greet_user))
        dp.add_handler(MessageHandler(Filters.text, talk_to_me))    # Добавим новый handler в main()
        mybot.start_polling()
        mybot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
    main()


