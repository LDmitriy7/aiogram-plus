from __future__ import annotations
import inspect
from typing import Optional

from ..dispatcher import Dispatcher


class State:
    """
    State object
    """

    def __init__(self, state: Optional[str] = None, group_name: Optional[str] = None): ...

    @property
    def group(self) -> type[StatesGroup]: ...

    def get_root(self) -> type[StatesGroup]: ...

    @property
    def state(self) -> str: ...

    def set_parent(self, group): ...

    async def set(self): ...


class StatesGroupMeta(type):

    @property
    def __group_name__(cls) -> str: ...

    @property
    def __full_group_name__(cls) -> str: ...

    @property
    def states(cls) -> tuple[State]: ...

    @property
    def childs(cls) -> tuple[StatesGroupMeta]: ...

    @property
    def all_childs(cls) -> tuple[StatesGroupMeta]: ...

    @property
    def all_states(cls) -> tuple[State]: ...

    @property
    def all_states_names(cls) -> tuple[str]: ...

    @property
    def states_names(cls) -> tuple[str]: ...

    def get_root(cls) -> StatesGroupMeta: ...


class StatesGroup(metaclass=StatesGroupMeta):

    @classmethod
    async def next(cls) -> str: ...

    @classmethod
    async def previous(cls) -> str: ...

    @classmethod
    async def first(cls) -> str: ...

    @classmethod
    async def last(cls) -> str: ...
