"""Response models for Finnish."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Finnish."""

    lang_fi: tuple[base.WeatherDescItem, ...]
    """Weather description in Finnish, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Finnish."""

    lang_fi: tuple[base.WeatherDescItem, ...]
    """Weather description in Finnish, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.FI`."""
