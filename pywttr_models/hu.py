from __future__ import annotations

from typing import Tuple

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_hu: Tuple[base.LangItem, ...]


class HourlyItem(base.HourlyItem):
    lang_hu: Tuple[base.LangItem, ...]


class WeatherItem(base.WeatherItem):
    hourly: Tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: Tuple[CurrentConditionItem, ...]
    weather: Tuple[WeatherItem, ...]
