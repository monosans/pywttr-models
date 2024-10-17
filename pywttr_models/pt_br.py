from __future__ import annotations

from pydantic import Field

from . import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pt_br: tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


class HourlyItem(base.HourlyItem):
    lang_pt_br: tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


class WeatherItem(base.WeatherItem):
    hourly: tuple[HourlyItem, ...]


class Model(base.Model):
    current_condition: tuple[CurrentConditionItem, ...]
    weather: tuple[WeatherItem, ...]
