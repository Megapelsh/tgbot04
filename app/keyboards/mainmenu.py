from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Додати авто в базу"),
        ],
        [
            KeyboardButton(text="Пошук за держномером"),
            KeyboardButton(text="Пошук за VIN")
        ],
    ],
    resize_keyboard=True
)