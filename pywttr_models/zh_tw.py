from __future__ import annotations

from typing import List

try:
    from pydantic.v1 import Field
except ImportError:  # pragma: no cover
    from pydantic import Field  # type: ignore[assignment]

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_zh_tw: List[base.LangItem] = Field(alias="lang_zh-tw")


class HourlyItem(base.HourlyItem):
    lang_zh_tw: List[base.LangItem] = Field(alias="lang_zh-tw")


class WeatherItem(base.WeatherItem):
    hourly: List[HourlyItem]


class Model(base.Model):
    current_condition: List[CurrentConditionItem]
    weather: List[WeatherItem]
