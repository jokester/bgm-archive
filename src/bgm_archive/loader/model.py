from enum import Enum, IntEnum
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict

_config = ConfigDict(use_enum_values=True, extra="forbid")


class SubjectType(IntEnum):
    """Subject types in Bangumi."""

    BOOK = 1  # 书籍
    ANIME = 2  # 动画
    MUSIC = 3  # 音乐
    GAME = 4  # 游戏
    REAL = 6  # 三次元


class PersonType(IntEnum):
    """Person types in Bangumi."""

    OTHER = 0  # 其他

    INDIVIDUAL = 1  # 个人
    COMPANY = 2  # 公司
    ASSOCIATION = 3  # 组合


class CharacterRole(IntEnum):
    """Character role types in Bangumi."""

    MAIN = 1  # 主角
    SUPPORTING = 2  # 配角
    GUEST = 3  # 客串

    OTHER = 4  # 其他


class EpisodeType(IntEnum):
    """Episode types in Bangumi."""

    MAIN = 0  # 正篇
    SPECIAL = 1  # 特别篇
    OP = 2  # OP
    ED = 3  # ED
    TRAILER = 4  # 预告/宣传/广告
    MAD = 5  # MAD
    OTHER = 6  # 其他


class RelationType(IntEnum):
    """Relation types between subjects."""

    # Anime relations (1-99)
    ADAPTATION = 1  # Shared by Anime, Book, Game - Adaptation / 改编
    PREQUEL = 2  # Prequel / 前传
    SEQUEL = 3  # Sequel / 续集
    SUMMARY = 4  # Summary / 总集篇
    FULL_STORY = 5  # Full Story / 全集
    SIDE_STORY = 6  # Side Story / 番外篇
    CHARACTER = 7  # Character / 角色出演
    SAME_SETTING = 8  # Same setting / 相同世界观
    ALTERNATIVE_SETTING = 9  # Alternative setting / 不同世界观
    ALTERNATIVE_VERSION = 10  # Alternative version / 不同演绎
    SPIN_OFF = 11  # Spin-off / 衍生
    PARENT_STORY = 12  # Parent Story / 主线故事
    COLLABORATION = 14  # Collaboration / 联动
    OTHER = 99  # Other / 其他

    # Book relations (1000-1099)
    BOOK_SERIES = 1002  # Series / 系列
    BOOK_OFFPRINT = 1003  # Offprint / 单行本
    BOOK_ALBUM = 1004  # Album / 画集
    BOOK_PREQUEL = 1005  # Prequel / 前传
    BOOK_SEQUEL = 1006  # Sequel / 续集
    BOOK_SIDE_STORY = 1007  # Side Story / 番外篇
    BOOK_PARENT_STORY = 1008  # Parent Story / 主线故事
    BOOK_ALTERNATIVE_VERSION = 1010  # Alternative version / 不同版本
    BOOK_CHARACTER = 1011  # Character / 角色出演
    BOOK_SAME_SETTING = 1012  # Same setting / 相同世界观
    BOOK_ALTERNATIVE_SETTING = 1013  # Alternative setting / 不同世界观
    BOOK_COLLABORATION = 1014  # Collaboration / 联动
    BOOK_OTHER = 1099  # Other / 其他

    # Music relations (3000-3099)
    MUSIC_OST = 3001  # OST / 原声集
    MUSIC_CHARACTER_SONG = 3002  # Character Song / 角色歌
    MUSIC_OPENING_SONG = 3003  # Opening Song / 片头曲
    MUSIC_ENDING_SONG = 3004  # Ending Song / 片尾曲
    MUSIC_INSERT_SONG = 3005  # Insert Song / 插入歌
    MUSIC_IMAGE_SONG = 3006  # Image Song / 印象曲
    MUSIC_DRAMA = 3007  # Drama / 广播剧
    MUSIC_OTHER = 3099  # Other / 其他

    # Game relations (4000-4099)
    GAME_PREQUEL = 4002  # Prequel / 前传
    GAME_SEQUEL = 4003  # Sequel / 续集
    GAME_SIDE_STORY = 4006  # Side Story / 外传
    GAME_CHARACTER = 4007  # Character / 角色出演
    GAME_SAME_SETTING = 4008  # Same Setting / 相同世界观
    GAME_ALTERNATIVE_SETTING = 4009  # Alternative Setting / 不同世界观
    GAME_ALTERNATIVE_VERSION = 4010  # Alternative Version / 不同演绎
    GAME_VERSION = 4011  # Version / 不同版本
    GAME_PARENT_STORY = 4012  # Parent Story / 主线故事
    GAME_MAIN_VERSION = 4013  # Main Version / 主版本
    GAME_COLLABORATION = 4014  # Collaboration / 联动
    GAME_DLC = 4015  # DLC / 扩展包
    GAME_COLLECTION = 4016  # Collection / 合集
    GAME_IN_COLLECTION = 4017  # In Collection / 收录作品
    GAME_OTHER = 4099  # Other / 其他


