import random
from enum import Enum, auto
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, field
import math
import time

# ========================
# Базовые перечисления и классы
# ========================

class DamageType(Enum):
    """Типы урона в системе"""
    SLASHING = auto()      # Режущий
    PIERCING = auto()      # Колющий
    BLUNT = auto()         # Дробящий
    FIRE = auto()          # Огонь
    COLD = auto()          # Холод
    ACID = auto()          # Кислота
    POISON = auto()        # Яд
    ELECTRIC = auto()      # Электрический
    PSYCHIC = auto()       # Психический
    HOLY = auto()          # Святой
    DARK = auto()          # Тёмный
    BLEEDING = auto()      # Кровотечение
    INTERNAL = auto()      # Внутренние повреждения
    FATIGUE = auto()       # Усталость
    DISEASE = auto()       # Болезнь
    SONIC = auto()         # Звуковой
    RADIANT = auto()       # Излучение
    NECROTIC = auto()      # Некротический
    FORCE = auto()         # Силовой
    ARCANE = auto()        # Тайная магия

class SocialClass(Enum):
    """Социальные классы персонажей"""
    SLAVE = auto()         # Раб
    PEASANT = auto()       # Крестьянин
    COMMONER = auto()      # Горожанин
    MERCHANT = auto()      # Купец
    ARTISAN = auto()       # Ремесленник
    NOBLE = auto()         # Дворянин
    ROYALTY = auto()       # Королевская семья
    CLERGY = auto()        # Духовенство
    OUTCAST = auto()       # Изгой
    CRIMINAL = auto()      # Преступник
    SCHOLAR = auto()       # Учёный
    SOLDIER = auto()       # Солдат
    ADVENTURER = auto()    # Искатель приключений
    HERMIT = auto()        # Отшельник
    ENTERTAINER = auto()   # Артист

class MaterialType(Enum):
    """Типы материалов для брони и оружия"""
    # Металлы
    IRON = auto()          # Железо
    STEEL = auto()         # Сталь
    BRONZE = auto()        # Бронза
    SILVER = auto()        # Серебро
    GOLD = auto()          # Золото
    MITHRIL = auto()       # Мифрил
    ADAMANTINE = auto()    # Адамантин
    DARKSTEEL = auto()     # Тёмная сталь
    ORICHALCUM = auto()    # Орихалк
    TITANIUM = auto()      # Титан
    COPPER = auto()        # Медь
    # Органические
    LEATHER = auto()       # Кожа
    HARDENED_LEATHER = auto() # Укреплённая кожа
    BONE = auto()          # Кость
    SCALE = auto()         # Чешуя
    CHITIN = auto()        # Хитин
    DRAGONHIDE = auto()    # Драконья шкура
    # Ткани
    LINEN = auto()         # Лён
    WOOL = auto()          # Шерсть
    SILK = auto()          # Шёлк
    COTTON = auto()        # Хлопок
    VELVET = auto()        # Бархат
    # Дерево
    OAK = auto()           # Дуб
    MAPLE = auto()         # Клён
    EBONY = auto()         # Эбеновое
    YEW = auto()           # Тис
    MAHOGANY = auto()      # Красное дерево
    # Камень
    STONE = auto()         # Камень
    OBSIDIAN = auto()      # Обсидиан
    MARBLE = auto()        # Мрамор
    # Другое
    GLASS = auto()         # Стекло
    CRYSTAL = auto()       # Кристалл
    ENCHANTED = auto()     # Зачарованный материал
    LIVING = auto()        # Живая материя

class BodyPart(Enum):
    """Части тела с детализацией"""
    # Голова
    HEAD = auto()          # Голова
    SKULL = auto()         # Череп
    BRAIN = auto()         # Мозг
    FACE = auto()          # Лицо
    FOREHEAD = auto()      # Лоб
    EYES = auto()          # Глаза
    NOSE = auto()          # Нос
    MOUTH = auto()         # Рот
    LIPS = auto()          # Губы
    TEETH = auto()         # Зубы
    TONGUE = auto()        # Язык
    EARS = auto()          # Уши
    CHEEKS = auto()        # Щёки
    JAW = auto()           # Челюсть
    # Шея
    NECK = auto()          # Шея
    THROAT = auto()        # Горло
    # Туловище
    CHEST = auto()         # Грудь
    RIBS = auto()          # Рёбра
    HEART = auto()         # Сердце
    LUNGS = auto()         # Лёгкие
    STOMACH = auto()       # Желудок
    LIVER = auto()         # Печень
    KIDNEYS = auto()       # Почки
    INTESTINES = auto()    # Кишки
    SPINE = auto()         # Позвоночник
    BACK = auto()          # Спина
    # Руки
    SHOULDERS = auto()     # Плечи
    UPPER_ARM = auto()     # Плечо (верх)
    ELBOW = auto()         # Локоть
    LOWER_ARM = auto()     # Предплечье
    WRIST = auto()         # Запястье
    HAND = auto()          # Кисть
    PALM = auto()          # Ладонь
    FINGERS = auto()       # Пальцы (все)
    THUMB = auto()         # Большой палец
    INDEX = auto()         # Указательный
    MIDDLE = auto()        # Средний
    RING = auto()          # Безымянный
    LITTLE = auto()        # Мизинец
    # Ноги
    HIPS = auto()          # Бёдра
    GROIN = auto()         # Пах
    GENITALS = auto()      # Гениталии
    THIGH = auto()         # Бедро
    KNEE = auto()          # Колено
    CALF = auto()          # Икра
    ANKLE = auto()         # Лодыжка
    FOOT = auto()          # Стопа
    TOES = auto()          # Пальцы ног
    BIG_TOE = auto()       # Большой палец ноги
    # Другое
    NAILS = auto()         # Ногти
    HAIR = auto()          # Волосы
    SKIN = auto()          # Кожа
    BLOOD_VESSELS = auto() # Кровеносные сосуды
    MUSCLES = auto()       # Мышцы
    TENDONS = auto()       # Сухожилия
    NERVES = auto()        # Нервы

class WoundSeverity(Enum):
    """Уровень тяжести ранения"""
    SCRATCH = auto()       # Царапина
    MINOR = auto()         # Лёгкое
    MODERATE = auto()      # Среднее
    SEVERE = auto()        # Тяжёлое
    CRITICAL = auto()      # Критическое
    FATAL = auto()         # Смертельное
    MAIMING = auto()       # Калечащее
    DISFIGURING = auto()   # Обезображивающее

