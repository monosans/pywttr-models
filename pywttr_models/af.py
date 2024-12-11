from __future__ import annotations

from typing import Final

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_af: tuple[base.LangItem, ...]


class HourlyItem(base.HourlyItem):
    lang_af: tuple[base.LangItem, ...]


Model: Final = base.Model[CurrentConditionItem, HourlyItem]
