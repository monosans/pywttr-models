from __future__ import annotations

from pywttr_models import base

CurrentConditionItem = base.CurrentConditionItem
HourlyItem = base.HourlyItem

Model = base.Model[CurrentConditionItem, HourlyItem]
