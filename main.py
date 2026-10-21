import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(F.text)
async def echo_handler(message: Message):
    """Отправляет полученный текст обратно пользователю."""
    await message.reply(message.text)


@dp.message()
async def fallback_handler(message: Message):
    """Не повторяет то, что не является текстом."""
    await message.reply("I can only repeat text =( ")


async def main():
    logging.info("Эхо-бот запущен.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
