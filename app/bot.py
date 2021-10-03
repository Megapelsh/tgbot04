from loader import bot, storage
from aiogram import types
from handlers import common


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Головне меню"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("test", "Доступні функції"),
            types.BotCommand("stop", "Па-па")
        ]
    )


# изменения внесены для проверки обновления данных в докере

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    common.register_handlers_common(dp)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
