from __future__ import annotations

from pydantic import Field

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_zh_cn: tuple[base.LangItem, ...] = Field(alias="lang_zh-cn")


class HourlyItem(base.HourlyItem):
    lang_zh_cn: tuple[base.LangItem, ...] = Field(alias="lang_zh-cn")


Model = base.Model[CurrentConditionItem, HourlyItem]