class PainLevel(Enum):
    """Уровень боли"""
    NONE = auto()          # Нет
    MILD = auto()          # Слабая
    MODERATE = auto()      # Умеренная
    SEVERE = auto()        # Сильная
    EXCRUCIATING = auto()  # Невыносимая
    PARALYZING = auto()    # Парализующая

class AttackStyle(Enum):
    """Стили атаки"""
    AGGRESSIVE = auto()    # Агрессивный
    DEFENSIVE = auto()     # Защитный
    BALANCED = auto()      # Сбалансированный
    PRECISE = auto()       # Точный
    BRUTAL = auto()        # Жестокий
    FENCING = auto()       # Фехтовальный
    BERSERK = auto()       # Берсерк
    DEXTEROUS = auto()     # Ловкий
    SAVAGE = auto()        # Дикий
    TECHNICAL = auto()     # Техничный
    FLUID = auto()         # Плавный
    UNPREDICTABLE = auto() # Непредсказуемый

class PersonalityTrait(Enum):
    """Черты личности"""
    BRAVE = auto()         # Храбрый
    COWARD = auto()        # Трусливый
    AGGRESSIVE = auto()    # Агрессивный
    CALM = auto()          # Спокойный
    COMPASSIONATE = auto() # Сострадательный
    CRUEL = auto()         # Жестокий
    HONEST = auto()        # Честный
    DECEITFUL = auto()     # Лживый
    GENEROUS = auto()      # Щедрый
    GREEDY = auto()        # Жадный
    MASOCHIST = auto()     # Мазохист
    SADIST = auto()        # Садист
    NYMPHOMANIAC = auto()  # Нимфоманка/Сатир
    PERVERT = auto()       # Извращенец
    NAIVE = auto()         # Наивный
    CUNNING = auto()       # Хитрый
    LOYAL = auto()         # Верный
    TREACHEROUS = auto()   # Предательский
    LAZY = auto()          # Ленивый
    HARDWORKING = auto()   # Трудолюбивый
    OPTIMISTIC = auto()    # Оптимистичный
    PESSIMISTIC = auto()   # Пессимистичный
    ROMANTIC = auto()      # Романтичный
    CYNICAL = auto()       # Циничный
    HUMOROUS = auto()      # Юмористичный
    SERIOUS = auto()       # Серьёзный
    CURIOUS = auto()       # Любопытный
    INDIFFERENT = auto()   # Равнодушный
    AMBITIOUS = auto()     # Амбициозный
    CONTENT = auto()       # Довольствующийся малым

# ========================
# Классы данных
# ========================

@dataclass
class Wound:
    """Класс ранения"""
    body_part: BodyPart
    severity: WoundSeverity
    damage_type: DamageType
    pain_level: PainLevel
    bleeding: bool
    description: str
    treated: bool = False
    time_occurred: float = field(default_factory=time.time)
    is_scar: bool = False

    def get_pain_value(self) -> int:
        """Возвращает числовое значение боли для расчетов"""
        pain_values = {
            PainLevel.NONE: 0,
            PainLevel.MILD: 1,
            PainLevel.MODERATE: 3,
            PainLevel.SEVERE: 6,
            PainLevel.EXCRUCIATING: 10,
            PainLevel.PARALYZING: 15
        }
        return pain_values[self.pain_level]

    def get_severity_value(self) -> int:
        """Возвращает числовое значение тяжести ранения"""
        severity_values = {
            WoundSeverity.SCRATCH: 1,
            WoundSeverity.MINOR: 2,
            WoundSeverity.MODERATE: 4,
            WoundSeverity.SEVERE: 7,
            WoundSeverity.CRITICAL: 12,
            WoundSeverity.FATAL: 20,
            WoundSeverity.MAIMING: 15,
            WoundSeverity.DISFIGURING: 10
        }
        return severity_values[self.severity]

@dataclass
class CharacterStats:
    """Характеристики персонажа"""
    strength: int = 10      # Сила
    agility: int = 10       # Ловкость
    endurance: int = 10     # Выносливость
    perception: int = 10    # Восприятие
    intelligence: int = 10  # Интеллект
    willpower: int = 10     # Сила воли
    charisma: int = 10      # Харизма
    luck: int = 10          # Удача
    dexterity: int = 10     # Ловкость рук
    constitution: int = 10  # Телосложение

@dataclass
class CharacterState:
    """Состояние персонажа в бою"""
    health: float = 100.0
    stamina: float = 100.0
    fatigue: float = 0.0
    pain: float = 0.0
    blood_loss: float = 0.0
    wounds: List[Wound] = field(default_factory=list)
    active_effects: List[str] = field(default_factory=list)
    equipped_weapon: Optional['Weapon'] = None
    armor: Dict[BodyPart, Optional['Armor']] = field(default_factory=dict)
    stance: AttackStyle = AttackStyle.BALANCED
    morale: float = 50.0  # Боевой дух от 0 до 100
    adrenaline: float = 0.0 # Уровень адреналина
    focus: float = 50.0    # Концентрация

@dataclass
class Weapon:
    """Класс оружия"""
    name: str
    damage_types: List[DamageType]
    base_damage: float
    material: MaterialType
    weight: float
    attack_speed: float
    reach: float
    durability: float
    max_durability: float
    description: str
    handedness: int = 1  # 1 - одноручное, 2 - двуручное
    quality: float = 1.0 # Качество изготовления (0.5-1.5)

@dataclass
class Armor:
    """Класс брони"""
    name: str
    covered_parts: List[BodyPart]
    defense: Dict[DamageType, float]
    material: MaterialType
    weight: float
    durability: float
    max_durability: float
    description: str
    coverage: float = 0.8  # Покрытие части тела (0-1)
    flexibility: float = 0.5 # Гибкость (0-1)

# ========================
# Генераторы описаний
# ========================

