"""Response models for Turkish."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Turkish."""

    lang_tr: tuple[base.WeatherDescItem, ...]
    """Weather description in Turkish, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Turkish."""

    lang_tr: tuple[base.WeatherDescItem, ...]
    """Weather description in Turkish, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.TR`."""
