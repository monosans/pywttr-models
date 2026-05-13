from __future__ import annotations

from pywttr_models import _lang_base, base


class CurrentConditionItem(_lang_base.CurrentConditionItem):
    @property
    def lang_id(self) -> tuple[base.WeatherDescItem, ...]:
        return self.lang_xx


class HourlyItem(_lang_base.HourlyItem):
    @property
    def lang_id(self) -> tuple[base.WeatherDescItem, ...]:
        return self.lang_xx


Model = _lang_base.Model[CurrentConditionItem, HourlyItem]
