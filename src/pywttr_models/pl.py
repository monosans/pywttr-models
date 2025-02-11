from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pl: tuple[base.LangItem, ...]


class HourlyItem(base.HourlyItem):
    lang_pl: tuple[base.LangItem, ...]


Model = base.Model[CurrentConditionItem, HourlyItem]
