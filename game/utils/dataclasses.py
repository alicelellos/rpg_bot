from dataclasses import dataclass
import math
from typing import Dict, List, Optional, Tuple
from enum import Enum

@dataclass
class Vector2:
    x: float
    y: float
    
    def distance_to(self, other: 'Vector2') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)
    
    # Остальные методы Vector2...

@dataclass
class MaterialProperties:
    density: float
    hardness: float
    toughness: float
    flexibility: float
    sharpness: float
    conductivity: float
    durability: float
    comfort: float

# Остальные dataclasses...