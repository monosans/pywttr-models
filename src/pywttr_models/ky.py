"""Response models for Kyrgyz."""

from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Kyrgyz."""

    lang_ky: tuple[base.WeatherDescItem, ...]
    """Weather description in Kyrgyz, one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Kyrgyz."""

    lang_ky: tuple[base.WeatherDescItem, ...]
    """Weather description in Kyrgyz, one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.KY`."""
