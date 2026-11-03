"""Response models for Telugu."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Telugu."""

    lang_te: tuple[base.WeatherDescItem, ...]
    """Weather description in Telugu, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Telugu."""

    lang_te: tuple[base.WeatherDescItem, ...]
    """Weather description in Telugu, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.TE`."""
