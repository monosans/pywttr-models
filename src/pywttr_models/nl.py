"""Response models for Dutch."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Dutch."""

    lang_nl: tuple[base.WeatherDescItem, ...]
    """Weather description in Dutch, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Dutch."""

    lang_nl: tuple[base.WeatherDescItem, ...]
    """Weather description in Dutch, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.NL`."""
