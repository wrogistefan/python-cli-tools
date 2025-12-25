import argparse
import pytest
import requests
from unittest.mock import patch, MagicMock

import weather_cli.weather_cli as weather_cli


# -----------------------------
# Geocoding tests
# -----------------------------

def test_geocode_city_success():
    mock_response = {
        "results": [
            {
                "latitude": 52.52,
                "longitude": 13.41,
                "name": "Berlin",
                "country": "Germany"
            }
        ]
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )

        lat, lon, name, country = weather_cli.geocode_city("Berlin")

        assert lat == 52.52
        assert lon == 13.41
        assert name == "Berlin"
        assert country == "Germany"


def test_geocode_city_not_found():
    mock_response = {"results": []}

    with patch("requests.get") as mock_get, pytest.raises(SystemExit):
        mock_get.return_value = MagicMock(
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )
        weather_cli.geocode_city("Atlantis")


def test_geocode_city_api_error():
    with patch("requests.get") as mock_get, pytest.raises(SystemExit):
        mock_get.side_effect = requests.exceptions.RequestException("API error")
        weather_cli.geocode_city("Berlin")


# -----------------------------
# Weather fetch tests
# -----------------------------

def test_fetch_weather_success():
    mock_response = {
        "current_weather": {
            "temperature": 10.5,
            "windspeed": 5.2,
            "winddirection": 180,
            "time": "2025-12-21T12:00"
        }
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )

        data = weather_cli.fetch_weather(52.52, 13.41)

        assert "current_weather" in data
        assert data["current_weather"]["temperature"] == 10.5


def test_fetch_weather_api_error():
    with patch("requests.get") as mock_get, pytest.raises(SystemExit):
        mock_get.side_effect = requests.exceptions.RequestException("API error")
        weather_cli.fetch_weather(52.52, 13.41)


# -----------------------------
# CLI tests (high-level)
# -----------------------------

def test_cli_city_success(capsys):
    """Simulate running: weather --city Berlin"""

    geocode_mock = (52.52, 13.41, "Berlin", "Germany")
    weather_mock = {
        "current_weather": {
            "temperature": 10,
            "windspeed": 5,
            "winddirection": 200,
            "time": "2025-12-21T12:00"
        }
    }

    with patch("weather_cli.weather_cli.geocode_city", return_value=geocode_mock), \
         patch("weather_cli.weather_cli.fetch_weather", return_value=weather_mock), \
         patch("argparse.ArgumentParser.parse_args",
               return_value=argparse.Namespace(city="Berlin", lat=None, lon=None)):

        weather_cli.main()
        captured = capsys.readouterr()

        assert "Berlin" in captured.out
        assert "Temperature" in captured.out


def test_cli_missing_arguments(capsys):
    """Simulate running without --city or --lat/--lon"""

    with patch("argparse.ArgumentParser.parse_args",
               return_value=argparse.Namespace(city=None, lat=None, lon=None)), \
         pytest.raises(SystemExit):

        weather_cli.main()

        captured = capsys.readouterr()
        assert "Provide --city" in captured.out
