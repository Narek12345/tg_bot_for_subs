import asyncio
import logging

from create_bot import bot, dp
from db.create_db import create_database

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
	create_database()
    asyncio.run(main())
