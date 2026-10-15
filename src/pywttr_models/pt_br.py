"""Response models for Brazilian Portuguese."""

from __future__ import annotations

from pydantic import Field

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Brazilian Portuguese."""

    lang_pt_br: tuple[base.WeatherDescItem, ...] = Field(alias="lang_pt-br")
    """Weather description in Brazilian Portuguese, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Brazilian Portuguese."""

    lang_pt_br: tuple[base.WeatherDescItem, ...] = Field(alias="lang_pt-br")
    """Weather description in Brazilian Portuguese, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.PT_BR`."""
