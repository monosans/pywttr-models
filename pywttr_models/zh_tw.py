from __future__ import annotations

from typing import Tuple

from pydantic import Field

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_zh_tw: Tuple[base.LangItem, ...] = Field(alias="lang_zh-tw")


class HourlyItem(base.HourlyItem):
    lang_zh_tw: Tuple[base.LangItem, ...] = Field(alias="lang_zh-tw")


class WeatherItem(base.WeatherItem):
    hourly: Tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: Tuple[CurrentConditionItem, ...]
    weather: Tuple[WeatherItem, ...]
