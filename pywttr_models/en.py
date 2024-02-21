from __future__ import annotations

from typing import Tuple

from . import base


class WeatherItem(base.WeatherItem):
    hourly: Tuple[base.HourlyItem, ...]


class Model(base.Model):
    current_condition: Tuple[base.CurrentConditionItem, ...]
    weather: Tuple[WeatherItem, ...]
