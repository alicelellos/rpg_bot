import random
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import math

class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()
    HERMAPHRODITE = auto()

class SocialClass(Enum):
    NOBLE = auto()
    MERCHANT = auto()
    ARTISAN = auto()
    PEASANT = auto()
    SLAVE = auto()
    OUTCAST = auto()
    CLERIC = auto()
    MILITARY = auto()

class PersonalityTrait(Enum):
    BRAVE = auto()
    COWARD = auto()
    GENEROUS = auto()
    GREEDY = auto()
    COMPASSIONATE = auto()
    CRUEL = auto()
    HONEST = auto()
    DECEITFUL = auto()
    AMBITIOUS = auto()
    CONTENT = auto()

@dataclass
class BodyPartState:
    hp: int
    max_hp: int
    bleeding: bool = False
    fractures: int = 0
    burns: int = 0
    dirtiness: float = 0.0  # 0-1 scale
    wetness: float = 0.0  # 0-1 scale
    covered: bool = False
    temperature: float = 37.0  # Celsius
    wounds: List['Wound'] = None
    subparts: Dict[str, 'BodyPartState'] = None

    def __post_init__(self):
        self.wounds = []
        if self.subparts is None:
            self.subparts = {}

class Wound:
    WOUND_TYPES = {
        'cut': ["Неглубокий порез", "Рваная рана", "Глубокий разрез"],
        'stab': ["Колотая рана", "Проникающее ранение", "Прокол"],
        'blunt': ["Ушиб", "Гематома", "Внутреннее кровотечение"],
        'burn': ["Лёгкий ожог", "Волдыри", "Обугленная плоть"],
        'frostbite': ["Обморожение", "Отмороженные ткани", "Некроз от холода"]
    }

    SEVERITY_LEVELS = [
        "лёгкое", "умеренное", "серьёзное", 
        "тяжёлое", "критическое", "смертельное"
    ]

    def __init__(self, wound_type: str, severity: int, body_part: str):
        self.wound_type = wound_type
        self.severity = min(max(severity, 1), 6)
        self.body_part = body_part
        self.time_healing = 0
        self.healed = False
        self.scar_chance = 0.1 * severity
        self.description = self._generate_description()

    def _generate_description(self) -> str:
        wound_desc = random.choice(self.WOUND_TYPES.get(self.wound_type, ["Травма"]))
        severity_desc = self.SEVERITY_LEVELS[self.severity - 1]
        return f"{severity_desc} {wound_desc} на {self.body_part}"

    def update_healing(self, medical_skill: int) -> bool:
        """Обновляет состояние раны, возвращает True если зажила"""
        heal_rate = 0.1 + (medical_skill * 0.05)
        self.time_healing += heal_rate
        
        if self.time_healing >= self.severity:
            self.healed = True
            return True
        return False

