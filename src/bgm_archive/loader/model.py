from enum import Enum, IntEnum
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict

_config = ConfigDict(use_enum_values=True)


class SubjectType(IntEnum):
    """Subject types in Bangumi."""

    BOOK = 1  # 书籍
    ANIME = 2  # 动画
    MUSIC = 3  # 音乐
    GAME = 4  # 游戏
    REAL = 6  # 三次元


class PersonType(IntEnum):
    """Person types in Bangumi."""

    _UNKNOWN = 0  # TODO: ask upstream

    INDIVIDUAL = 1  # 个人
    COMPANY = 2  # 公司
    ASSOCIATION = 3  # 组合


class CharacterRole(IntEnum):
    """Character role types in Bangumi."""

    MAIN = 1  # 主角
    SUPPORTING = 2  # 配角
    GUEST = 3  # 客串

    _UNKNOWN4 = 4  # TODO: ask upstream


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

    SEQUEL = 1  # 续集
    PREQUEL = 2  # 前传
    SAME_SETTING = 3  # 同一世界观
    SAME_SERIES = 4  # 同一系列
    SIDE_STORY = 5  # 外传
    PARENT_STORY = 6  # 主线故事
    ALTERNATIVE_VERSION = 7  # 不同版本
    CHARACTER_SAME = 8  # 角色相同
    SPIN_OFF = 9  # 衍生
    ADAPTATION = 10  # 改编
    ALTERNATIVE_SETTING = 11  # 不同世界观
    OTHER = 0  # 其他

    # UNKNOWN_1 = 4002  # TODO: ask upstream
    # UNKNOWN_2 = 4006  # TODO: ask upstream


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

    id: int
    role: CharacterRole
    name: str
    infobox: str
    summary: str
    comments: int
    collects: int


class Episode(BaseModel):
    """Episode model."""

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

    character_id: int
    subject_id: int
    type: CharacterSubjectType
    order: int


class SubjectPerson(BaseModel):
    """Relation between subject and person."""

    person_id: int
    subject_id: int
    position: str


class PersonCharacter(BaseModel):
    """Relation between person and character."""

    person_id: int
    subject_id: int
    character_id: int
    summary: str
