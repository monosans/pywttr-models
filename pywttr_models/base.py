# -*- coding: utf-8 -*-
from typing import List as _List

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field


class LangItem(_BaseModel):
    value: str


class WeatherDescItem(_BaseModel):
    value: str


class WeatherIconUrlItem(_BaseModel):
    value: str


class CurrentConditionItem(_BaseModel):
    feels_like_c: str = _Field(..., alias="FeelsLikeC")
    feels_like_f: str = _Field(..., alias="FeelsLikeF")
    cloudcover: str
    humidity: str
    local_obs_date_time: str = _Field(..., alias="localObsDateTime")
    observation_time: str
    precip_inches: str = _Field(..., alias="precipInches")
    precip_mm: str = _Field(..., alias="precipMM")
    pressure: str
    pressure_inches: str = _Field(..., alias="pressureInches")
    temp_c: str = _Field(..., alias="temp_C")
    temp_f: str = _Field(..., alias="temp_F")
    uv_index: str = _Field(..., alias="uvIndex")
    visibility: str
    visibility_miles: str = _Field(..., alias="visibilityMiles")
    weather_code: str = _Field(..., alias="weatherCode")
    weather_desc: _List[WeatherDescItem] = _Field(..., alias="weatherDesc")
    weather_icon_url: _List[WeatherIconUrlItem] = _Field(
        ..., alias="weatherIconUrl"
    )
    winddir16_point: str = _Field(..., alias="winddir16Point")
    winddir_degree: str = _Field(..., alias="winddirDegree")
    windspeed_kmph: str = _Field(..., alias="windspeedKmph")
    windspeed_miles: str = _Field(..., alias="windspeedMiles")


class AreaNameItem(_BaseModel):
    value: str


class CountryItem(_BaseModel):
    value: str


class RegionItem(_BaseModel):
    value: str


class WeatherUrlItem(_BaseModel):
    value: str


class NearestAreaItem(_BaseModel):
    area_name: _List[AreaNameItem] = _Field(..., alias="areaName")
    country: _List[CountryItem]
    latitude: str
    longitude: str
    population: str
    region: _List[RegionItem]
    weather_url: _List[WeatherUrlItem] = _Field(..., alias="weatherUrl")


class RequestItem(_BaseModel):
    query: str
    type: str


class AstronomyItem(_BaseModel):
    moon_illumination: str
    moon_phase: str
    moonrise: str
    moonset: str
    sunrise: str
    sunset: str


class WeatherDescItem1(_BaseModel):
    value: str


class WeatherIconUrlItem1(_BaseModel):
    value: str


class HourlyItem(_BaseModel):
    dew_point_c: str = _Field(..., alias="DewPointC")
    dew_point_f: str = _Field(..., alias="DewPointF")
    feels_like_c: str = _Field(..., alias="FeelsLikeC")
    feels_like_f: str = _Field(..., alias="FeelsLikeF")
    heat_index_c: str = _Field(..., alias="HeatIndexC")
    heat_index_f: str = _Field(..., alias="HeatIndexF")
    wind_chill_c: str = _Field(..., alias="WindChillC")
    wind_chill_f: str = _Field(..., alias="WindChillF")
    wind_gust_kmph: str = _Field(..., alias="WindGustKmph")
    wind_gust_miles: str = _Field(..., alias="WindGustMiles")
    chanceoffog: str
    chanceoffrost: str
    chanceofhightemp: str
    chanceofovercast: str
    chanceofrain: str
    chanceofremdry: str
    chanceofsnow: str
    chanceofsunshine: str
    chanceofthunder: str
    chanceofwindy: str
    cloudcover: str
    humidity: str
    precip_inches: str = _Field(..., alias="precipInches")
    precip_mm: str = _Field(..., alias="precipMM")
    pressure: str
    pressure_inches: str = _Field(..., alias="pressureInches")
    temp_c: str = _Field(..., alias="tempC")
    temp_f: str = _Field(..., alias="tempF")
    time: str
    uv_index: str = _Field(..., alias="uvIndex")
    visibility: str
    visibility_miles: str = _Field(..., alias="visibilityMiles")
    weather_code: str = _Field(..., alias="weatherCode")
    weather_desc: _List[WeatherDescItem1] = _Field(..., alias="weatherDesc")
    weather_icon_url: _List[WeatherIconUrlItem1] = _Field(
        ..., alias="weatherIconUrl"
    )
    winddir16_point: str = _Field(..., alias="winddir16Point")
    winddir_degree: str = _Field(..., alias="winddirDegree")
    windspeed_kmph: str = _Field(..., alias="windspeedKmph")
    windspeed_miles: str = _Field(..., alias="windspeedMiles")


class WeatherItem(_BaseModel):
    astronomy: _List[AstronomyItem]
    avgtemp_c: str = _Field(..., alias="avgtempC")
    avgtemp_f: str = _Field(..., alias="avgtempF")
    date: str
    maxtemp_c: str = _Field(..., alias="maxtempC")
    maxtemp_f: str = _Field(..., alias="maxtempF")
    mintemp_c: str = _Field(..., alias="mintempC")
    mintemp_f: str = _Field(..., alias="mintempF")
    sun_hour: str = _Field(..., alias="sunHour")
    total_snow_cm: str = _Field(..., alias="totalSnow_cm")
    uv_index: str = _Field(..., alias="uvIndex")


class Model(_BaseModel):
    nearest_area: _List[NearestAreaItem]
    request: _List[RequestItem]
