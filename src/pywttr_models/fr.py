"""Response models for French."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in French."""

    lang_fr: tuple[base.WeatherDescItem, ...]
    """Weather description in French, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in French."""

    lang_fr: tuple[base.WeatherDescItem, ...]
    """Weather description in French, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.FR`."""
