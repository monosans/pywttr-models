"""Response models for Czech."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Czech."""

    lang_cs: tuple[base.WeatherDescItem, ...]
    """Weather description in Czech, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Czech."""

    lang_cs: tuple[base.WeatherDescItem, ...]
    """Weather description in Czech, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.CS`."""
