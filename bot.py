# Импортируем нужные компоненты, импорт обработчика команд
from telegram.ext import Updater, CommandHandler

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# Создадим функцию greet_user
# Она будет вызываться,
# когда пользователь в чате напишет /start вручную или подключится к боту в первый раз.
def greet_user(bot, update):
    text = 'Привет, как дела?'
    print(text)
    update.message.reply_text(text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("908634581:AAEZYDLx0qq4MIcbfdonViKeQgY6J3MsOpM", request_kwargs=PROXY)
    # Команды в чате Telegram выглядят как "/команда".
    # Научим бота реагировать на команду /start - она автоматически выполняется при подключении к боту.
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()