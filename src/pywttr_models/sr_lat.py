"""Response models for Serbian (Latin script)."""

from __future__ import annotations

from pydantic import Field

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    """Current weather, described in Serbian (Latin script)."""

    lang_sr_lat: tuple[base.WeatherDescItem, ...] = Field(alias="lang_sr-lat")
    """Weather description in Serbian (Latin script), one item."""


class HourlyItem(_lang_base.HourlyItem):
    """3-hour forecast, described in Serbian (Latin script)."""

    lang_sr_lat: tuple[base.WeatherDescItem, ...] = Field(alias="lang_sr-lat")
    """Weather description in Serbian (Latin script), one item."""


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.SR_LAT`."""
