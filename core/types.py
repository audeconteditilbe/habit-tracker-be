from typing import Optional, TypedDict, Union

class HabitListQuery(TypedDict):
    userId: Optional[str]

class EntryListQuery(TypedDict):
    habitId: str
    time_start: Optional[str]
    time_end: Optional[str]

class UserListQuery(TypedDict):
    userId: Optional[str]