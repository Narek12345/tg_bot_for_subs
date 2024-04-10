from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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