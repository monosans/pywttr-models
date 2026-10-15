"""Response models for Catalan."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Catalan."""

    lang_ca: tuple[base.WeatherDescItem, ...]
    """Weather description in Catalan, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Catalan."""

    lang_ca: tuple[base.WeatherDescItem, ...]
    """Weather description in Catalan, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.CA`."""
