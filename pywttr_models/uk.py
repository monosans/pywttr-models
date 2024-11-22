from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_uk: tuple[base.LangItem, ...]


class HourlyItem(base.HourlyItem):
    lang_uk: tuple[base.LangItem, ...]


class WeatherItem(base.WeatherItem):
    hourly: tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: tuple[CurrentConditionItem, ...]
    weather: tuple[WeatherItem, ...]
