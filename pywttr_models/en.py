from __future__ import annotations

from typing import Final

from pywttr_models import base

CurrentConditionItem: Final = base.CurrentConditionItem
HourlyItem: Final = base.HourlyItem

Model: Final = base.Model[CurrentConditionItem, HourlyItem]
