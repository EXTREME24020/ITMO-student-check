import telebot # импорт библиотеки для работы с ботами в тг

bot = telebot.TeleBot("") # сюда вписывается токен бота из botfather
@bot.message_handler(commands=['itmostudent']) # команда для запуска проги

def check_itmo_student(message): # главная функция


bot.polling(none_stop=True) # запуск бота