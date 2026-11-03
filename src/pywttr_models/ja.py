"""Response models for Japanese."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Japanese."""

    lang_ja: tuple[base.WeatherDescItem, ...]
    """Weather description in Japanese, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Japanese."""

    lang_ja: tuple[base.WeatherDescItem, ...]
    """Weather description in Japanese, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.JA`."""
