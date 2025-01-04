from typing import Literal, Optional, TypedDict

from core.models import HabitStatus


class HabitListQuery(TypedDict):
    userId: Optional[str]
    status: Optional[HabitStatus]
    ongoing: Optional[Literal["0", "1"]]


class EntryListQuery(TypedDict):
    habitId: str
    time_start: Optional[str]
    time_end: Optional[str]


class UserListQuery(TypedDict):
    userId: Optional[str]
