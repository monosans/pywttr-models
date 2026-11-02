"""Response models shared by all languages."""

from __future__ import annotations

import sys
from typing import Generic

from pydantic import Field

from pywttr_models._pydantic import FrozenModel

if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar


class WeatherDescItem(FrozenModel):
    """Weather description, e.g. `Sunny`."""

    value: str


LangItem = WeatherDescItem
"""Alias of `WeatherDescItem`."""


class WeatherIconUrlItem(FrozenModel):
    """URL of a weather icon."""

    value: str


class CurrentConditionItem(FrozenModel):
    """Current weather."""

    feels_like_c: int = Field(alias="FeelsLikeC")
    """Feels-like temperature, °C."""
    feels_like_f: int = Field(alias="FeelsLikeF")
    """Feels-like temperature, °F."""
    cloudcover: int
    """Cloud cover, %."""
    humidity: int
    """Relative humidity, %."""
    observation_time: str
    """Observation time in UTC, e.g. `04:33 AM`."""
    precip_inches: float = Field(alias="precipInches")
    """Precipitation, inches."""
    precip_mm: float = Field(alias="precipMM")
    """Precipitation, mm."""
    pressure: int
    """Atmospheric pressure, hPa."""
    pressure_inches: int = Field(alias="pressureInches")
    """Atmospheric pressure, inHg."""
    temp_c: int = Field(alias="temp_C")
    """Temperature, °C."""
    temp_f: int = Field(alias="temp_F")
    """Temperature, °F."""
    uv_index: int = Field(alias="uvIndex")
    """UV index."""
    visibility: int
    """Visibility, km."""
    visibility_miles: int = Field(alias="visibilityMiles")
    """Visibility, miles."""
    weather_code: int = Field(alias="weatherCode")
    """WorldWeatherOnline condition code, e.g. `113` for clear sky."""
    weather_desc: tuple[WeatherDescItem, ...] = Field(alias="weatherDesc")
    """Weather description in English, one item."""
    weather_icon_url: tuple[WeatherIconUrlItem, ...] = Field(alias="weatherIconUrl")
    """Weather icon, one item."""
    winddir16_point: str = Field(alias="winddir16Point")
    """Wind direction on a 16-point compass, e.g. `SSW`."""
    winddir_degree: int = Field(alias="winddirDegree")
    """Wind direction, degrees."""
    windspeed_kmph: int = Field(alias="windspeedKmph")
    """Wind speed, km/h."""
    windspeed_miles: int = Field(alias="windspeedMiles")
    """Wind speed, mph."""


class AreaNameItem(FrozenModel):
    """Area name, e.g. `Saint-Merri`."""

    value: str


class CountryItem(FrozenModel):
    """Country name, e.g. `France`."""

    value: str


class RegionItem(FrozenModel):
    """Region name, e.g. `Ile-de-France`."""

    value: str


class WeatherUrlItem(FrozenModel):
    """URL of the area's forecast on WorldWeatherOnline."""

    value: str


class NearestAreaItem(FrozenModel):
    """The area nearest to the requested location."""

    area_name: tuple[AreaNameItem, ...] = Field(alias="areaName")
    """Area name, one item."""
    country: tuple[CountryItem, ...]
    """Country, one item."""
    latitude: float
    """Latitude, degrees."""
    longitude: float
    """Longitude, degrees."""
    population: int
    """Population, `0` if unknown."""
    region: tuple[RegionItem, ...]
    """Region, one item."""
    weather_url: tuple[WeatherUrlItem, ...] = Field(alias="weatherUrl")
    """Forecast page on WorldWeatherOnline, one item."""


class RequestItem(FrozenModel):
    """How wttr.in understood the location."""

    query: str
    """Resolved location, e.g. `Lat 48.86 and Lon 2.35`."""
    type: str
    """Query type, e.g. `LatLon`."""


class AstronomyItem(FrozenModel):
    """Sun and moon for a day."""

    moon_illumination: int
    """Moon illumination, %."""
    moon_phase: str
    """Moon phase, e.g. `Waxing Crescent`."""
    moonrise: str
    """Moonrise, local time, e.g. `01:47 PM`."""
    moonset: str
    """Moonset, local time, e.g. `09:03 PM`."""
    sunrise: str
    """Sunrise, local time, e.g. `08:11 AM`."""
    sunset: str
    """Sunset, local time, e.g. `07:01 PM`."""


