from typing import Dict
from ..utils.dataclasses import Vector2

def generate_terrain(location_type: str, width: int, height: int) -> Dict[Vector2, str]:
    """Генерирует местность для локации"""
    terrain_types = {
        "city": ["street", "building", "alley", "plaza", "fountain"],
        "forest": ["tree", "bush", "path", "stream", "clearing"],
        "tavern": ["table", "bar", "hearth", "staircase", "private_room"]
    }
    
    available_terrain = terrain_types.get(location_type, ["ground"])
    terrain = {}
    
    for x in range(width):
        for y in range(height):
            pos = Vector2(x, y)
            terrain[pos] = random.choice(available_terrain)
    
    return terrain