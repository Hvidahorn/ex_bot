import aiogram
from aiogram import Bot, Dispatcher, executor, types
import test
import config
import datetime
import pytz
import json
import logging

logging.basicConfig(level=logging.INFO)

PY_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_SN = config.TIMEZONE_SN


bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Greetings! I can show you exchange rates.\n' +
                         'To get the exchange rates press /list.\n' +
                         'To get some help press /help')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    keyboard = aiogram.types.InlineKeyboardMarkup()
    keyboard.add(aiogram.types.InlineKeyboardButton(text='My tg :)', url='https://t.me/Hvidahorn'))
    await message.answer('1) To receive a list of available currencies press /list.\n' +
                         '2) Click on the currency you are interested in.\n' +
                         '3) You will receive a message containing information regarding the source and the target '
                         'currencies.\n' +
                         '4) Click "update" to receive the current information regarding the request.\n',
                         reply_markup=keyboard)


@dp.message_handler(commands=['list'])
async def list_command(message: types.Message):
    keyboard = aiogram.types.InlineKeyboardMarkup()
    keyboard.row(
        aiogram.types.InlineKeyboardButton('CAD', callback_data='get_CAD'),
        aiogram.types.InlineKeyboardButton('HKD', callback_data='get_HKD'),
        aiogram.types.InlineKeyboardButton('ISK', callback_data='get_ISK'),
        aiogram.types.InlineKeyboardButton('PHP', callback_data='get_PHP'),
        aiogram.types.InlineKeyboardButton('DKK', callback_data='get_DKK'),
        aiogram.types.InlineKeyboardButton('HUF', callback_data='get_HUF')
    )
    keyboard.row(
        aiogram.types.InlineKeyboardButton('CZK', callback_data='get_CZK'),
        aiogram.types.InlineKeyboardButton('GBP', callback_data='get_GBP'),
        aiogram.types.InlineKeyboardButton('RON', callback_data='get_RON'),
        aiogram.types.InlineKeyboardButton('SEK', callback_data='get_SEK'),
        aiogram.types.InlineKeyboardButton('IDR', callback_data='get_IDR'),
        aiogram.types.InlineKeyboardButton('INR', callback_data='get_INR')
    )
    keyboard.row(
        aiogram.types.InlineKeyboardButton('BRL', callback_data='get_BRL'),
        aiogram.types.InlineKeyboardButton('RUB', callback_data='get_RUB'),
        aiogram.types.InlineKeyboardButton('HRK', callback_data='get_HRK'),
        aiogram.types.InlineKeyboardButton('JPY', callback_data='get_JPY'),
        aiogram.types.InlineKeyboardButton('THB', callback_data='get_THB'),
        aiogram.types.InlineKeyboardButton('CHF', callback_data='get_CHF')
    )
    keyboard.row(
        aiogram.types.InlineKeyboardButton('EUR', callback_data='get_EUR'),
        aiogram.types.InlineKeyboardButton('MYR', callback_data='get_MYR'),
        aiogram.types.InlineKeyboardButton('BGN', callback_data='get_BGN'),
        aiogram.types.InlineKeyboardButton('TRY', callback_data='get_TRY'),
        aiogram.types.InlineKeyboardButton('CNY', callback_data='get_CNY'),
        aiogram.types.InlineKeyboardButton('NOK', callback_data='get_NOK')
    )
    keyboard.row(
        aiogram.types.InlineKeyboardButton('NZD', callback_data='get_NZD'),
        aiogram.types.InlineKeyboardButton('ZAR', callback_data='get_ZAR'),
        aiogram.types.InlineKeyboardButton('USD', callback_data='get_USD'),
        aiogram.types.InlineKeyboardButton('MXN', callback_data='get_MXN'),
        aiogram.types.InlineKeyboardButton('SGD', callback_data='get_SGD'),
        aiogram.types.InlineKeyboardButton('AUD', callback_data='get_AUD')
    )
    keyboard.row(
        aiogram.types.InlineKeyboardButton('ILS', callback_data='get_ILS'),
        aiogram.types.InlineKeyboardButton('KRW', callback_data='get_KRW'),
        aiogram.types.InlineKeyboardButton('PLN', callback_data='get_PLN')
    )
    await message.answer('Click on currency of choice.\n' +
                         'Currencies based on current rate of USD.',
                         reply_markup=keyboard)


'''
@dp.callback_query_handler(lambda call: True)
def id_callback(query):
    data = query.data
    if data.startswith('get_'):
        get_ex_callback(query)

def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])

def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = test.get_exchange(ex_code)
    bot.send_message(
        message.chat.id, serialize_ex(ex),
        reply_markup=get_update_keyboard(ex),
        parse_mode='HTML'
    )

def get_update_keyboard(ex):
    keyboard = aiogram.types.InlineKeyboardMarkup()
    keyboard.row(
        aiogram.types.InlineKeyboardButton('Update',
                                           callback_data=json.dumps({
                                               't': 'u',
                                               'e': {
                                                   'c': ex['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP',
                                                   'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB',
                                                   'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR',
                                                   'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN']
    }
                                           })
                                           )
    )
    return keyboard

def serialize_ex(ex_json, diff=None):
    result = '<b>' + ex_json['base'] + ' -> ' + ex_json[''] + ':</b>\n\n' + \
             'Buy: ' + ex_json['']
    return result
'''


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
