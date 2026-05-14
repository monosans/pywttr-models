from __future__ import annotations

from pydantic import Field

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    lang_zh_cn: tuple[base.WeatherDescItem, ...] = Field(alias="lang_zh-cn")


class HourlyItem(_lang_base.HourlyItem):
    lang_zh_cn: tuple[base.WeatherDescItem, ...] = Field(alias="lang_zh-cn")


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
