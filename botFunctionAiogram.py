from aiogram import Bot, Dispatcher, executor, types
import asyncio
import checkVisa
import telegramConnection

bot = Bot(telegramConnection.telegramConnection)
dp = Dispatcher(bot)

def main():
    executor.start_polling(dp)


@dp.message_handler(commands=['visa'])
async def visa_command(message: types.Message):
    #await message.answer(text=message)
    checkVisa.main('OAM-02172-2/TP-2023')
    #checkVisa.main('OAM-42474-3/DP-2022')
    #print(checkVisa.statusViza)
    await message.reply(text=checkVisa.statusViza)

# 391074308 - Mor....

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.find('checkvisa_') != -1:
        visaNumber = message.text[message.text.find('checkvisa_')+10:]

        checkVisa.main(visaNumber)
        await message.answer(text=checkVisa.statusViza)
    else:
        await message.answer(text='no')

