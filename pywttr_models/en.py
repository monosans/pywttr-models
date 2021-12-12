# -*- coding: utf-8 -*-
from typing import List as _List

from pywttr_models import base as _base


class WeatherItem(_base.WeatherItem):
    hourly: _List[_base.HourlyItem]


class Model(_base.Model):
    current_condition: _List[_base.CurrentConditionItem]
    weather: _List[WeatherItem]
