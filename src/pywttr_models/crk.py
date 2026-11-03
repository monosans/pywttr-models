"""Response models for Plains Cree."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Plains Cree."""

    lang_crk: tuple[base.WeatherDescItem, ...]
    """Weather description in Plains Cree, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Plains Cree."""

    lang_crk: tuple[base.WeatherDescItem, ...]
    """Weather description in Plains Cree, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.CRK`."""
