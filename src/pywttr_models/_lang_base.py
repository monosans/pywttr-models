from __future__ import annotations

from pywttr_models import base


class CurrentConditionItem(base.CurrentConditionItem):
    lang_xx: tuple[base.WeatherDescItem, ...]
    """Weather description in the requested language, one item."""


class HourlyItem(base.HourlyItem):
    lang_xx: tuple[base.WeatherDescItem, ...]
    """Weather description in the requested language, one item."""


Model = base.Model