class DescriptionGenerator:
    """Генератор описаний для различных аспектов боя"""
    
    @staticmethod
    def generate_wound_description(wound: Wound) -> str:
        """Генерация художественного описания раны"""
        part_descriptions = {
            BodyPart.HEAD: ["головы", "черепа", "лица", "макушки"],
            BodyPart.FACE: ["лица", "физиономии", "морды", "обличья"],
            BodyPart.EYES: ["глаза", "ока", "зеницы ока", "глазного яблока"],
            BodyPart.NOSE: ["носа", "носовой перегородки", "переносицы", "ноздри"],
            BodyPart.MOUTH: ["рта", "губ", "ротовой полости", "челюсти"],
            BodyPart.NECK: ["шеи", "горла", "шейных позвонков", "кадыка"],
            BodyPart.CHEST: ["груди", "грудной клетки", "рёбер", "сердца"],
            BodyPart.STOMACH: ["живота", "брюшной полости", "пупа", "кишечника"],
            BodyPart.ARMS: ["руки", "конечности", "длани", "предплечья"],
            BodyPart.HANDS: ["кисти", "ладони", "пальцев", "запястья"],
            BodyPart.LEGS: ["ноги", "конечности", "бедра", "голени"],
            BodyPart.FEET: ["стопы", "ступни", "пятки", "лодыжки"],
            BodyPart.GENITALS: ["паха", "гениталий", "интимных мест", "достоинства"]
        }
        
        severity_descriptions = {
            WoundSeverity.SCRATCH: [
                "Незначительная царапина",
                "Лёгкое повреждение",
                "Поверхностная рана",
                "Едва заметный след"
            ],
            WoundSeverity.MINOR: [
                "Кровавая ссадина",
                "Неглубокий порез",
                "Лёгкое рассечение",
                "Заметная царапина"
            ],
            WoundSeverity.MODERATE: [
                "Кровоточащая рана",
                "Глубокий порез",
                "Серьёзное повреждение",
                "Зияющая рана"
            ],
            WoundSeverity.SEVERE: [
                "Глубокое зияющее ранение",
                "Ужасная рваная рана",
                "Кровоточащая трещина",
                "Разрушительное повреждение"
            ],
            WoundSeverity.CRITICAL: [
                "Критическое ранение",
                "Калечащая травма",
                "Ужасающее повреждение",
                "Разрушение тканей"
            ],
            WoundSeverity.FATAL: [
                "Смертоносная рана",
                "Несовместимое с жизнью повреждение",
                "Фатальное разрушение",
                "Кончающая травма"
            ]
        }
        
        damage_descriptions = {
            DamageType.SLASHING: [
                "режущего",
                "рубящего",
                "острого",
                "рассекающего"
            ],
            DamageType.PIERCING: [
                "колющего",
                "проникающего",
                "пробивающего",
                "прокола"
            ],
            DamageType.BLUNT: [
                "дробящего",
                "тупого",
                "раздавливающего",
                "сокрушительного"
            ],
            DamageType.FIRE: [
                "огненного",
                "обжигающего",
                "пылающего",
                "выжигающего"
            ],
            DamageType.COLD: [
                "ледяного",
                "замораживающего",
                "пронизывающего холода",
                "обморожения"
            ],
            DamageType.ACID: [
                "разъедающего",
                "кислотного",
                "коррозийного",
                "едкого"
            ],
            DamageType.POISON: [
                "ядовитого",
                "токсичного",
                "отравляющего",
                "яда"
            ],
            DamageType.ELECTRIC: [
                "электрического",
                "молниеносного",
                "разряда",
                "электрошока"
            ],
            DamageType.PSYCHIC: [
                "психического",
                "ментального",
                "разума",
                "сознания"
            ]
        }
        
        pain_descriptions = {
            PainLevel.MILD: [
                "слабо ноет",
                "покалывает",
                "слегка беспокоит",
                "чувствуется дискомфорт"
            ],
            PainLevel.MODERATE: [
                "пульсирует болью",
                "ноет",
                "причиняет страдания",
                "дёргает"
            ],
            PainLevel.SEVERE: [
                "пронзает острой болью",
                "невыносимо болит",
                "пульсирует мучительной болью",
                "сводит от боли"
            ],
            PainLevel.EXCRUCIATING: [
                "испепеляет невыносимой болью",
                "парализует агонией",
                "разрывает на части от боли",
                "заставляет кричать от мучений"
            ]
        }
        
        part = random.choice(part_descriptions.get(wound.body_part, ["тела", "плоти", "кожи", "тканей"]))
        severity = random.choice(severity_descriptions.get(wound.severity, ["рана", "повреждение", "травма", "увечье"]))
        damage = random.choice(damage_descriptions.get(wound.damage_type, ["", "неизвестного", "странного", "загадочного"]))
        pain = random.choice(pain_descriptions.get(wound.pain_level, ["", "беспокоит", "причиняет дискомфорт", "ощущается"]))
        
        bleeding_text = ", кровь хлещет ручьём" if wound.bleeding else ""
        pain_text = f", {pain}" if wound.pain_level != PainLevel.NONE else ""
        
        descriptions = [
            f"{severity} от {damage} воздействия на {part}{bleeding_text}{pain_text}",
            f"На {part} видно {severity.lower()} от {damage} удара{bleeding_text}{pain_text}",
            f"Последствие {damage} воздействия — {severity.lower()} на {part}{bleeding_text}{pain_text}",
            f"Жуткая картина: {severity.lower()} на {part} от {damage} повреждения{bleeding_text}{pain_text}"
        ]
        
        return random.choice(descriptions)

    @staticmethod
    def generate_attack_description(attacker: str, target: str, weapon: Optional[Weapon], 
                                  damage: float, critical: bool) -> str:
        """Генерация художественного описания атаки"""
        if weapon is None:
            attack_verbs = [
                "наносит удар кулаком", "бьёт со всей силы", "вмазывает кулачищем",
                "врезает со злостью", "ударяет сокрушительно", "впечатывает кулак",
                "прикладывает по полной", "вмазывает со свистом"
            ]
            weapon_desc = ["кулаком", "голыми руками", "рукой", "дланью", "крепкой пятернёй"]
        else:
            attack_verbs = {
                DamageType.SLASHING: [
                    "рассекает", "рубит с размаху", "вспарывает", "наносит режущий удар",
                    "проводит молниеносный удар", "разрезает воздух", "наносит рубящий удар",
                    "взмахивает со свистом"
                ],
                DamageType.PIERCING: [
                    "прокалывает", "вонзает оружие", "протыкает", "наносит колющий удар",
                    "впускает лезвие", "пробивает защиту", "втыкает остриё", "пронзает"
                ],
                DamageType.BLUNT: [
                    "оглушает ударом", "молотит со страшной силой", "вдалбливает", 
                    "наносит сокрушительный удар", "впечатывает оружие", "бьёт с размаху",
                    "размахивается и бьёт", "обрушивает всю мощь"
                ],
                DamageType.FIRE: [
                    "выжигает", "опаляет", "поджаривает", "наносит обжигающий удар",
                    "вспыхивает пламенем", "обрушивает огненную атаку", "испепеляет",
                    "покрывает ожогами"
                ],
                DamageType.COLD: [
                    "промораживает", "покрывает инеем", "пронзает ледяным холодом",
                    "наносит обмораживающий удар", "впускает холод в плоть", 
                    "замораживает до костей", "вызывает обморожение", "леденит"
                ],
                DamageType.ELECTRIC: [
                    "поражает разрядом", "бьёт током", "пронзает молнией",
                    "накачивает электричеством", "искрит от удара", "вызывает конвульсии",
                    "парализует разрядом", "поджаривает током"
                ]
            }
            weapon_desc = [weapon.name.lower(), "своим оружием", "стальным лезвием", 
                          "смертоносным инструментом", f"{weapon.material.name.lower()} {weapon.name.lower()}"]
        
        verb = random.choice(attack_verbs.get(weapon.damage_types[0] if weapon else DamageType.BLUNT, ["атакует", "наносит удар"]))
        weapon_text = random.choice(weapon_desc)
        
        crit_texts = [
            " Сокрушительный удар!", " Критический урон!", " Смертоносная точность!",
            " Удар в самое уязвимое место!", " Идеальное попадание!", 
            " Удар, от которого звенит в ушах!", " Апперкот судьбы!"
        ] if critical else ""
        
        damage_texts = [
            f"нанося {damage:.1f} урона",
            f"причиняя {damage:.1f} единиц боли",
            f"оставляя повреждения на {damage:.1f} пунктов",
            f"влетая на {damage:.1f} единиц разрушения",
            f"вызывая повреждения в {damage:.1f} пунктов"
        ]
        
        attack_styles = [
            f"{attacker} {verb} {target} {weapon_text}{crit_texts}, {random.choice(damage_texts)}",
            f"{verb.capitalize()} {weapon_text}, {attacker} попадает по {target}{crit_texts} и {random.choice(damage_texts)}",
            f"Страшный удар! {attacker} {verb} {target} {weapon_text}{crit_texts}, {random.choice(damage_texts)}",
            f"{weapon_text.capitalize()} {attacker} {verb} {target}{crit_texts}, {random.choice(damage_texts)}",
            f"{attacker} мастерски {verb} {weapon_text} по {target}{crit_texts}, {random.choice(damage_texts)}"
        ]
        
        return random.choice(attack_styles)

    @staticmethod
    def generate_dodge_description(defender: str) -> str:
        """Генерация художественного описания уклонения"""
        dodges = [
            f"{defender} ловко уворачивается, как кошка",
            f"{defender} отпрыгивает с грацией пантеры",
            f"Словно предчувствуя удар, {defender} отклоняется в сторону",
            f"С молниеносной реакцией {defender} уклоняется от атаки",
            f"{defender} делает изящный пируэт, избегая удара",
            f"Словно читая мысли, {defender} уходит от атаки",
            f"С проворством змеи {defender} скользит в сторону",
            f"{defender} делает резкий шаг назад, уводя тело из-под удара",
            f"Словно в замедленной съёмке, {defender} отклоняет корпус",
            f"С мастерством опытного бойца {defender} парирует атаку"
        ]
        return random.choice(dodges)

    @staticmethod
    def generate_miss_description(attacker: str) -> str:
        """Генерация описания промаха"""
        misses = [
            f"{attacker} машет оружием, но попадает только по воздуху",
            f"Удар {attacker} проходит в сантиметрах от цели",
            f"{attacker} теряет равновесие и промахивается",
            f"Неуклюжий выпад {attacker} не достигает цели",
            f"{attacker} слишком медлителен — удар не достигает цели",
            f"Расчёт {attacker} оказывается неверным — удар идёт мимо",
            f"{attacker} замахивается, но в последний момент меняет траекторию",
            f"Слишком резкое движение {attacker} приводит к промаху",
            f"{attacker} не рассчитывает дистанцию и бьёт в пустоту",
            f"Оружие {attacker} свистит в воздухе, но не находит цели"
        ]
        return random.choice(misses)

    @staticmethod
    def generate_armor_block_description(defender: str, armor: Armor) -> str:
        """Генерация описания блокирования броней"""
        blocks = [
            f"Удар глухо стучит по {armor.name} {defender}, не причиняя вреда",
            f"{armor.name.capitalize()} {defender} надёжно защищает от удара",
            f"Со звоном удар отскакивает от {armor.name} {defender}",
            f"{defender} полагается на свою {armor.name} — и не зря!",
            f"Прочная {armor.name} поглощает удар, защищая {defender}",
            f"Искры летят от {armor.name}, но {defender} остаётся невредим",
            f"Удар встречает непреодолимую преграду в виде {armor.name} {defender}",
            f"{armor.name.capitalize()} демонстрирует свою надёжность, защищая {defender}",
            f"Скрежет металла — удар по {armor.name} не достигает цели",
            f"{defender} уверен в своей {armor.name}, и она его не подводит"
        ]
        return random.choice(blocks)

