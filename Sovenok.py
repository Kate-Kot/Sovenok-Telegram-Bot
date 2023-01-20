import telebot
import random
import Token_sova
import time

bot = telebot.TeleBot(Token_sova.Token_sova)
#'message.from_user.id' or 'message.chat.id' ==?

@bot.message_handler(commands=['start', 'help', 'Help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет. Я Милый Совёнок!')
    bot.register_next_step_handler(message, privet)
#    bot.send_message(message.chat.id, 'Привет. Я Милый Совёнок!')



@bot.message_handler(content_types=['text'])
def privet(message):
    bot.send_message(message.from_user.id, 'Привет. Я Милый Совёнок! Давай играть! Я буду отправлять тебе примеры, а ты пиши ответ. Удачи! У тебя всё получится!')
    sti = 'CAACAgIAAxkBAAEFtbpjDMw9bNPDO7YwBu73ClydEVflVAACJAADwZxgDEgkWrolDSiOKQQ'
    bot.send_sticker(message.from_user.id, sti)
    bot.register_next_step_handler(message, question)


@bot.message_handler(content_types=['text'])
def question(message):
    global a
    global b
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    bot.send_message(message.from_user.id, f'Подскажи, сколько будет {a} * {b} ?')
    bot.register_next_step_handler(message, logik)


@bot.message_handler(content_types=['text'])
def logik(message):
    global resh
    resh = a*b
    try:
        if message.text.isdigit():
            otvet = int(message.text)
        else:
            otvet = -1
    except AttributeError:
        otvet = 0

    if otvet == resh:
        right_resh(message)
    else:
        incorrect_resh(message)


@bot.message_handler(content_types=['text'])
def right_resh(message):
    #bot.send_message(message.from_user.id, 'Ура! Правильно! Ты молодец!!!')
    bot.reply_to(message, 'Ура! Правильно! Ты молодец!!!')
    sti_rad = ['CAACAgIAAxkBAAEFtbxjDM0c3d1Gjl9z0Gvs3RbFgc4D2QACMQADwZxgDMYOMqCLWnWlKQQ', 'CAACAgIAAxkBAAEFtb5jDM1Fj1bwvSzA8GLutcOGh3QsNAACMAADwZxgDC_O3xNMCmecKQQ', 'CAACAgIAAxkBAAEFtcBjDM1jthdjJ3KPqaE4p01TakxoPQACKwADwZxgDFxmIgABy0eE7SkE', 'CAACAgIAAxkBAAEFtcJjDM1y5293VlFA0Q8cvrgjIwks1gACLAADwZxgDLDdeXbj2CCVKQQ', 'CAACAgIAAxkBAAEFtyRjDeDvkhRE-05AagvUasRO7O60zgACIAADwZxgDGWWbaHi0krRKQQ', 'CAACAgIAAxkBAAEFtyZjDeFp-Vzur7MsznvbnEA1Xe6hqAACKgADwZxgDCPGi6TA6qoMKQQ', 'CAACAgIAAxkBAAEFtyhjDeGQ-7yI4DgLF_Ed-q8CVjM6QgACKQADwZxgDPBLqR6_2N98KQQ', 'CAACAgIAAxkBAAEFtypjDeG873PECT1iUNJTk7T37AtUegACMQADwZxgDMYOMqCLWnWlKQQ', 'CAACAgIAAxkBAAEFtzZjDeKWzMQsHVTtCKd5dmkoWM5S4wACKAADwZxgDKEyH9MLlol4KQQ']
    bot.send_sticker(message.from_user.id, random.choice(sti_rad))
    question(message)

@bot.message_handler(content_types=['text'])
def incorrect_resh(message):
    bot.reply_to(message, f'Мне жаль, но тут ошибка. {a} * {b} = {resh}')
    #bot.send_message(message.from_user.id, f'Мне жаль, но тут ошибка. {a} * {b} = {resh}')
    sti_sad = ['CAACAgIAAxkBAAEFtyxjDeH0HEN499dLeZisJ8dfm8R8bAACIwADwZxgDJDk7nBqLVflKQQ', 'CAACAgIAAxkBAAEFty5jDeIE5KuUKwxT64_F7IgovTFZcgACJQADwZxgDLGbFNkrHorWKQQ', 'CAACAgIAAxkBAAEFtzBjDeIYU9nbb63p9RPVyoGz3TCYUAACJwADwZxgDDyooGzktoF7KQQ', 'CAACAgIAAxkBAAEFtzJjDeI9lLh2N5fxQxJkNtoM2qI3gQACLQADwZxgDOM08idy_5BlKQQ', 'CAACAgIAAxkBAAEFtzRjDeJZOoKhJxNVHkRfWTlyJlFm_wACLwADwZxgDK-MRHjuZdGKKQQ']
    bot.send_sticker(message.from_user.id, random.choice(sti_sad))
    bot.send_message(message.from_user.id, f'Подскажи, сколько будет {a} * {b} ?')
    bot.register_next_step_handler(message, logik)
    


           
# запуск бота
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as err:
        time.sleep(0.1)
    
