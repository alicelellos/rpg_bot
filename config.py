import os
from pathlib import Path

class Config:
    def __init__(self):
        self.BASE_DIR = Path(__file__).parent.parent
        self.SAVE_DIR = self.BASE_DIR / "saves"
        self.DATA_DIR = self.BASE_DIR / "data"
        
        # Создаем необходимые директории
        self.SAVE_DIR.mkdir(exist_ok=True)
        (self.SAVE_DIR / "characters").mkdir(exist_ok=True)
        (self.SAVE_DIR / "locations").mkdir(exist_ok=True)
        (self.SAVE_DIR / "items").mkdir(exist_ok=True)
        (self.SAVE_DIR / "dialogs").mkdir(exist_ok=True)
        (self.SAVE_DIR / "maps").mkdir(exist_ok=True)
        
        self.TOKEN = "8206494085:AAFhoXfLaSgfEPMF4u8GrtAyTf-J-l7VRxs"
        self.DEBUG_MODE = True
        self.MAP_WIDTH = 50
        self.MAP_HEIGHT = 30
        self.TILE_SIZE = 20