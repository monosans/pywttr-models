from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    @property
    def lang_xx(self) -> tuple[base.WeatherDescItem, ...]:
        return self.weather_desc

    @property
    def lang_en(self) -> tuple[base.WeatherDescItem, ...]:
        return self.weather_desc


class HourlyItem(base.HourlyItem):
    @property
    def lang_xx(self) -> tuple[base.WeatherDescItem, ...]:
        return self.weather_desc

    @property
    def lang_en(self) -> tuple[base.WeatherDescItem, ...]:
        return self.weather_desc


Model = base.Model[CurrentConditionItem, HourlyItem]
