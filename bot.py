# coding=utf-8

import funcs as f
import telebot
import config_file as conf
from telebot import types


token = conf.getToken()
bot = telebot.TeleBot(token)





@bot.message_handler(commands=['start'])
def handle_start_help(message):
     bot.send_message(message.chat.id, text='Для начала работы с ботом поприветствуйте его.')


@bot.message_handler(content_types=["text"])
def start(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'здравствуйте' or message.text.lower() == 'здравствуй':
        keyboard = types.InlineKeyboardMarkup();
        key_status = types.InlineKeyboardButton(text='Узнать данные о документе', callback_data='status');
        keyboard.add(key_status);
        key_pension = types.InlineKeyboardButton(text='Узнать данные о социальных выплатах', callback_data='pension');
        keyboard.add(key_pension);
        key_help = types.InlineKeyboardButton(text='Получить информацию о правах и льготах', callback_data='help');
        keyboard.add(key_help);
        bot.send_message(message.chat.id, text='Вас приветствует бот SocShield. Чем я могу Вам помочь?', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, text='Извините, я Вас не понял.')

def identifier_status(message):
    if len(message.text) == 8:
        keyboard = types.InlineKeyboardMarkup();
        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.from_user.id, f.getData(message.text), reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup();
        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.chat.id, 'Неверный идентификатор SocShield', reply_markup=keyboard)

def identifier_pension(message):
    if len(message.text) == 8:
        keyboard = types.InlineKeyboardMarkup();
        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.from_user.id, f.getPension(message.text), reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup();
        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.chat.id, 'Неверный идентификатор SocShield', reply_markup=keyboard)

def identifier_help(message):
    if len(message.text) == 8:
        keyboard = types.InlineKeyboardMarkup();
        if(f.getHelp(message.text)!=''):
            text = 'Здравствуйте! Информация для Вас готова!'
            key_helpshield = types.InlineKeyboardButton(text='Ваша помощь', url=f.getHelp(message.text));
            keyboard.add(key_helpshield)
        else:
            text = 'Срок Вашего документа истек.'

        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.from_user.id, text, reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup();
        key_back = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='backtomenu');
        keyboard.add(key_back)
        bot.send_message(message.chat.id, 'Неверный идентификатор SocShield', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'status':
        bot.send_message(call.message.chat.id, 'Введите свой идентификатор SocShield')
        bot.register_next_step_handler(call.message, identifier_status)
    elif call.data == 'pension':
        bot.send_message(call.message.chat.id, 'Введите свой идентификатор SocShield')
        bot.register_next_step_handler(call.message, identifier_pension)
    elif call.data == 'backtomenu':
        keyboard = types.InlineKeyboardMarkup();
        key_status = types.InlineKeyboardButton(text='Узнать данные о документе', callback_data='status');
        keyboard.add(key_status);
        key_pension = types.InlineKeyboardButton(text='Узнать данные о социальных выплатах', callback_data='pension');
        keyboard.add(key_pension);
        key_help = types.InlineKeyboardButton(text='Получить информацию о правах и льготах', callback_data='help');
        keyboard.add(key_help);
        bot.send_message(call.message.chat.id, text='Вас приветствует бот SocShield. Чем я могу Вам помочь?', reply_markup=keyboard)
    elif call.data == 'help':
        bot.send_message(call.message.chat.id, 'Введите свой идентификатор SocShield')
        bot.register_next_step_handler(call.message, identifier_help)


if __name__ == '__main__':
    bot.polling(none_stop=True)