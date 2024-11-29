from __future__ import annotations

from pydantic import Field

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_pt_br: tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


class HourlyItem(base.HourlyItem):
    lang_pt_br: tuple[base.LangItem, ...] = Field(alias="lang_pt-br")


Model = base.Model[CurrentConditionItem, HourlyItem]