# ========================
# Основной класс боевой системы
# ========================

class CombatSystem:
    """Система реалистичного боя с детализированными повреждениями"""
    
    def __init__(self):
        self.body_part_hit_chance = self._init_body_part_hit_chance()
        self.material_resistances = self._init_material_resistances()
        self.wound_descriptions = self._init_wound_descriptions()
    
    def _init_body_part_hit_chance(self) -> Dict[BodyPart, float]:
        """Инициализация шансов попадания по частям тела"""
        return {
            BodyPart.HEAD: 0.1,
            BodyPart.NECK: 0.05,
            BodyPart.CHEST: 0.25,
            BodyPart.STOMACH: 0.15,
            BodyPart.ARMS: 0.15,
            BodyPart.HANDS: 0.05,
            BodyPart.LEGS: 0.2,
            BodyPart.FEET: 0.05,
            BodyPart.SHOULDERS: 0.05,
            BodyPart.GROIN: 0.01,
            BodyPart.BACK: 0.05
        }
    
    def _init_material_resistances(self) -> Dict[MaterialType, Dict[DamageType, float]]:
        """Инициализация сопротивлений материалов"""
        resistances = {
            MaterialType.IRON: {
                DamageType.SLASHING: 0.7,
                DamageType.PIERCING: 0.6,
                DamageType.BLUNT: 0.5,
                DamageType.FIRE: 0.3,
                DamageType.COLD: 0.4,
                DamageType.ELECTRIC: 0.2,
                DamageType.ACID: 0.1,
                DamageType.POISON: 0.0
            },
            MaterialType.STEEL: {
                DamageType.SLASHING: 0.8,
                DamageType.PIERCING: 0.7,
                DamageType.BLUNT: 0.6,
                DamageType.FIRE: 0.4,
                DamageType.COLD: 0.5,
                DamageType.ELECTRIC: 0.3,
                DamageType.ACID: 0.2,
                DamageType.POISON: 0.0
            },
            MaterialType.MITHRIL: {
                DamageType.SLASHING: 0.9,
                DamageType.PIERCING: 0.8,
                DamageType.BLUNT: 0.7,
                DamageType.FIRE: 0.6,
                DamageType.COLD: 0.8,
                DamageType.ELECTRIC: 0.5,
                DamageType.ACID: 0.4,
                DamageType.POISON: 0.3
            },
            MaterialType.LEATHER: {
                DamageType.SLASHING: 0.4,
                DamageType.PIERCING: 0.3,
                DamageType.BLUNT: 0.5,
                DamageType.FIRE: 0.1,
                DamageType.COLD: 0.6,
                DamageType.ELECTRIC: 0.0,
                DamageType.ACID: 0.0,
                DamageType.POISON: 0.0
            },
            MaterialType.CHAINMAIL: {
                DamageType.SLASHING: 0.7,
                DamageType.PIERCING: 0.5,
                DamageType.BLUNT: 0.3,
                DamageType.FIRE: 0.2,
                DamageType.COLD: 0.4,
                DamageType.ELECTRIC: 0.1,
                DamageType.ACID: 0.0,
                DamageType.POISON: 0.0
            },
            MaterialType.PLATE: {
                DamageType.SLASHING: 0.8,
                DamageType.PIERCING: 0.6,
                DamageType.BLUNT: 0.7,
                DamageType.FIRE: 0.3,
                DamageType.COLD: 0.5,
                DamageType.ELECTRIC: 0.2,
                DamageType.ACID: 0.1,
                DamageType.POISON: 0.0
            }
        }
        return resistances
    
    def _init_wound_descriptions(self) -> Dict[Tuple[DamageType, WoundSeverity], List[str]]:
        """Инициализация описаний ран"""
        descriptions = {
            (DamageType.SLASHING, WoundSeverity.SCRATCH): [
                "Неглубокий порез",
                "Кровавая царапина",
                "Лёгкое рассечение",
                "Поверхностная резаная рана"
            ],
            (DamageType.SLASHING, WoundSeverity.MINOR): [
                "Кровоточащий порез",
                "Заметная резаная рана",
                "Глубокая царапина",
                "Рассечённая плоть"
            ],
            (DamageType.SLASHING, WoundSeverity.MODERATE): [
                "Глубокий порез",
                "Зияющая резаная рана",
                "Сильно кровоточащее рассечение",
                "Рваная рана от лезвия"
            ],
            (DamageType.SLASHING, WoundSeverity.SEVERE): [
                "Глубокое зияющее ранение",
                "Ужасная рваная рана",
                "Разрушительный разрез",
                "Рассечённые до кости ткани"
            ],
            (DamageType.PIERCING, WoundSeverity.SCRATCH): [
                "Неглубокий прокол",
                "Крошечное отверстие",
                "Лёгкое колотое повреждение",
                "Минимальное проникновение"
            ],
            (DamageType.PIERCING, WoundSeverity.MINOR): [
                "Кровоточащий прокол",
                "Заметное колотое ранение",
                "Глубокий укол",
                "Проникающая рана"
            ],
            (DamageType.PIERCING, WoundSeverity.MODERATE): [
                "Глубокий прокол",
                "Серьёзное колотое ранение",
                "Рана от проникновения острого предмета",
                "Кровоточащее отверстие"
            ],
            (DamageType.PIERCING, WoundSeverity.SEVERE): [
                "Сквозное ранение",
                "Ужасающий прокол",
                "Глубокое проникающее ранение",
                "Разрушительное колотое повреждение"
            ],
            (DamageType.BLUNT, WoundSeverity.SCRATCH): [
                "Небольшая гематома",
                "Лёгкий ушиб",
                "Минимальный отёк",
                "Покраснение от удара"
            ],
            (DamageType.BLUNT, WoundSeverity.MINOR): [
                "Заметный синяк",
                "Кровоподтёк",
                "Ушиб средней тяжести",
                "Отёк от удара"
            ],
            (DamageType.BLUNT, WoundSeverity.MODERATE): [
                "Большая гематома",
                "Серьёзный ушиб",
                "Сильный отёк тканей",
                "Повреждение от сильного удара"
            ],
            (DamageType.BLUNT, WoundSeverity.SEVERE): [
                "Разрушительный ушиб",
                "Размозжение тканей",
                "Критическое повреждение от удара",
                "Раздробление плоти"
            ],
            (DamageType.FIRE, WoundSeverity.SCRATCH): [
                "Лёгкий ожог",
                "Покраснение кожи",
                "Незначительный термический ожог",
                "Поверхностное обгорание"
            ],
            (DamageType.FIRE, WoundSeverity.MINOR): [
                "Ожог первой степени",
                "Заметное обгорание кожи",
                "Болезненный термический ожог",
                "Пузырящаяся от жара кожа"
            ],
            (DamageType.FIRE, WoundSeverity.MODERATE): [
                "Ожог второй степени",
                "Серьёзное обгорание",
                "Глубокий термический ожог",
                "Обугливание плоти"
            ],
            (DamageType.FIRE, WoundSeverity.SEVERE): [
                "Ожог третьей степени",
                "Ужасное обгорание",
                "Критический термический ожог",
                "Обугленные ткани"
            ]
        }
        return descriptions
    
    def calculate_damage(self, attacker: CharacterStats, defender: CharacterState,
                        weapon: Optional[Weapon], attack_style: AttackStyle) -> Tuple[float, BodyPart, bool]:
        """Расчёт урона с учётом всех факторов"""
        # 1. Определяем часть тела, в которую попали
        hit_part = self._determine_hit_body_part(defender)
        
        # 2. Проверяем, есть ли броня на этой части тела
        armor = defender.armor.get(hit_part, None)
        armor_reduction = 0.0
        
        if armor:
            # Рассчитываем снижение урона от брони
            armor_reduction = self._calculate_armor_reduction(armor, weapon.damage_types[0] if weapon else DamageType.BLUNT)
            
            # Уменьшаем прочность брони
            if weapon:
                self._degrade_armor(armor, weapon)
        
        # 3. Базовый урон
        base_damage = weapon.base_damage if weapon else 5.0
        base_damage *= weapon.quality if weapon else 1.0
        
        # 4. Модификаторы от характеристик
        str_mod = attacker.strength / 10.0
        agi_mod = 0.5 + (attacker.agility / 20.0)  # От 0.5 до 1.5
        
        # 5. Модификатор стиля атаки
        style_mod = self._get_attack_style_modifier(attack_style, weapon)
        
        # 6. Критический удар (зависит от удачи и ловкости)
        critical = self._check_critical_hit(attacker)
        crit_mod = 1.5 + (attacker.luck / 20.0) if critical else 1.0
        
        # 7. Итоговый урон
        total_damage = base_damage * str_mod * agi_mod * style_mod * crit_mod * (1.0 - armor_reduction)
        
        # 8. Учитываем усталость защищающегося
        fatigue_mod = 1.0 + (defender.fatigue / 100.0)
        total_damage *= fatigue_mod
        
        # 9. Округляем
        total_damage = max(1.0, round(total_damage, 1))
        
        return total_damage, hit_part, critical
    
    def apply_damage(self, target: CharacterState, damage: float, damage_type: DamageType,
                    hit_part: BodyPart, critical: bool) -> Wound:
        """Применение урона к цели с созданием раны"""
        # 1. Определяем тяжесть ранения
        severity = self._determine_wound_severity(damage, critical)
        
        # 2. Определяем уровень боли
        pain_level = self._determine_pain_level(severity, hit_part)
        
        # 3. Проверяем, вызывает ли рана кровотечение
        bleeding = self._check_bleeding(hit_part, severity)
        
        # 4. Создаём описание раны
        wound_desc = DescriptionGenerator.generate_wound_description(
            Wound(hit_part, severity, damage_type, pain_level, bleeding, "")
        )
        
        # 5. Создаём объект раны
        wound = Wound(
            body_part=hit_part,
            severity=severity,
            damage_type=damage_type,
            pain_level=pain_level,
            bleeding=bleeding,
            description=wound_desc
        )
        
        # 6. Добавляем рану к персонажу
        target.wounds.append(wound)
        
        # 7. Обновляем состояние персонажа
        self._update_character_state(target, wound)
        
        return wound
    
    def _determine_hit_body_part(self, defender: CharacterState) -> BodyPart:
        """Определение части тела, в которую попадает удар"""
        # Учитываем текущую стойку для изменения вероятностей
        stance_modifiers = {
            AttackStyle.AGGRESSIVE: {BodyPart.HEAD: 0.15, BodyPart.CHEST: 0.3},
            AttackStyle.DEFENSIVE: {BodyPart.ARMS: 0.25, BodyPart.LEGS: 0.25},
            AttackStyle.PRECISE: {BodyPart.EYES: 0.1, BodyPart.NECK: 0.1, BodyPart.HANDS: 0.1},
            AttackStyle.BERSERK: {BodyPart.HEAD: 0.2, BodyPart.CHEST: 0.3, BodyPart.STOMACH: 0.2},
            AttackStyle.DEXTEROUS: {BodyPart.ARMS: 0.3, BodyPart.LEGS: 0.3},
            AttackStyle.BRUTAL: {BodyPart.GROIN: 0.15, BodyPart.NECK: 0.15}
        }
        
        # Копируем базовые шансы
        hit_chances = self.body_part_hit_chance.copy()
        
        # Применяем модификаторы от стойки
        if defender.stance in stance_modifiers:
            for part, mod in stance_modifiers[defender.stance].items():
                if part in hit_chances:
                    hit_chances[part] += mod
                else:
                    hit_chances[part] = mod
        
        # Нормализуем шансы
        total = sum(hit_chances.values())
        normalized = {k: v/total for k, v in hit_chances.items()}
        
        # Выбираем случайную часть тела
        rand = random.random()
        cumulative = 0.0
        
        for part, chance in normalized.items():
            cumulative += chance
            if rand <= cumulative:
                return part
        
        return BodyPart.CHEST  # fallback
    
    def _calculate_armor_reduction(self, armor: Armor, damage_type: DamageType) -> float:
        """Расчёт снижения урона от брони"""
        # Базовое сопротивление
        resistance = armor.defense.get(damage_type, 0.0)
        
        # Учитываем материал
        material_resist = self.material_resistances.get(armor.material, {}).get(damage_type, 0.0)
        
        # Учитываем состояние брони
        durability_mod = armor.durability / armor.max_durability
        
        # Итоговое сопротивление
        total_resist = (resistance + material_resist) * durability_mod * armor.coverage
        
        return min(0.9, total_resist)  # Максимум 90% снижения
    
    def _degrade_armor(self, armor: Armor, weapon: Weapon):
        """Ухудшение состояния брони при ударе"""
        # Сила удара влияет на износ
        hit_power = weapon.base_damage * (weapon.weight / 2.0)
        
        # Материал оружия влияет на износ
        weapon_material_mod = {
            MaterialType.IRON: 1.0,
            MaterialType.STEEL: 1.2,
            MaterialType.BRONZE: 0.9,
            MaterialType.MITHRIL: 1.5,
            MaterialType.ADAMANTINE: 2.0,
            MaterialType.OBSIDIAN: 1.3,
            MaterialType.BONE: 0.7,
            MaterialType.STONE: 1.1
        }.get(weapon.material, 0.8)
        
        # Материал брони влияет на износ
        armor_material_mod = {
            MaterialType.LEATHER: 1.5,
            MaterialType.STEEL: 0.8,
            MaterialType.IRON: 0.9,
            MaterialType.MITHRIL: 0.5,
            MaterialType.CHAINMAIL: 1.1,
            MaterialType.PLATE: 0.7,
            MaterialType.HARDENED_LEATHER: 1.2
        }.get(armor.material, 1.0)
        
        # Рассчитываем износ
        degradation = hit_power * weapon_material_mod * armor_material_mod * 0.01
        armor.durability = max(0, armor.durability - degradation)
    
    def _get_attack_style_modifier(self, style: AttackStyle, weapon: Optional[Weapon]) -> float:
        """Модификатор урона от стиля атаки"""
        modifiers = {
            AttackStyle.AGGRESSIVE: 1.2,
            AttackStyle.DEFENSIVE: 0.8,
            AttackStyle.BALANCED: 1.0,
            AttackStyle.PRECISE: 1.1,
            AttackStyle.BRUTAL: 1.3,
            AttackStyle.FENCING: 0.9,
            AttackStyle.BERSERK: 1.5,
            AttackStyle.DEXTEROUS: 1.0,
            AttackStyle.SAVAGE: 1.4,
            AttackStyle.TECHNICAL: 1.1,
            AttackStyle.FLUID: 1.0,
            AttackStyle.UNPREDICTABLE: 1.2
        }
        return modifiers.get(style, 1.0)
    
    def _check_critical_hit(self, attacker: CharacterStats) -> bool:
        """Проверка на критический удар"""
        crit_chance = (attacker.agility + attacker.luck) / 200.0
        return random.random() < crit_chance
    
    def _determine_wound_severity(self, damage: float, critical: bool) -> WoundSeverity:
        """Определение тяжести ранения на основе урона"""
        if critical:
            damage *= 1.5
        
        if damage < 5:
            return WoundSeverity.SCRATCH
        elif damage < 10:
            return WoundSeverity.MINOR
        elif damage < 20:
            return WoundSeverity.MODERATE
        elif damage < 35:
            return WoundSeverity.SEVERE
        elif damage < 50:
            return WoundSeverity.CRITICAL
        else:
            return WoundSeverity.FATAL
    
    def _determine_pain_level(self, severity: WoundSeverity, body_part: BodyPart) -> PainLevel:
        """Определение уровня боли"""
        # Более чувствительные части тела
        sensitive_parts = {
            BodyPart.EYES, BodyPart.GENITALS, BodyPart.FINGERS, 
            BodyPart.NOSE, BodyPart.EARS, BodyPart.NECK,
            BodyPart.THROAT, BodyPart.LIPS, BodyPart.TONGUE
        }
        
        pain_mapping = {
            WoundSeverity.SCRATCH: PainLevel.MILD,
            WoundSeverity.MINOR: PainLevel.MODERATE,
            WoundSeverity.MODERATE: PainLevel.MODERATE,
            WoundSeverity.SEVERE: PainLevel.SEVERE,
            WoundSeverity.CRITICAL: PainLevel.EXCRUCIATING,
            WoundSeverity.FATAL: PainLevel.EXCRUCIATING,
            WoundSeverity.MAIMING: PainLevel.PARALYZING,
            WoundSeverity.DISFIGURING: PainLevel.EXCRUCIATING
        }
        
        base_pain = pain_mapping.get(severity, PainLevel.MODERATE)
        
        # Увеличиваем боль для чувствительных частей
        if body_part in sensitive_parts and base_pain.value < PainLevel.EXCRUCIATING.value:
            return PainLevel(base_pain.value + 1)
        
        return base_pain
    
    def _check_bleeding(self, body_part: BodyPart, severity: WoundSeverity) -> bool:
        """Проверка, вызывает ли рана кровотечение"""
        if severity in [WoundSeverity.SCRATCH, WoundSeverity.MINOR]:
            return False
        
        # Части тела с большим количеством сосудов
        vascular_parts = {
            BodyPart.NECK, BodyPart.THIGH, BodyPart.CHEST, 
            BodyPart.STOMACH, BodyPart.UPPER_ARM, BodyPart.GROIN
        }
        
        return (severity >= WoundSeverity.MODERATE and 
                (body_part in vascular_parts or severity >= WoundSeverity.SEVERE))
    
    def _update_character_state(self, character: CharacterState, wound: Wound):
        """Обновление состояния персонажа после получения раны"""
        # Уменьшение здоровья
        health_loss = wound.get_severity_value() * 2.5
        character.health -= health_loss
        
        # Добавление боли
        character.pain += wound.get_pain_value()
        
        # Кровопотеря
        if wound.bleeding:
            character.blood_loss += wound.get_severity_value() * 0.5
        
        # Влияние на боевой дух
        morale_loss = wound.get_pain_value() * 2.0
        if wound.severity >= WoundSeverity.SEVERE:
            morale_loss *= 1.5
        character.morale -= morale_loss
        
        # Ограничения
        character.health = max(0, character.health)
        character.pain = min(100, character.pain)
        character.blood_loss = min(100, character.blood_loss)
        character.morale = max(0, character.morale)

