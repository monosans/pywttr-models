from typing import List

from pydantic import Field

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_sr_lat: List[base.LangItem] = Field(..., alias="lang_sr-lat")


class HourlyItem(base.HourlyItem):
    lang_sr_lat: List[base.LangItem] = Field(..., alias="lang_sr-lat")


class WeatherItem(base.WeatherItem):
    hourly: List[HourlyItem]


class Model(base.Model):
    current_condition: List[CurrentConditionItem]
    weather: List[WeatherItem]
