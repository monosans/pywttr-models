"""Response models for English."""

from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    """Current weather, described in English."""

    @property
    def lang_xx(self) -> tuple[base.WeatherDescItem, ...]:
        """Same as `weather_desc`."""
        return self.weather_desc

    @property
    def lang_en(self) -> tuple[base.WeatherDescItem, ...]:
        """Same as `weather_desc`."""
        return self.weather_desc


class HourlyItem(base.HourlyItem):
    """3-hour forecast, described in English."""

    @property
    def lang_xx(self) -> tuple[base.WeatherDescItem, ...]:
        """Same as `weather_desc`."""
        return self.weather_desc

    @property
    def lang_en(self) -> tuple[base.WeatherDescItem, ...]:
        """Same as `weather_desc`."""
        return self.weather_desc


Model = base.Model[CurrentConditionItem, HourlyItem]
"""Response for `Language.EN`."""