# ========================
# Вспомогательные функции
# ========================

def create_character_stats() -> CharacterStats:
    """Создание случайных характеристик персонажа"""
    return CharacterStats(
        strength=random.randint(8, 15),
        agility=random.randint(8, 15),
        endurance=random.randint(8, 15),
        perception=random.randint(8, 15),
        intelligence=random.randint(8, 15),
        willpower=random.randint(8, 15),
        charisma=random.randint(8, 15),
        luck=random.randint(8, 15),
        dexterity=random.randint(8, 15),
        constitution=random.randint(8, 15)
    )

def create_weapon(name: str, damage_types: List[DamageType], material: MaterialType) -> Weapon:
    """Создание оружия"""
    base_damage = {
        DamageType.SLASHING: random.uniform(8, 15),
        DamageType.PIERCING: random.uniform(6, 12),
        DamageType.BLUNT: random.uniform(10, 18),
        DamageType.FIRE: random.uniform(5, 10),
        DamageType.COLD: random.uniform(5, 10),
        DamageType.ELECTRIC: random.uniform(4, 8),
        DamageType.ACID: random.uniform(3, 7),
        DamageType.POISON: random.uniform(2, 5)
    }.get(damage_types[0], 10.0)
    
    weight = {
        MaterialType.IRON: random.uniform(2.0, 3.5),
        MaterialType.STEEL: random.uniform(1.8, 3.2),
        MaterialType.BRONZE: random.uniform(2.2, 3.8),
        MaterialType.MITHRIL: random.uniform(1.0, 2.0),
        MaterialType.ADAMANTINE: random.uniform(3.0, 4.5),
        MaterialType.OBSIDIAN: random.uniform(1.5, 2.5),
        MaterialType.BONE: random.uniform(1.0, 2.0),
        MaterialType.WOOD: random.uniform(1.5, 2.5)
    }.get(material, 2.5)
    
    quality = random.uniform(0.8, 1.2)  # Качество изготовления
    
    return Weapon(
        name=name,
        damage_types=damage_types,
        base_damage=base_damage,
        material=material,
        weight=weight,
        attack_speed=random.uniform(0.8, 1.5),
        reach=random.uniform(0.5, 2.0),
        durability=100.0,
        max_durability=100.0,
        description=f"{name}, изготовленный из {material.name.lower()}",
        quality=quality
    )

