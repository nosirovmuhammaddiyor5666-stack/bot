import asyncio
from  aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message ,KeyboardButton,ReplyKeyboardMarkup,BotCommand

bot = Bot(token= "8795474224:AAF1HRrLpyrYBdqZHJrOlR8pqAssak6rVQQ")
dp = Dispatcher()

@dp.message(Command("start"))
async def handStart(message: Message):
    await message.answer("Botga hush kelibsiz")

@dp.message(Command("help"))
async def handHelp(message: Message):
    await message.answer("yordam uchun @MDlyor ga murojat qiling")

@dp.message(Command("admin"))
async def handAdmin(message: Message):
    await message.answer("1)Admin: @MDlyor")

@dp.message(Command("coder"))
async def handCoder(message: Message):
    await message.answer("@MDlyor")

@dp.message(Command("settings"))
async def handSettings(message: Message):
    await message.answer("⚙️ Sozlamalar bo'limi:\nTez orada bu yerda tillarni o'zgartirish imkoniyati qo'shiladi.")

@dp.message(F.text=="salom")
async def salomHand(message: Message):
    await message.answer("Valaykum salom nma yordam bera olaman")

@dp.message()
async def give(message: Message):
    await bot.send_message(chat_id=5891166251,text= f"Sizga habar yuborildi: {message.text}")
    await message.answer("Habaringiz qabul qilindi!")


@dp.message(F.contact)
@dp.message(F.location)
@dp.message(F.voice)
@dp.message(F.photo)
@dp.message(F.audio)
@dp.message(F.text)
async def get_text(message: Message):
    await message.answer("Habaringiz qabul qilindi!")


    

async def main():
    await bot.set_my_commands(commands=[BotCommand(command="start",description="botni ishga tushurish"),
                                        BotCommand(command= "help",description="Yordam murojati"),
                                        BotCommand(command= "admin",description="admin username"),
                                        BotCommand(command= "settings",description="sozlamalar"),
                                        BotCommand(command= "coder",description="@MDlyor")
                                        ])
    await dp.start_polling(bot)

asyncio.run(main())
