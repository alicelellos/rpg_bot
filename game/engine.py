from typing import Dict, List, Optional
from datetime import datetime
import logging
from pathlib import Path
import json
import os

from rpg_bot.config import config
from .world.world import GameWorld
from .systems.dialogue import DialogueSystem
from .systems.combat import CombatSystem
from .entities.character import Character

logger = logging.getLogger(__name__)

class GameEngine:
    """Основной игровой движок, управляющий всеми системами"""
    def __init__(self):
        self.world = GameWorld()
        self.dialogue_system = DialogueSystem(self.world)
        self.combat_system = CombatSystem(self.world)
        self.last_update_time = datetime.now()
        self.load_game()
    
    def update(self):
        """Обновляет состояние игры"""
        now = datetime.now()
        time_passed = now - self.last_update_time
        self.last_update_time = now
        
        # Обновляем всех персонажей
        for char in self.world.characters.values():
            char.update(time_passed)
        
        # Обновляем бои
        for combat in list(self.combat_system.active_combats.values()):
            if combat.is_ended():
                self.combat_system.end_combat(combat.id)
            else:
                events = combat.execute_turn()
                for event in events:
                    self.combat_system._add_to_history(combat.id, event)
    
    def create_character(self, name: str, gender: 'Gender', culture: str = "nordic") -> Character:
        """Создаёт нового персонажа с заданными параметрами"""
        char = Character(name, gender, culture)
        self.world.characters[char.id] = char
        return char
    
    def generate_character(self) -> Character:
        """Генерирует случайного персонажа"""
        from .utils.enums import Gender
        from .world.world import NAME_DATABASE, SURNAME_DATABASE
        
        try:
            culture = random.choice(list(NAME_DATABASE.keys()))
            available_genders = [g for g in Gender if g in NAME_DATABASE[culture]]
            if not available_genders:
                available_genders = [Gender.MALE, Gender.FEMALE]
            
            gender = random.choice(available_genders)
            first_name = random.choice(NAME_DATABASE[culture][gender])
            surname = random.choice(SURNAME_DATABASE[culture])
            name = f"{first_name} {surname}"
            
            return self.create_character(name, gender, culture)
            
        except Exception as e:
            logger.error(f"Error generating character: {e}")
            return self.create_character("Странник", Gender.MALE, "slavic")
    
    def move_character(self, character: Character, location_name: str) -> bool:
        """Перемещает персонажа в указанную локацию"""
        return self.world.move_character(character, location_name)
    
    def start_dialogue(self, initiator: Character, target: Character) -> 'Dialogue':
        """Начинает диалог между двумя персонажами"""
        return self.dialogue_system.start_dialogue(initiator, target)
    
    def start_combat(self, participants: List[Character]) -> 'Combat':
        """Начинает бой между участниками"""
        return self.combat_system.start_combat(participants)
    
    def save_game(self):
        """Сохраняет текущее состояние игры"""
        self.world.save()
        self.dialogue_system.save_dialogue_history()
        self.combat_system.save_combat_history()
        
        game_state = {
            "last_update_time": self.last_update_time.isoformat()
        }
        
        file_path = config.SAVE_DIR / "game_state.json"
        with open(file_path, "w") as f:
            json.dump(game_state, f, indent=2)
    
    def load_game(self):
        """Загружает сохранённое состояние игры"""
        if not self.world.load():
            self.world = GameWorld()
        
        self.dialogue_system.load_dialogue_history()
        self.combat_system.load_combat_history()
        
        game_state_file = config.SAVE_DIR / "game_state.json"
        if os.path.exists(game_state_file):
            with open(game_state_file, "r") as f:
                game_state = json.load(f)
                self.last_update_time = datetime.fromisoformat(game_state["last_update_time"])