def create_armor(name: str, covered_parts: List[BodyPart], material: MaterialType) -> Armor:
    """Создание брони"""
    defense = {
        DamageType.SLASHING: random.uniform(0.4, 0.8),
        DamageType.PIERCING: random.uniform(0.3, 0.7),
        DamageType.BLUNT: random.uniform(0.2, 0.6),
        DamageType.FIRE: random.uniform(0.1, 0.5),
        DamageType.COLD: random.uniform(0.1, 0.5),
        DamageType.ELECTRIC: random.uniform(0.0, 0.3),
        DamageType.ACID: random.uniform(0.0, 0.2),
        DamageType.POISON: random.uniform(0.0, 0.1)
    }
    
    weight = {
        MaterialType.LEATHER: random.uniform(2.0, 4.0),
        MaterialType.STEEL: random.uniform(8.0, 15.0),
        MaterialType.IRON: random.uniform(10.0, 18.0),
        MaterialType.MITHRIL: random.uniform(4.0, 8.0),
        MaterialType.CHAINMAIL: random.uniform(6.0, 12.0),
        MaterialType.PLATE: random.uniform(12.0, 20.0),
        MaterialType.HARDENED_LEATHER: random.uniform(3.0, 6.0)
    }.get(material, 5.0)
    
    flexibility = {
        MaterialType.LEATHER: random.uniform(0.7, 0.9),
        MaterialType.STEEL: random.uniform(0.3, 0.5),
        MaterialType.MITHRIL: random.uniform(0.6, 0.8),
        MaterialType.CHAINMAIL: random.uniform(0.5, 0.7),
        MaterialType.PLATE: random.uniform(0.2, 0.4)
    }.get(material, 0.5)
    
    return Armor(
        name=name,
        covered_parts=covered_parts,
        defense=defense,
        material=material,
        weight=weight,
        durability=100.0,
        max_durability=100.0,
        description=f"{name}, сделанная из {material.name.lower()}",
        flexibility=flexibility
    )

