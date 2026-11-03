"""Response models for Latvian."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Latvian."""

    lang_lv: tuple[base.WeatherDescItem, ...]
    """Weather description in Latvian, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Latvian."""

    lang_lv: tuple[base.WeatherDescItem, ...]
    """Weather description in Latvian, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.LV`."""
