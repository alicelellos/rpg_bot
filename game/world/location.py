from typing import Dict, List, Optional, Tuple
import random
import json
import os
from pathlib import Path
import uuid
from datetime import datetime
from PIL import Image, ImageDraw

from rpg_bot.config import config
from ..entities.character import Character
from ..entities.item import Item
from ..utils.enums import BodyPart
from ..utils.dataclasses import Vector2

class WorldLocation:
    def __init__(self, name: str, description: str, loc_type: str, 
                 connections: List[str], services: Optional[List[str]] = None,
                 features: Optional[List[str]] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.type = loc_type
        self.connections = connections
        self.services = services or []
        self.features = features or []
        self.characters: List[Character] = []
        self.items: List[Item] = []
        self.terrain: Dict[Vector2, str] = {}
        self.positions: Dict[Character, Vector2] = {}
        
    # Все методы класса WorldLocation из оригинального кода...