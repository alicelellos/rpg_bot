# Инициализация игрового модуля
from .engine import GameEngine
from .world.world import WorldLocation, GameWorld
from .entities.character import Character
from .entities.item import Item, Weapon, ArmorItem, ClothingItem, UnderwearItem, FoodItem, DrinkItem
from .systems.combat import CombatSystem, Combat
from .systems.dialogue import DialogueSystem, Dialogue
from .utils.enums import *

__all__ = [
    'GameEngine', 'WorldLocation', 'GameWorld', 'Character',
    'Item', 'Weapon', 'ArmorItem', 'ClothingItem', 'UnderwearItem', 'FoodItem', 'DrinkItem',
    'CombatSystem', 'Combat', 'DialogueSystem', 'Dialogue'
]