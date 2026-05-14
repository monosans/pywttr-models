from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    lang_nl: tuple[base.WeatherDescItem, ...]


class HourlyItem(_lang_base.HourlyItem):
    lang_nl: tuple[base.WeatherDescItem, ...]


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
