"""Response models for Kazakh."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Kazakh."""

    lang_kk: tuple[base.WeatherDescItem, ...]
    """Weather description in Kazakh, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Kazakh."""

    lang_kk: tuple[base.WeatherDescItem, ...]
    """Weather description in Kazakh, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.KK`."""
