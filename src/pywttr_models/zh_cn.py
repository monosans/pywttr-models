"""Response models for Simplified Chinese."""

from __future__ import annotations

from pydantic import Field

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Simplified Chinese."""

    lang_zh_cn: tuple[base.WeatherDescItem, ...] = Field(alias="lang_zh-cn")
    """Weather description in Simplified Chinese, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Simplified Chinese."""

    lang_zh_cn: tuple[base.WeatherDescItem, ...] = Field(alias="lang_zh-cn")
    """Weather description in Simplified Chinese, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.ZH_CN`."""
