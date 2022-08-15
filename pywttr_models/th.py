from __future__ import annotations

from typing import List

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_th: List[base.LangItem]


class HourlyItem(base.HourlyItem):
    lang_th: List[base.LangItem]


class WeatherItem(base.WeatherItem):
    hourly: List[HourlyItem]


class Model(base.Model):
    current_condition: List[CurrentConditionItem]
    weather: List[WeatherItem]
