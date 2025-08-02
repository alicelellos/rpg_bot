from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext
import logging
import os
from pathlib import Path
import random

from rpg_bot.config import config
from game.engine import GameEngine
from game.entities.character import Character
from game.utils.enums import Gender

logger = logging.getLogger(__name__)

class TelegramGameInterface:
    """Интерфейс для взаимодействия с игрой через Telegram"""
    def __init__(self, engine: GameEngine):
        self.engine = engine
        self.player_characters: Dict[int, str] = {}
        self.user_states: Dict[int, str] = {}
        self.message_callbacks: Dict[int, callable] = {}
    
    async def handle_start(self, update: Update, context: CallbackContext):
        """Обработчик команды /start"""
        user_id = update.effective_user.id
        if user_id in self.player_characters:
            char = self.engine.world.find_character(self.player_characters[user_id])
            if char:
                await update.message.reply_text(
                    f"Добро пожаловать обратно, {char.name}!",
                    reply_markup=self._get_main_menu(char)
                )
        else:
            await update.message.reply_text(
                "Добро пожаловать в мир Теней!\n"
                "Прежде чем начать, создайте своего персонажа.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Создать персонажа", callback_data="create_character")]
                ])
            )
    async def handle_create_character(self, update: Update, context: CallbackContext):
    """Обработчик создания персонажа"""
    query = update.callback_query
    await query.answer()
    
    try:
        # Генерируем персонажа с обработкой возможных ошибок
        try:
            char = self.engine.generate_character()
        except Exception as e:
            logger.error(f"Ошибка при генерации персонажа: {str(e)}")
            # Пробуем с фиксированными параметрами
            char = self.engine.create_character("Странник", Gender.MALE, "slavic")
        
        user_id = query.from_user.id
        self.player_characters[user_id] = char.id
        
        # Сохраняем персонажа
        char.save()
        
        # Помещаем в стартовую локацию
        start_loc = random.choice(["black_bastion", "silver_harbor"])
        success = self.engine.move_character(char, start_loc)
        if not success:
            logger.warning(f"Не удалось разместить персонажа в локации {start_loc}")
        
        # Отправляем описание персонажа
        await query.edit_message_text(
            f"🎭 Ваш персонаж:\n"
            f"Имя: {char.name}\n"
            f"Пол: {char.gender.value}\n"
            f"Возраст: {char.age}\n"
            f"Социальный статус: {char.social_class.value}\n"
            f"Профессия: {char.profession}\n\n"
            f"Внешность: {char.appearance.describe()}\n\n"
            f"Вы очнулись в локации: {char.location.name if char.location else 'неизвестно'}",
            reply_markup=self._get_main_menu(char)
        )
    except Exception as e:
        logger.error(f"Ошибка в handle_create_character: {str(e)}")
        await query.edit_message_text(
            "Произошла ошибка при создании персонажа. Пожалуйста, попробуйте ещё раз.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Создать персонажа", callback_data="create_character")]
            ])
        )
        
    async def handle_explore(self, update: Update, context: CallbackContext):
        """Обработчик исследования локации"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        char = self.engine.world.find_character(self.player_characters.get(user_id))
        if not char or not char.location:
            await query.edit_message_text("Ошибка: персонаж не найден")
            return
          
        # Показываем описание локации с картой
        description = char.location.describe(char, detailed=True)
        
        # Генерируем карту
        map_img = char.location.render_map(char)
        map_path = os.path.join(MAPS_DIR, f"{char.id}_map.png")
        map_img.save(map_path)
        
        # Отправляем описание и карту
        with open(map_path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=photo,
                caption=description,
                reply_markup=self._get_explore_menu(char)
            )
        
        await query.delete_message()