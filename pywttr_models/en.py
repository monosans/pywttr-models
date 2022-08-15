from __future__ import annotations

from typing import List

from . import base


class WeatherItem(base.WeatherItem):
    hourly: List[base.HourlyItem]


class Model(base.Model):
    current_condition: List[base.CurrentConditionItem]
    weather: List[WeatherItem]
