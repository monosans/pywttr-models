from typing import List

from pywttr_models import base


class WeatherItem(base.WeatherItem):
    hourly: List[base.HourlyItem]


class Model(base.Model):
    current_condition: List[base.CurrentConditionItem]
    weather: List[WeatherItem]
