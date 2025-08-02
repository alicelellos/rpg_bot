from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from bot.interface import TelegramGameInterface
from game.engine import GameEngine

def main():
    # Инициализация игрового движка
    engine = GameEngine()
    
    # Создаём интерфейс для Telegram
    tg_interface = TelegramGameInterface(engine)
    
    # Настройка бота
    from rpg_bot.config import config
    app = (
        Application.builder()
        .token(config.TOKEN)
        .build()
    )
    
    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", tg_interface.handle_start))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_create_character, pattern="^create_character$"))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_explore, pattern="^explore$"))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_inventory, pattern="^inventory$"))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_stats, pattern="^stats$"))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_save, pattern="^save$"))
    app.add_handler(CallbackQueryHandler(tg_interface.handle_main_menu, pattern="^main_menu$"))
    
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()