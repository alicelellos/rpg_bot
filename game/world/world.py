from typing import Dict, List, Optional
import random
import json
import os
from pathlib import Path
import uuid
from datetime import datetime
from PIL import Image, ImageDraw

from rpg_bot.config import config
from .location import WorldLocation
from ..entities.character import Character
from ..entities.item import Item
from ..utils.enums import *

# Базы данных перенесены сюда из оригинального кода
NAME_DATABASE = {
    "nordic": {
        Gender.MALE: ["Ролан", "Бьорн", "Эрик", "Олаф", "Торгрим", "Свен", "Харальд", "Ивар", "Ульфрик", "Гуннар"],
        Gender.FEMALE: ["Астрид", "Фрейя", "Сигрид", "Ингеборг", "Хельга", "Гудрун", "Сванхильд", "Бритта", "Эльфрида", "Рагнхильд"]
    },
    # Остальные культуры...
}

SURNAME_DATABASE = {
    "nordic": ["Железный Кулак", "Северный Волк", "Камнедробитель", "Кровавый Топор"],
    # Остальные культуры...
}

LOCATION_DATABASE = {
    "cities": [
        {
            "name": "Чёрный Бастион",
            "description": "Мрачная крепость, возвышающаяся над утёсами...",
            "districts": ["Крепость", "Рыночная площадь", "Порт", "Трущобы"],
            "services": ["blacksmith", "tavern", "temple", "market"]
        }
    ],
    # Остальные локации...
}

class GameWorld:
    """Игровой мир с локациями и персонажами"""
    def __init__(self):
        self.locations: Dict[str, WorldLocation] = {}
        self.characters: Dict[str, Character] = {}
        self.items: Dict[str, Item] = {}
        self._setup_world()
        
    def _setup_world(self):
        """Инициализирует игровой мир"""
        for city_data in LOCATION_DATABASE["cities"]:
            city = WorldLocation(
                name=city_data["name"],
                description=city_data["description"],
                loc_type="city",
                connections=[f"district:{dist}" for dist in city_data["districts"]],
                services=city_data.get("services", [])
            )
            self.locations[city_data["name"].lower()] = city
            
            for district in city_data["districts"]:
                district_desc = random.choice([
                    f"{district} города {city_data['name']}. {random.choice(['Шумное', 'Тихое', 'Оживлённое'])} место.",
                    f"{district} - {random.choice(['бедный', 'богатый', 'средний'])} район {city_data['name']}."
                ])
                
                district_loc = WorldLocation(
                    name=f"{district}",
                    description=district_desc,
                    loc_type="district",
                    connections=[city_data["name"].lower()],
                    services=city_data.get("services", [])
                )
                self.locations[f"district:{district.lower()}"] = district_loc
        
        # Остальная инициализация мира...
    
    # Остальные методы класса GameWorld из оригинального кода...