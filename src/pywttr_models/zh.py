"""Response models for Chinese."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Chinese."""

    lang_zh: tuple[base.WeatherDescItem, ...]
    """Weather description in Chinese, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Chinese."""

    lang_zh: tuple[base.WeatherDescItem, ...]
    """Weather description in Chinese, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.ZH`."""
