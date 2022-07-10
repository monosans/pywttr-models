from __future__ import annotations

from pydantic import Field

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pt_br: list[base.LangItem] = Field(..., alias="lang_pt-br")


class HourlyItem(base.HourlyItem):
    lang_pt_br: list[base.LangItem] = Field(..., alias="lang_pt-br")


class WeatherItem(base.WeatherItem):
    hourly: list[HourlyItem]


class Model(base.Model):
    current_condition: list[CurrentConditionItem]
    weather: list[WeatherItem]
