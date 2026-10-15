"""Response models for Danish."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Danish."""

    lang_da: tuple[base.WeatherDescItem, ...]
    """Weather description in Danish, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Danish."""

    lang_da: tuple[base.WeatherDescItem, ...]
    """Weather description in Danish, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.DA`."""
