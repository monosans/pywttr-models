from __future__ import annotations

import enum
from typing import Any, Self


class StrEnum(enum.StrEnum):
    def __new__(cls, value: str, *_: Any) -> Self:
        member = str.__new__(cls, value)
        member._value_ = value
        return member
