from __future__ import annotations

from typing import List

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:  # pragma: no cover
    from pydantic import BaseModel, Field  # type: ignore[assignment]


class LangItem(BaseModel):
    value: str


class WeatherDescItem(BaseModel):
    value: str


class WeatherIconUrlItem(BaseModel):
    value: str


class CurrentConditionItem(BaseModel):
    feels_like_c: str = Field(alias="FeelsLikeC")
    feels_like_f: str = Field(alias="FeelsLikeF")
    cloudcover: str
    humidity: str
    local_obs_date_time: str = Field(alias="localObsDateTime")
    observation_time: str
    precip_inches: str = Field(alias="precipInches")
    precip_mm: str = Field(alias="precipMM")
    pressure: str
    pressure_inches: str = Field(alias="pressureInches")
    temp_c: str = Field(alias="temp_C")
    temp_f: str = Field(alias="temp_F")
    uv_index: str = Field(alias="uvIndex")
    visibility: str
    visibility_miles: str = Field(alias="visibilityMiles")
    weather_code: str = Field(alias="weatherCode")
    weather_desc: List[WeatherDescItem] = Field(alias="weatherDesc")
    weather_icon_url: List[WeatherIconUrlItem] = Field(alias="weatherIconUrl")
    winddir16_point: str = Field(alias="winddir16Point")
    winddir_degree: str = Field(alias="winddirDegree")
    windspeed_kmph: str = Field(alias="windspeedKmph")
    windspeed_miles: str = Field(alias="windspeedMiles")


class AreaNameItem(BaseModel):
    value: str


class CountryItem(BaseModel):
    value: str


class RegionItem(BaseModel):
    value: str


class WeatherUrlItem(BaseModel):
    value: str


class NearestAreaItem(BaseModel):
    area_name: List[AreaNameItem] = Field(alias="areaName")
    country: List[CountryItem]
    latitude: str
    longitude: str
    population: str
    region: List[RegionItem]
    weather_url: List[WeatherUrlItem] = Field(alias="weatherUrl")


class RequestItem(BaseModel):
    query: str
    type: str


class AstronomyItem(BaseModel):
    moon_illumination: str
    moon_phase: str
    moonrise: str
    moonset: str
    sunrise: str
    sunset: str


class WeatherDescItem1(BaseModel):
    value: str


class WeatherIconUrlItem1(BaseModel):
    value: str


class HourlyItem(BaseModel):
    dew_point_c: str = Field(alias="DewPointC")
    dew_point_f: str = Field(alias="DewPointF")
    feels_like_c: str = Field(alias="FeelsLikeC")
    feels_like_f: str = Field(alias="FeelsLikeF")
    heat_index_c: str = Field(alias="HeatIndexC")
    heat_index_f: str = Field(alias="HeatIndexF")
    wind_chill_c: str = Field(alias="WindChillC")
    wind_chill_f: str = Field(alias="WindChillF")
    wind_gust_kmph: str = Field(alias="WindGustKmph")
    wind_gust_miles: str = Field(alias="WindGustMiles")
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
    precip_inches: str = Field(alias="precipInches")
    precip_mm: str = Field(alias="precipMM")
    pressure: str
    pressure_inches: str = Field(alias="pressureInches")
    temp_c: str = Field(alias="tempC")
    temp_f: str = Field(alias="tempF")
    time: str
    uv_index: str = Field(alias="uvIndex")
    visibility: str
    visibility_miles: str = Field(alias="visibilityMiles")
    weather_code: str = Field(alias="weatherCode")
    weather_desc: List[WeatherDescItem1] = Field(alias="weatherDesc")
    weather_icon_url: List[WeatherIconUrlItem1] = Field(alias="weatherIconUrl")
    winddir16_point: str = Field(alias="winddir16Point")
    winddir_degree: str = Field(alias="winddirDegree")
    windspeed_kmph: str = Field(alias="windspeedKmph")
    windspeed_miles: str = Field(alias="windspeedMiles")


class WeatherItem(BaseModel):
    astronomy: List[AstronomyItem]
    avgtemp_c: str = Field(alias="avgtempC")
    avgtemp_f: str = Field(alias="avgtempF")
    date: str
    maxtemp_c: str = Field(alias="maxtempC")
    maxtemp_f: str = Field(alias="maxtempF")
    mintemp_c: str = Field(alias="mintempC")
    mintemp_f: str = Field(alias="mintempF")
    sun_hour: str = Field(alias="sunHour")
    total_snow_cm: str = Field(alias="totalSnow_cm")
    uv_index: str = Field(alias="uvIndex")


class Model(BaseModel):
    nearest_area: List[NearestAreaItem]
    request: List[RequestItem]
