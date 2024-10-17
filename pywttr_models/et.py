from __future__ import annotations

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_et: tuple[base.LangItem, ...]


class HourlyItem(base.HourlyItem):
    lang_et: tuple[base.LangItem, ...]


class WeatherItem(base.WeatherItem):
    hourly: tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: tuple[CurrentConditionItem, ...]
    weather: tuple[WeatherItem, ...]
