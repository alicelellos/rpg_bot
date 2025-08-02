from typing import Dict, List, Optional
import random
import json
import os
from pathlib import Path
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

from rpg_bot.config import config
from .body import CharacterBody
from .item import Item, Weapon, ArmorItem, ClothingItem, UnderwearItem
from ..utils.enums import *
from ..systems.combat import CombatStyle
from ..systems.dialogue import DialogueMood

class CharacterAppearance:
    # Класс CharacterAppearance из оригинального кода...
    pass

class CharacterNeeds:
    # Класс CharacterNeeds из оригинального кода...
    pass

class CharacterPersonality:
    # Класс CharacterPersonality из оригинального кода...
    pass

class CharacterInventory:
    # Класс CharacterInventory из оригинального кода...
    pass

class CharacterEquipment:
    # Класс CharacterEquipment из оригинального кода...
    pass

class CharacterSkills:
    # Класс CharacterSkills из оригинального кода...
    pass

class Character:
    """Полная реализация персонажа с детализированными системами"""
    def __init__(self, name: str, gender: Gender, culture: str = "nordic"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.gender = gender
        self.culture = culture
        self.age = random.randint(18, 60)
        self.social_class = random.choice(list(SocialClass))
        self.profession = self._generate_profession()
        self.appearance = CharacterAppearance(gender)
        self.personality = CharacterPersonality()
        self.needs = CharacterNeeds()
        self.skills = CharacterSkills()
        self.inventory = CharacterInventory()
        self.equipment = CharacterEquipment()
        self.body = CharacterBody(gender)
        self.location: Optional['WorldLocation'] = None
        self.position = Vector2(0, 0)
        self.combat_style = random.choice(list(CombatStyle))
        self.companions: List[Character] = []
        self.last_meal_time = datetime.now() - timedelta(hours=random.randint(1, 6))
        self.last_sleep_time = datetime.now() - timedelta(hours=random.randint(1, 12))
        self.is_sleeping = False
        self.is_naked = False
        self.is_combat = False
        self._setup_initial_gear()
    
    # Все методы класса Character из оригинального кода...