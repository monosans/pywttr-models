from __future__ import annotations

from typing import List

try:
    from pydantic.v1 import Field
except ImportError:  # pragma: no cover
    from pydantic import Field  # type: ignore[assignment]

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pt_br: List[base.LangItem] = Field(alias="lang_pt-br")


class HourlyItem(base.HourlyItem):
    lang_pt_br: List[base.LangItem] = Field(alias="lang_pt-br")


class WeatherItem(base.WeatherItem):
    hourly: List[HourlyItem]


class Model(base.Model):
    current_condition: List[CurrentConditionItem]
    weather: List[WeatherItem]
