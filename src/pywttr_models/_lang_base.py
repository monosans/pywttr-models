from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_xx: tuple[base.WeatherDescItem, ...]


class HourlyItem(base.HourlyItem):
    lang_xx: tuple[base.WeatherDescItem, ...]


Model = base.Model
