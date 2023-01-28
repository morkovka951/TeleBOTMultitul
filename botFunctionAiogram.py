from aiogram import Bot, Dispatcher, executor, types

import checkVisa
import telegramConnection

bot = Bot(telegramConnection.telegramConnection)
dp = Dispatcher(bot)

def main():
    executor.start_polling(dp)

@dp.message_handler(commands=['visa'])
async def visa_command(message: types.Message):
    checkVisa.main('OAM-42474-3/DP-2022')
    await message.reply(text=checkVisa.statusViza)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)



