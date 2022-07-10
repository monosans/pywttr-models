from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_ar: list[base.LangItem]


class HourlyItem(base.HourlyItem):
    lang_ar: list[base.LangItem]


class WeatherItem(base.WeatherItem):
    hourly: list[HourlyItem]


class Model(base.Model):
    current_condition: list[CurrentConditionItem]
    weather: list[WeatherItem]
