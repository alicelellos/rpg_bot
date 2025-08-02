import random
from typing import List, Dict, Any

def random_name(gender: 'Gender', culture: str) -> str:
    """Генерирует случайное имя"""
    from .enums import Gender
    from ..world.world import NAME_DATABASE, SURNAME_DATABASE
    
    try:
        first_name = random.choice(NAME_DATABASE[culture][gender])
        surname = random.choice(SURNAME_DATABASE[culture])
        return f"{first_name} {surname}"
    except:
        return "Неизвестный" if gender == Gender.MALE else "Неизвестная"

# Другие вспомогательные функции...