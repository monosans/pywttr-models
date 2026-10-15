"""Response models for Hindi."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Hindi."""

    lang_hi: tuple[base.WeatherDescItem, ...]
    """Weather description in Hindi, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Hindi."""

    lang_hi: tuple[base.WeatherDescItem, ...]
    """Weather description in Hindi, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.HI`."""
