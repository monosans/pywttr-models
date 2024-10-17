from __future__ import annotations

from . import base


class WeatherItem(base.WeatherItem):
    hourly: tuple[base.HourlyItem, ...]


class Model(base.Model):
    current_condition: tuple[base.CurrentConditionItem, ...]
    weather: tuple[WeatherItem, ...]
