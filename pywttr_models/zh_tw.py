# -*- coding: utf-8 -*-
from typing import List as _List

from pydantic import Field as _Field

from pywttr_models import base as _base


class CurrentConditionItem(_base.CurrentConditionItem):
    lang_zh_tw: _List[_base.LangItem] = _Field(..., alias="lang_zh-tw")


class HourlyItem(_base.HourlyItem):
    lang_zh_tw: _List[_base.LangItem] = _Field(..., alias="lang_zh-tw")


class WeatherItem(_base.WeatherItem):
    hourly: _List[HourlyItem]


class Model(_base.Model):
    current_condition: _List[CurrentConditionItem]
    weather: _List[WeatherItem]
