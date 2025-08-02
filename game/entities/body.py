from typing import Dict, List, Optional, Tuple
import random
from datetime import datetime, timedelta
from collections import defaultdict

from ..utils.enums import *
from ..utils.dataclasses import DamageModel

class BodyPartState:
    # Класс BodyPartState из оригинального кода...
    pass

class CharacterBody:
    """Физическое тело персонажа с детализированной анатомией"""
    def __init__(self, gender: Gender):
        self.gender = gender
        self.parts: Dict[BodyPart, BodyPartState] = {
            part: BodyPartState(part) for part in BodyPart
        }
        self.fluids: Dict[BodilyFluidType, float] = defaultdict(float)
        self.health = 100.0
        self.max_health = 100.0
        self.stamina = 100.0
        self.max_stamina = 100.0
        self.bleeding_rate = 0.0
        self.pain_level = 0.0
    
    # Все методы класса CharacterBody из оригинального кода...