class CharacterSubjectType(IntEnum):
    """Character types in subject-character relationships."""

    MAIN = 1  # 主角
    SUPPORTING = 2  # 配角
    GUEST = 3  # 客串


class Tag(BaseModel):
    """Tag model for subjects."""

    name: str
    count: int


class ScoreDetails(BaseModel):
    """Score distribution details."""

    score_1: int = Field(0, alias="1")
    score_2: int = Field(0, alias="2")
    score_3: int = Field(0, alias="3")
    score_4: int = Field(0, alias="4")
    score_5: int = Field(0, alias="5")
    score_6: int = Field(0, alias="6")
    score_7: int = Field(0, alias="7")
    score_8: int = Field(0, alias="8")
    score_9: int = Field(0, alias="9")
    score_10: int = Field(0, alias="10")


class Favorite(BaseModel):
    """Favorite statistics."""

    wish: int
    done: int
    doing: int
    on_hold: int
    dropped: int


class Subject(BaseModel):
    """Subject model (anime, book, game, etc.)."""

    model_config = _config

    id: int
    type: SubjectType
    name: str
    name_cn: str
    infobox: str
    platform: int
    summary: str
    nsfw: bool
    tags: List[Tag] = Field(default_factory=list)
    score: float
    score_details: Optional[ScoreDetails] = None
    rank: int
    date: str
    favorite: Favorite
    series: bool
    meta_tags: Optional[str] = None


class Person(BaseModel):
    """Person model (individual, company, association)."""

    model_config = _config

    id: int
    name: str
    type: PersonType
    career: List[str] = Field(default_factory=list)
    infobox: str
    summary: str
    comments: int
    collects: int


class Character(BaseModel):
    """Character model."""

    model_config = _config

    id: int
    role: CharacterRole
    name: str
    infobox: str
    summary: str
    comments: int
    collects: int


class Episode(BaseModel):
    """Episode model."""

    model_config = _config

    id: int
    name: str
    name_cn: str
    description: str
    airdate: str
    disc: int
    duration: str
    subject_id: int
    sort: int | float
    type: EpisodeType


class SubjectRelation(BaseModel):
    """Relation between subjects."""

    model_config = _config

    subject_id: int
    relation_type: RelationType
    related_subject_id: int
    order: int


class SubjectCharacter(BaseModel):
    """Relation between subject and character."""

    model_config = _config

    character_id: int
    subject_id: int
    type: CharacterSubjectType
    order: int


class SubjectPerson(BaseModel):
    """Relation between subject and person."""

    model_config = _config

    person_id: int
    subject_id: int
    position: str  # FIXME: need actual values


class PersonCharacter(BaseModel):
    """Relation between person and character."""

    model_config = _config

    person_id: int
    subject_id: int
    character_id: int
    summary: str
