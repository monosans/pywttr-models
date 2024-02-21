from __future__ import annotations

from typing import Tuple

from pydantic import Field

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pt_br: Tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


class HourlyItem(base.HourlyItem):
    lang_pt_br: Tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


class WeatherItem(base.WeatherItem):
    hourly: Tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: Tuple[CurrentConditionItem, ...]
    weather: Tuple[WeatherItem, ...]
