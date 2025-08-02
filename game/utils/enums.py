from enum import Enum, auto

class Gender(Enum):
    MALE = "мужской"
    FEMALE = "женский"
    OTHER = "другой"

class SocialClass(Enum):
    PEASANT = "крестьянин"
    MERCHANT = "торговец"
    NOBLE = "дворянин"
    SOLDIER = "военный"
    CRIMINAL = "преступник"
    CLERIC = "духовенство"
    ARTISAN = "ремесленник"
    SCHOLAR = "учёный"
    ENTERTAINER = "артист"

# Все остальные Enum классы из оригинального кода...