class HourlyItem(FrozenModel):
    """Forecast for a 3-hour slot."""

    dew_point_c: int = Field(alias="DewPointC")
    """Dew point, °C."""
    dew_point_f: int = Field(alias="DewPointF")
    """Dew point, °F."""
    feels_like_c: int = Field(alias="FeelsLikeC")
    """Feels-like temperature, °C."""
    feels_like_f: int = Field(alias="FeelsLikeF")
    """Feels-like temperature, °F."""
    heat_index_c: int = Field(alias="HeatIndexC")
    """Heat index, °C."""
    heat_index_f: int = Field(alias="HeatIndexF")
    """Heat index, °F."""
    wind_chill_c: int = Field(alias="WindChillC")
    """Wind chill, °C."""
    wind_chill_f: int = Field(alias="WindChillF")
    """Wind chill, °F."""
    wind_gust_kmph: int = Field(alias="WindGustKmph")
    """Wind gusts, km/h."""
    wind_gust_miles: int = Field(alias="WindGustMiles")
    """Wind gusts, mph."""
    chanceoffog: int
    """Chance of fog, %."""
    chanceoffrost: int
    """Chance of frost, %."""
    chanceofhightemp: int
    """Chance of high temperature, %."""
    chanceofovercast: int
    """Chance of overcast, %."""
    chanceofrain: int
    """Chance of rain, %."""
    chanceofremdry: int
    """Chance of staying dry, %."""
    chanceofsnow: int
    """Chance of snow, %."""
    chanceofsunshine: int
    """Chance of sunshine, %."""
    chanceofthunder: int
    """Chance of thunder, %."""
    chanceofwindy: int
    """Chance of wind, %."""
    cloudcover: int
    """Cloud cover, %."""
    diff_rad: float = Field(alias="diffRad")
    """Diffuse solar radiation, W/m²."""
    humidity: int
    """Relative humidity, %."""
    precip_inches: float = Field(alias="precipInches")
    """Precipitation, inches."""
    precip_mm: float = Field(alias="precipMM")
    """Precipitation, mm."""
    pressure: int
    """Atmospheric pressure, hPa."""
    pressure_inches: int = Field(alias="pressureInches")
    """Atmospheric pressure, inHg."""
    short_rad: float = Field(alias="shortRad")
    """Shortwave solar radiation, W/m²."""
    temp_c: int = Field(alias="tempC")
    """Temperature, °C."""
    temp_f: int = Field(alias="tempF")
    """Temperature, °F."""
    time: int
    """Local start time, `HHMM` as a number: `0`, `300`, ..., `2100`."""
    uv_index: int = Field(alias="uvIndex")
    """UV index."""
    visibility: int
    """Visibility, km."""
    visibility_miles: int = Field(alias="visibilityMiles")
    """Visibility, miles."""
    weather_code: int = Field(alias="weatherCode")
    """WorldWeatherOnline condition code, e.g. `113` for clear sky."""
    weather_desc: tuple[WeatherDescItem, ...] = Field(alias="weatherDesc")
    """Weather description in English, one item."""
    weather_icon_url: tuple[WeatherIconUrlItem, ...] = Field(alias="weatherIconUrl")
    """Weather icon, one item."""
    winddir16_point: str = Field(alias="winddir16Point")
    """Wind direction on a 16-point compass, e.g. `SSW`."""
    winddir_degree: int = Field(alias="winddirDegree")
    """Wind direction, degrees."""
    windspeed_kmph: int = Field(alias="windspeedKmph")
    """Wind speed, km/h."""
    windspeed_miles: int = Field(alias="windspeedMiles")
    """Wind speed, mph."""


_THourlyItem = TypeVar("_THourlyItem", bound="HourlyItem")


class WeatherItem(FrozenModel, Generic[_THourlyItem]):
    """Forecast for a day."""

    astronomy: tuple[AstronomyItem, ...]
    """Sun and moon, one item."""
    avgtemp_c: int = Field(alias="avgtempC")
    """Average temperature, °C."""
    avgtemp_f: int = Field(alias="avgtempF")
    """Average temperature, °F."""
    date: str
    """Local date, e.g. `2026-10-15`."""
    hourly: tuple[_THourlyItem, ...]
    """Forecast for every 3 hours, from 00:00 to 21:00 local time."""
    maxtemp_c: int = Field(alias="maxtempC")
    """Maximum temperature, °C."""
    maxtemp_f: int = Field(alias="maxtempF")
    """Maximum temperature, °F."""
    mintemp_c: int = Field(alias="mintempC")
    """Minimum temperature, °C."""
    mintemp_f: int = Field(alias="mintempF")
    """Minimum temperature, °F."""
    sun_hour: float = Field(alias="sunHour")
    """Hours of sunshine."""
    total_snow_cm: float = Field(alias="totalSnow_cm")
    """Snowfall, cm."""
    uv_index: int = Field(alias="uvIndex")
    """UV index."""


_TCurrentConditionItem = TypeVar("_TCurrentConditionItem", bound="CurrentConditionItem")


class Model(FrozenModel, Generic[_TCurrentConditionItem, _THourlyItem]):
    """Weather at a location: now and for 3 days."""

    current_condition: tuple[_TCurrentConditionItem, ...]
    """Current weather, one item."""
    nearest_area: tuple[NearestAreaItem, ...]
    """The area nearest to the location, one item."""
    request: tuple[RequestItem, ...]
    """How wttr.in understood the location, one item."""
    weather: tuple[WeatherItem[_THourlyItem], ...]
    """Forecast for today, tomorrow and the day after."""
