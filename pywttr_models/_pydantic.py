from __future__ import annotations

from pydantic import BaseModel


class FrozenModel(BaseModel):
    model_config = {"frozen": True}
