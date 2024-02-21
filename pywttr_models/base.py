from __future__ import annotations

from typing import Tuple

from pydantic import Field

from ._pydantic import FrozenModel


class LangItem(FrozenModel):
    value: str


class WeatherDescItem(FrozenModel):
    value: str


class WeatherIconUrlItem(FrozenModel):
    value: str


class CurrentConditionItem(FrozenModel):
    feels_like_c: int = Field(alias="FeelsLikeC")
    feels_like_f: int = Field(alias="FeelsLikeF")
    cloudcover: int
    humidity: int
    local_obs_date_time: str = Field(alias="localObsDateTime")
    observation_time: str
    precip_inches: float = Field(alias="precipInches")
    precip_mm: float = Field(alias="precipMM")
    pressure: int
    pressure_inches: int = Field(alias="pressureInches")
    temp_c: int = Field(alias="temp_C")
    temp_f: int = Field(alias="temp_F")
    uv_index: int = Field(alias="uvIndex")
    visibility: int
    visibility_miles: int = Field(alias="visibilityMiles")
    weather_code: int = Field(alias="weatherCode")
    weather_desc: Tuple[WeatherDescItem, ...] = Field(alias="weatherDesc")
    weather_icon_url: Tuple[WeatherIconUrlItem, ...] = Field(
        alias="weatherIconUrl"
    )
    winddir16_point: str = Field(alias="winddir16Point")
    winddir_degree: int = Field(alias="winddirDegree")
    windspeed_kmph: int = Field(alias="windspeedKmph")
    windspeed_miles: int = Field(alias="windspeedMiles")


class AreaNameItem(FrozenModel):
    value: str


class CountryItem(FrozenModel):
    value: str


class RegionItem(FrozenModel):
    value: str


class WeatherUrlItem(FrozenModel):
    value: str


class NearestAreaItem(FrozenModel):
    area_name: Tuple[AreaNameItem, ...] = Field(alias="areaName")
    country: Tuple[CountryItem, ...]
    latitude: float
    longitude: float
    population: int
    region: Tuple[RegionItem, ...]
    weather_url: Tuple[WeatherUrlItem, ...] = Field(alias="weatherUrl")


class RequestItem(FrozenModel):
    query: str
    type: str


class AstronomyItem(FrozenModel):
    moon_illumination: int
    moon_phase: str
    moonrise: str
    moonset: str
    sunrise: str
    sunset: str


class WeatherDescItem1(FrozenModel):
    value: str


class WeatherIconUrlItem1(FrozenModel):
    value: str


class HourlyItem(FrozenModel):
    dew_point_c: int = Field(alias="DewPointC")
    dew_point_f: int = Field(alias="DewPointF")
    feels_like_c: int = Field(alias="FeelsLikeC")
    feels_like_f: int = Field(alias="FeelsLikeF")
    heat_index_c: int = Field(alias="HeatIndexC")
    heat_index_f: int = Field(alias="HeatIndexF")
    wind_chill_c: int = Field(alias="WindChillC")
    wind_chill_f: int = Field(alias="WindChillF")
    wind_gust_kmph: int = Field(alias="WindGustKmph")
    wind_gust_miles: int = Field(alias="WindGustMiles")
    chanceoffog: int
    chanceoffrost: int
    chanceofhightemp: int
    chanceofovercast: int
    chanceofrain: int
    chanceofremdry: int
    chanceofsnow: int
    chanceofsunshine: int
    chanceofthunder: int
    chanceofwindy: int
    cloudcover: int
    diff_rad: float = Field(alias="diffRad")
    humidity: int
    precip_inches: float = Field(alias="precipInches")
    precip_mm: float = Field(alias="precipMM")
    pressure: int
    pressure_inches: int = Field(alias="pressureInches")
    short_rad: float = Field(alias="shortRad")
    temp_c: int = Field(alias="tempC")
    temp_f: int = Field(alias="tempF")
    time: int
    uv_index: int = Field(alias="uvIndex")
    visibility: int
    visibility_miles: int = Field(alias="visibilityMiles")
    weather_code: int = Field(alias="weatherCode")
    weather_desc: Tuple[WeatherDescItem1, ...] = Field(alias="weatherDesc")
    weather_icon_url: Tuple[WeatherIconUrlItem1, ...] = Field(
        alias="weatherIconUrl"
    )
    winddir16_point: str = Field(alias="winddir16Point")
    winddir_degree: int = Field(alias="winddirDegree")
    windspeed_kmph: int = Field(alias="windspeedKmph")
    windspeed_miles: int = Field(alias="windspeedMiles")


class WeatherItem(FrozenModel):
    astronomy: Tuple[AstronomyItem, ...]
    avgtemp_c: int = Field(alias="avgtempC")
    avgtemp_f: int = Field(alias="avgtempF")
    date: str
    maxtemp_c: int = Field(alias="maxtempC")
    maxtemp_f: int = Field(alias="maxtempF")
    mintemp_c: int = Field(alias="mintempC")
    mintemp_f: int = Field(alias="mintempF")
    sun_hour: float = Field(alias="sunHour")
    total_snow_cm: float = Field(alias="totalSnow_cm")
    uv_index: int = Field(alias="uvIndex")


class Model(FrozenModel):
    nearest_area: Tuple[NearestAreaItem, ...]
    request: Tuple[RequestItem, ...]
