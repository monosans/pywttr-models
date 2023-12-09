from __future__ import annotations

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:  # pragma: no cover
    from pydantic import BaseModel, Field  # type: ignore[assignment]


__all__ = ("BaseModel", "Field")
