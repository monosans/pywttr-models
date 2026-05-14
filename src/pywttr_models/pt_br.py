from __future__ import annotations

from pydantic import Field

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    lang_pt_br: tuple[base.WeatherDescItem, ...] = Field(alias="lang_pt-br")


class HourlyItem(_lang_base.HourlyItem):
    lang_pt_br: tuple[base.WeatherDescItem, ...] = Field(alias="lang_pt-br")


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
