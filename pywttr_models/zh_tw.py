from __future__ import annotations

from pydantic import Field

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_zh_tw: list[base.LangItem] = Field(..., alias="lang_zh-tw")


class HourlyItem(base.HourlyItem):
    lang_zh_tw: list[base.LangItem] = Field(..., alias="lang_zh-tw")


class WeatherItem(base.WeatherItem):
    hourly: list[HourlyItem]


class Model(base.Model):
    current_condition: list[CurrentConditionItem]
    weather: list[WeatherItem]