# ========================
# Пример использования
# ========================

if __name__ == "__main__":
    # Инициализация системы боя
    combat = CombatSystem()
    
    # Создание персонажей
    player_stats = create_character_stats()
    enemy_stats = create_character_stats()
    
    player_state = CharacterState()
    enemy_state = CharacterState()
    
    # Создание оружия и брони
    sword = create_weapon("Стальной меч", [DamageType.SLASHING], MaterialType.STEEL)
    player_state.equipped_weapon = sword
    
    axe = create_weapon("Боевой топор", [DamageType.SLASHING, DamageType.BLUNT], MaterialType.IRON)
    enemy_state.equipped_weapon = axe
    
    armor = create_armor("Кожаный доспех", 
                        [BodyPart.CHEST, BodyPart.STOMACH, BodyPart.BACK], 
                        MaterialType.LEATHER)
    player_state.armor[BodyPart.CHEST] = armor
    player_state.armor[BodyPart.STOMACH] = armor
    player_state.armor[BodyPart.BACK] = armor
    
    # Пример боя
    print("Начало боя!")
    print(f"Игрок ({player_stats}) vs Враг ({enemy_stats})")
    print("----------------------------")
    
    # Игрок атакует врага
    damage, hit_part, critical = combat.calculate_damage(
        player_stats, enemy_state, sword, AttackStyle.AGGRESSIVE
    )
    wound = combat.apply_damage(enemy_state, damage, sword.damage_types[0], hit_part, critical)
    
    # Вывод результатов
    print(DescriptionGenerator.generate_attack_description(
        "Игрок", "врага", sword, damage, critical
    ))
    print(f"Ранение: {wound.description}")
    print(f"Состояние врага: Здоровье={enemy_state.health:.1f}, Боль={enemy_state.pain:.1f}, Мораль={enemy_state.morale:.1f}")
    print("----------------------------")
    
    # Враг атакует игрока
    damage, hit_part, critical = combat.calculate_damage(
        enemy_stats, player_state, axe, AttackStyle.BRUTAL
    )
    
    # Проверка на попадание по броне
    if hit_part in player_state.armor and player_state.armor[hit_part]:
        print(DescriptionGenerator.generate_armor_block_description(
            "игрока", player_state.armor[hit_part]
        ))
        damage *= 0.3  # Уменьшаем урон при попадании в броню
    
    wound = combat.apply_damage(player_state, damage, axe.damage_types[0], hit_part, critical)
    
    print("\nВраг атакует!")
    print(DescriptionGenerator.generate_attack_description(
        "Враг", "игрока", axe, damage, critical
    ))
    if wound.severity != WoundSeverity.SCRATCH:
        print(f"Ранение: {wound.description}")
    print(f"Состояние игрока: Здоровье={player_state.health:.1f}, Боль={player_state.pain:.1f}, Мораль={player_state.morale:.1f}")
    print("----------------------------")
    
    # Второй удар игрока
    damage, hit_part, critical = combat.calculate_damage(
        player_stats, enemy_state, sword, AttackStyle.PRECISE
    )
    wound = combat.apply_damage(enemy_state, damage, sword.damage_types[0], hit_part, critical)
    
    print("\nИгрок контратакует!")
    print(DescriptionGenerator.generate_attack_description(
        "Игрок", "врага", sword, damage, critical
    ))
    print(f"Ранение: {wound.description}")
    print(f"Состояние врага: Здоровье={enemy_state.health:.1f}, Боль={enemy_state.pain:.1f}, Мораль={enemy_state.morale:.1f}")
    
    # Проверка на смерть врага
    if enemy_state.health <= 0:
        print("\nВраг повержен! Игрок побеждает!")
    elif player_state.health <= 0:
        print("\nИгрок повержен! Враг побеждает!")
    else:
        print("\nБой продолжается...")
