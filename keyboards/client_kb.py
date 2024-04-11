from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuKB:
	kb = [
			[
				KeyboardButton(text='👨‍💻 Заработать'),
				KeyboardButton(text='📢 Рекламировать'),
			],
			[
				KeyboardButton(text='🔗 Полезные ссылки'),
				KeyboardButton(text='📱 Мой кабинет'),
			],
			[
				KeyboardButton(text='⭐️ Проверка подписки'),
				KeyboardButton(text='🤖Наши боты / 📊Статистика'),
			],
			[
				KeyboardButton(text='📋 Инструкция'),
			],
		]
	menu_kb = ReplyKeyboardMarkup(
		keyboard=kb,
		resize_keyboard=True,
		input_field_placeholder="Выберите способ подачи"
	)


class InstructionKB:
	instruction_kb = InlineKeyboardBuilder().row(InlineKeyboardButton(text='📋 Инструкция', url="https://telegra.ph/Instrukciya-04-10-35"))
