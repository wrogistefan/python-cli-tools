"""Tests for weather CLI"""
import pytest
from weather_cli.weather_cli import WeatherCLI

def test_weather_returns_string():
    cli = WeatherCLI("Siracusa")
    result = cli.get_weather()
    assert isinstance(result, str)

def test_weather_contains_city_name():
    city = "Rome"
    cli = WeatherCLI(city)
    result = cli.get_weather()
    assert city in result
