# -*- coding: utf-8 -*-
from typing import List as _List

from pywttr_models import base as _base


class CurrentConditionItem(_base.CurrentConditionItem):
    lang_ca: _List[_base.LangItem]


class HourlyItem(_base.HourlyItem):
    lang_ca: _List[_base.LangItem]


class WeatherItem(_base.WeatherItem):
    hourly: _List[HourlyItem]


class Model(_base.Model):
    current_condition: _List[CurrentConditionItem]
    weather: _List[WeatherItem]
