from typing import List

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_am: List[base.LangItem]


class HourlyItem(base.HourlyItem):
    lang_am: List[base.LangItem]


class WeatherItem(base.WeatherItem):
    hourly: List[HourlyItem]


class Model(base.Model):
    current_condition: List[CurrentConditionItem]
    weather: List[WeatherItem]
