from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from typing_extensions import Any, Self, override


class StrEnum(str, Enum):
    if TYPE_CHECKING:
        _value_: str

        @property
        @override
        def value(self) -> str: ...

        def __new__(cls, value: str) -> Self: ...

    else:

        def __new__(cls, value: str, *_: Any) -> Self:
            member = str.__new__(cls, value)
            member._value_ = value
            return member

    @staticmethod
    @override
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[str]
    ) -> str:
        return name

    __str__ = str.__str__
    __format__ = str.__format__  # type: ignore[assignment]
