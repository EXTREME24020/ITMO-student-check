import telebot # импорт библиотеки для работы с ботами в тг

bot = telebot.TeleBot("") # сюда вписывается токен бота из botfather
@bot.message_handler(commands=['itmostudent']) # команда для запуска проги

def check_itmo_student(message): # главная функция
    user_id = message.from_user.id # сюда запишем айди пользователя, кто отправил команду
    try:
        chat_info = bot.get_chat(user_id) # получаем айди
        bio = chat_info.bio # здесь будет раздел "о себе" из профиля пользователя
        if bio and 'itmo' in bio.lower(): # проверяем есть ли в разделе "о себе" упоминание ИТМО
            bot.reply_to(message, "Это студент ИТМО") # если есть, то отвечаем положительно
        else:
            bot.reply_to(message, "Это не студент ИТМО") # иначе отвечаем отрицательно

    except Exception as e: # обработка возможной ошибки
        bot.reply_to(message, f"Ошибка {e}") # вывод возможной ошикби

bot.polling(none_stop=True) # запуск бота