"""Weather CLI - Fetch weather forecast from terminal."""

import argparse


class WeatherCLI:
    def __init__(self, city: str):
        self.city = city

    def get_weather(self) -> str:
        # Currently returns mocked data; replace with a real API client
        return f"Weather in {self.city}: Sunny, 18°C"


def main() -> None:
    parser = argparse.ArgumentParser(description="Check weather for a city.")
    parser.add_argument("city", help="City name")
    args = parser.parse_args()

    cli = WeatherCLI(args.city)
    print(cli.get_weather())


if __name__ == "__main__":
    main()