class Character:
    BODY_STRUCTURE = {
        'head': {
            'max_hp': 50,
            'critical': True,
            'subparts': {
                'left_eye': {'max_hp': 15},
                'right_eye': {'max_hp': 15},
                'nose': {'max_hp': 20},
                'mouth': {'max_hp': 25},
                'left_ear': {'max_hp': 10},
                'right_ear': {'max_hp': 10},
                'jaw': {'max_hp': 30}
            }
        },
        'torso': {
            'max_hp': 100,
            'critical': True,
            'subparts': {
                'heart': {'max_hp': 40, 'critical': True},
                'left_lung': {'max_hp': 30},
                'right_lung': {'max_hp': 30},
                'stomach': {'max_hp': 35},
                'liver': {'max_hp': 25}
            }
        },
        'left_arm': {'max_hp': 60},
        'right_arm': {'max_hp': 60},
        'left_leg': {'max_hp': 70},
        'right_leg': {'max_hp': 70},
        'groin': {
            'max_hp': 40,
            'subparts': {
                'genitals': {'max_hp': 20}
            }
        }
    }

    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender
        self.age = self._generate_age()
        self.height = self._generate_height()
        self.weight = self._generate_weight()
        self.body = self._init_body()
        self.stats = self._init_stats()
        self.skills = self._init_skills()
        self.traits = self._init_traits()
        self.equipment = {}
        self.inventory = []
        self.social_class = self._generate_social_class()
        self.hygiene = 1.0  # 0-1 scale
        self.temperature = 37.0  # body temp
        self.mood = "neutral"
        self.fears = []
        self.likes = []
        self.dislikes = []
        self.relationships = {}
        self.appearance = self._generate_appearance()
        self.voice = self._generate_voice()
        self.health_status = "healthy"
        self.alive = True
        self.karma = 0  # -100 to 100 scale

    def _generate_age(self) -> int:
        if self.social_class == SocialClass.NOBLE:
            return random.randint(16, 70)
        elif self.social_class == SocialClass.PEASANT:
            return random.randint(12, 60)
        return random.randint(15, 65)

    def _generate_height(self) -> float:
        if self.gender == Gender.MALE:
            base = random.uniform(160, 190)
        else:
            base = random.uniform(150, 180)
        
        # Adjust for social class (better nutrition)
        if self.social_class in [SocialClass.NOBLE, SocialClass.MERCHANT]:
            base += random.uniform(0, 10)
        elif self.social_class == SocialClass.PEASANT:
            base -= random.uniform(0, 5)
        
        return round(base, 1)

    def _generate_weight(self) -> float:
        bmi = random.uniform(18, 30)
        height_m = self.height / 100
        return round(bmi * (height_m ** 2), 1)

    def _init_body(self) -> Dict[str, BodyPartState]:
        """Инициализирует все части тела с их состояниями"""
        body = {}
        
        for part_name, part_data in self.BODY_STRUCTURE.items():
            subparts = {}
            if 'subparts' in part_data:
                for sub_name, sub_data in part_data['subparts'].items():
                    subparts[sub_name] = BodyPartState(
                        hp=sub_data['max_hp'],
                        max_hp=sub_data['max_hp']
                    )
            
            body[part_name] = BodyPartState(
                hp=part_data['max_hp'],
                max_hp=part_data['max_hp'],
                subparts=subparts
            )
        
        return body

    def _init_stats(self) -> Dict[str, int]:
        """Инициализирует базовые характеристики"""
        stats = {
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'wisdom': random.randint(3, 18),
            'charisma': random.randint(3, 18),
            'perception': random.randint(3, 18)
        }
        
        # Apply gender modifiers
        if self.gender == Gender.MALE:
            stats['strength'] += random.randint(0, 2)
            stats['endurance'] += random.randint(0, 2)
        elif self.gender == Gender.FEMALE:
            stats['agility'] += random.randint(0, 2)
            stats['perception'] += random.randint(0, 2)
        
        # Apply social class modifiers
        if self.social_class == SocialClass.NOBLE:
            stats['charisma'] += random.randint(1, 3)
        elif self.social_class == SocialClass.MILITARY:
            stats['strength'] += random.randint(1, 3)
            stats['endurance'] += random.randint(1, 3)
        elif self.social_class == SocialClass.CLERIC:
            stats['wisdom'] += random.randint(1, 3)
        
        return stats

    def _init_skills(self) -> Dict[str, int]:
        """Инициализирует навыки персонажа"""
        skills = {
            'swords': random.randint(1, 10),
            'axes': random.randint(1, 10),
            'bows': random.randint(1, 10),
            'unarmed': random.randint(1, 10),
            'medicine': random.randint(1, 10),
            'stealth': random.randint(1, 10),
            'persuasion': random.randint(1, 10),
            'intimidation': random.randint(1, 10),
            'survival': random.randint(1, 10),
            'crafting': random.randint(1, 10)
        }
        
        # Apply social class modifiers
        if self.social_class == SocialClass.MILITARY:
            for weapon_skill in ['swords', 'axes', 'bows']:
                skills[weapon_skill] += random.randint(1, 3)
        elif self.social_class == SocialClass.ARTISAN:
            skills['crafting'] += random.randint(2, 5)
        elif self.social_class == SocialClass.CLERIC:
            skills['medicine'] += random.randint(2, 5)
            skills['persuasion'] += random.randint(1, 3)
        
        return skills

    def _init_traits(self) -> List[PersonalityTrait]:
        """Генерирует черты характера"""
        traits = []
        trait_pool = list(PersonalityTrait)
        
        # Base traits based on social class
        if self.social_class == SocialClass.NOBLE:
            traits.extend([PersonalityTrait.AMBITIOUS, PersonalityTrait.DECEITFUL])
        elif self.social_class == SocialClass.PEASANT:
            traits.extend([PersonalityTrait.CONTENT, PersonalityTrait.HONEST])
        elif self.social_class == SocialClass.MILITARY:
            traits.extend([PersonalityTrait.BRAVE, PersonalityTrait.CRUEL])
        
        # Add random traits
        while len(traits) < 4 and trait_pool:
            new_trait = random.choice(trait_pool)
            if new_trait not in traits:
                traits.append(new_trait)
                trait_pool.remove(new_trait)
        
        return traits

    def _generate_social_class(self) -> SocialClass:
        """Генерирует социальный класс"""
        weights = {
            SocialClass.NOBLE: 0.05,
            SocialClass.MERCHANT: 0.1,
            SocialClass.ARTISAN: 0.15,
            SocialClass.PEASANT: 0.5,
            SocialClass.SLAVE: 0.1,
            SocialClass.OUTCAST: 0.05,
            SocialClass.CLERIC: 0.03,
            SocialClass.MILITARY: 0.02
        }
        return random.choices(list(weights.keys()), weights=list(weights.values()))[0]

    def _generate_appearance(self) -> Dict[str, str]:
        """Генерирует внешность персонажа"""
        appearance = {
            'hair_color': random.choice(["чёрный", "каштановый", "русый", "рыжий", "белый", "седой"]),
            'eye_color': random.choice(["карий", "голубой", "зелёный", "серый", "янтарный"]),
            'skin_tone': random.choice(["бледный", "светлый", "смуглый", "оливковый", "тёмный"]),
            'hair_length': random.choice(["короткие", "средней длины", "длинные"]),
            'hair_style': random.choice(["прямые", "волнистые", "кудрявые"]),
            'facial_hair': self._generate_facial_hair(),
            'body_type': self._generate_body_type(),
            'distinctive_features': self._generate_distinctive_features()
        }
        return appearance

    def _generate_facial_hair(self) -> str:
        """Генерирует растительность на лице"""
        if self.gender != Gender.MALE:
            return "нет"
        
        options = [
            "нет", "редкая щетина", "густая щетина", 
            "усы", "борода", "длинная борода"
        ]
        weights = [0.2, 0.3, 0.2, 0.15, 0.1, 0.05]
        return random.choices(options, weights=weights)[0]

    def _generate_body_type(self) -> str:
        """Генерирует тип телосложения"""
        bmi = self.weight / ((self.height/100) ** 2)
        
        if bmi < 18.5:
            return "худощавое"
        elif bmi < 25:
            return "атлетическое" if random.random() < 0.3 else "нормальное"
        elif bmi < 30:
            return "полное" if random.random() < 0.5 else "мускулистое"
        else:
            return "тучное"

    def _generate_distinctive_features(self) -> List[str]:
        """Генерирует отличительные черты внешности"""
        features = []
        feature_pool = [
            "шрам на лице", "родинка на щеке", "сломанный нос",
            "отсутствие зуба", "татуировка", "пирсинг",
            "разные глаза", "горб", "хромота"
        ]
        
        while len(features) < 2 and random.random() < 0.5:
            feature = random.choice(feature_pool)
            if feature not in features:
                features.append(feature)
        
        return features

    def _generate_voice(self) -> Dict[str, str]:
        """Генерирует характеристики голоса"""
        if self.gender == Gender.MALE:
            pitch = random.choice(["низкий", "грубый", "глубокий", "хриплый"])
        elif self.gender == Gender.FEMALE:
            pitch = random.choice(["высокий", "мягкий", "мелодичный"])
        else:
            pitch = random.choice(["нейтральный", "андрогинный"])
        
        return {
            'pitch': pitch,
            'clarity': random.choice(["чёткая", "невнятная", "картавая"]),
            'volume': random.choice(["тихий", "нормальный", "громкий"])
        }

    def calculate_total_hp(self) -> Tuple[int, int]:
        """Вычисляет текущее и максимальное HP"""
        total_hp = 0
        total_max_hp = 0
        
        for part in self.body.values():
            total_hp += part.hp
            total_max_hp += part.max_hp
            
            for subpart in part.subparts.values():
                total_hp += subpart.hp
                total_max_hp += subpart.max_hp
        
        return total_hp, total_max_hp

    def update_health_status(self):
        """Обновляет общий статус здоровья"""
        total_hp, max_hp = self.calculate_total_hp()
        hp_percent = total_hp / max_hp
        
        if hp_percent > 0.9:
            self.health_status = "здоров"
        elif hp_percent > 0.7:
            self.health_status = "лёгкие повреждения"
        elif hp_percent > 0.5:
            self.health_status = "ранен"
        elif hp_percent > 0.3:
            self.health_status = "тяжело ранен"
        elif hp_percent > 0.1:
            self.health_status = "при смерти"
        else:
            self.health_status = "мёртв"
            self.alive = False

    def take_damage(self, damage: int, damage_type: str, body_part: str) -> str:
        """Наносит урон указанной части тела"""
        if not self.alive:
            return "Персонаж уже мёртв"
        
        part = self.body.get(body_part)
        if part is None:
            return "Неверная часть тела"
        
        # Apply armor reduction
        equipped_armor = self.equipment.get('armor')
        if equipped_armor and body_part in equipped_armor.coverage:
            damage = max(1, damage - equipped_armor.protection)
        
        # Apply damage
        part.hp = max(0, part.hp - damage)
        
        # Create wound
        wound = Wound(
            wound_type=damage_type,
            severity=min(math.ceil(damage / 5), 6),
            body_part=body_part
        )
        part.wounds.append(wound)
        
        # Check for critical damage
        result_msg = f"{self.name} получает {damage} урона по {body_part}. {wound.description}"
        
        if part.hp <= 0 and part.critical:
            result_msg += f"\nКРИТИЧЕСКОЕ ПОРАЖЕНИЕ! {self.name} теряет сознание от боли!"
            self.health_status = "без сознания"
        
        self.update_health_status()
        return result_msg

    def heal(self, amount: int, body_part: str = None) -> str:
        """Лечит указанную часть тела или всё тело"""
        if not self.alive:
            return "Нельзя лечить мёртвого"
        
        if body_part:
            part = self.body.get(body_part)
            if part:
                part.hp = min(part.max_hp, part.hp + amount)
                self.update_health_status()
                return f"{self.name} восстановил {amount} HP на {body_part}"
            return "Неверная часть тела"
        else:
            healed_amount = 0
            for part in self.body.values():
                initial_hp = part.hp
                part.hp = min(part.max_hp, part.hp + amount)
                healed_amount += (part.hp - initial_hp)
            
            self.update_health_status()
            return f"{self.name} восстановил {healed_amount} HP в целом"

    def update_wounds(self, medical_skill: int = 0) -> List[str]:
        """Обновляет состояние всех ран, возвращает сообщения о заживших"""
        messages = []
        
        for part_name, part in self.body.items():
            healed_wounds = []
            
            for wound in part.wounds:
                if wound.update_healing(medical_skill):
                    healed_wounds.append(wound)
                    
                    # Chance to leave a scar
                    if random.random() < wound.scar_chance:
                        scar_desc = f"шрам от {wound.description.lower()}"
                        if scar_desc not in self.appearance['distinctive_features']:
                            self.appearance['distinctive_features'].append(scar_desc)
                            messages.append(f"На {part_name} {self.name} остался {scar_desc}")
            
            # Remove healed wounds
            for wound in healed_wounds:
                part.wounds.remove(wound)
        
        return messages

    def equip_item(self, item: 'Item') -> str:
        """Надевает предмет экипировки"""
        if not isinstance(item, (Weapon, Armor, Clothing)):
            return "Нельзя надеть этот предмет"
        
        slot = item.slot if hasattr(item, 'slot') else 'weapon'
        
        # Check if slot is already occupied
        if slot in self.equipment:
            return f"Слот {slot} уже занят"
        
        self.equipment[slot] = item
        return f"{self.name} надевает {item.name}"

    def unequip_item(self, slot: str) -> str:
        """Снимает предмет экипировки"""
        if slot not in self.equipment:
            return f"В слоте {slot} ничего нет"
        
        item = self.equipment.pop(slot)
        return f"{self.name} снимает {item.name}"

    def add_to_inventory(self, item: 'Item') -> bool:
        """Добавляет предмет в инвентарь"""
        current_weight = sum(i.weight for i in self.inventory)
        if current_weight + item.weight > self.carry_capacity:
            return False
        
        self.inventory.append(item)
        return True

    @property
    def carry_capacity(self) -> float:
        """Вычисляет грузоподъёмность персонажа"""
        base = self.stats['strength'] * 2
        endurance_bonus = self.stats['endurance'] * 0.5
        
        # Trait modifiers
        if PersonalityTrait.STRONG in self.traits:
            base += 5
        if PersonalityTrait.WEAK in self.traits:
            base -= 3
        
        return base + endurance_bonus

    def get_full_description(self) -> str:
        """Возвращает полное описание персонажа"""
        desc = f"{self.name} - {self.gender.name.lower()}, {self.age} лет\n"
        desc += f"Социальный класс: {self.social_class.name.lower()}\n"
        desc += f"Рост: {self.height} см, Вес: {self.weight} кг\n"
        desc += f"Телосложение: {self.appearance['body_type']}\n"
        desc += f"Волосы: {self.appearance['hair_length']} {self.appearance['hair_style']} {self.appearance['hair_color']}\n"
        desc += f"Глаза: {self.appearance['eye_color']}, Кожа: {self.appearance['skin_tone']}\n"
        
        if self.appearance['facial_hair'] != "нет":
            desc += f"Растительность на лице: {self.appearance['facial_hair']}\n"
        
        if self.appearance['distinctive_features']:
            desc += "Отличительные черты: " + ", ".join(self.appearance['distinctive_features']) + "\n"
        
        desc += f"\nХарактеристики:\n"
        for stat, value in self.stats.items():
            desc += f"- {stat}: {value}\n"
        
        desc += f"\nЧерты характера: {', '.join(t.name.lower() for t in self.traits)}\n"
        desc += f"Состояние здоровья: {self.health_status}\n"
        
        total_hp, max_hp = self.calculate_total_hp()
        desc += f"HP: {total_hp}/{max_hp}\n"
        
        if self.equipment:
            desc += f"\nЭкипировка:\n"
            for slot, item in self.equipment.items():
                desc += f"- {slot}: {item.name} (прочность: {item.durability}%)\n"
        
        return desc
