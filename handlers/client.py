from aiogram.types import Message
from aiogram.filters import CommandStart

from create_bot import dp
from db.models import User
from db.create_db import session
from keyboards import client_kb


async def start_cmd(message: Message):
	"""Команда /start."""
	# Регистрируем пользоавтеля если он еще не зарегестрирован.
	User.register_user(session, tg_id=message.from_user.id)

	await message.answer(f'Привет, {message.from_user.first_name}!\n\nПожалуйста, убедитесь, что вы прочитали <a href="https://telegra.ph/Instrukciya-04-10-35">инструкцию</a> по использованию бота! Используя бота, вы автоматически соглашаетесь с политикой конфиденциальности.', parse_mode="HTML", disable_web_page_preview=True, reply_markup=client_kb.menu_kb)


async def earn_cmd(message: Message):
	"""Команда на текст Заработать."""
	await message.answer("Заработок.")


async def ads_cmd(message: Message):
	"""Команда на текст Рекламировать."""
	await message.answer("Реклама.")


async def useful_links_cmd(message: Message):
	"""Команда на текст Полезные ссылки."""
	await message.answer("Ссылки.")


async def my_office_cmd(message: Message):
	"""Команда на текст Мой кабинет."""
	await message.answer("Кабинет.")


async def subs_check_cmd(message: Message):
	"""Команда на текст Проверка подписки."""
	await message.answer("Подписка.")


async def our_bots_and_statistics_cmd(message: Message):
	"""Команда на текст Наши боты / Статистика."""
	await message.answer("Статистика.")


async def instructions_cmd(message: Message):
	"""Команда на текст Инструкция."""
	await message.answer("Инструкция.")



def register_client_handlers(dp):
	dp.message.register(start_cmd, CommandStart())

	# Регистрируем обработчики команд главной меню.
	dp.message.register(earn_cmd, lambda message: '👨‍💻 Заработать' in message.text)
	dp.message.register(ads_cmd, lambda message: '📢 Рекламировать' in message.text)
	dp.message.register(useful_links_cmd, lambda message: '🔗 Полезные ссылки' in message.text)
	dp.message.register(my_office_cmd, lambda message: '📱 Мой кабинет' in message.text)
	dp.message.register(subs_check_cmd, lambda message: '⭐️ Проверка подписки' in message.text)
	dp.message.register(our_bots_and_statistics_cmd, lambda message: '🤖Наши боты / 📊Статистика' in message.text)
	dp.message.register(instructions_cmd, lambda message: '📋 Инструкция' in message.text)
