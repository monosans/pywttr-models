from __future__ import annotations

from pywttr_models import base


class WeatherItem(base.WeatherItem):
    hourly: list[base.HourlyItem]


class Model(base.Model):
    current_condition: list[base.CurrentConditionItem]
    weather: list[WeatherItem]
