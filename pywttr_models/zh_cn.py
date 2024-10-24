from __future__ import annotations

from pydantic import Field

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_zh_cn: tuple[base.LangItem, ...] = Field(alias="lang_zh-cn")


class HourlyItem(base.HourlyItem):
    lang_zh_cn: tuple[base.LangItem, ...] = Field(alias="lang_zh-cn")


class WeatherItem(base.WeatherItem):
    hourly: tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: tuple[CurrentConditionItem, ...]
    weather: tuple[WeatherItem, ...]
