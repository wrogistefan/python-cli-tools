
# Python CLI Tools

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Tests](https://github.com/wrogistefan/python-cli-tools/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/wrogistefan/python-cli-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/wrogistefan/python-cli-tools)

A collection of small, well-tested command-line utilities implemented in Python. Each tool is self-contained, tested, and designed to be easy to run locally or install as a console command.

Key features
- Small, focused CLI tools: file organizer, password generator, and weather CLI
- Unit tests with `pytest`
- Simple packaging via `pyproject.toml` with console scripts

Contents
- [Usage examples](docs/usage_examples.md)
- Project structure and developer instructions below

## Quickstart

1. Clone the repository and create a virtual environment

```bash
git clone https://github.com/wrogistefan/python-cli-tools.git
cd python-cli-tools
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies (editable install registers console scripts)

```bash
pip install -r requirements.txt
pip install -e .
```

After installation you can run tools either as modules, or via the installed console scripts (recommended):

```bash
# module form
python -m file_organizer.file_organizer ./downloads

# console scripts (after `pip install -e .`)
file-organizer ./downloads
password-generator -l 16 --no-specials
weather-cli --city London

```

### Tools & Usage
1. File Organizer
    Organizes files into folders by extension.
    See file_organizer/file_organizer.py  
    or run:
    file-organizer <directory>



2. Password Generator
    Generates strong, customizable passwords.
    See password_generator/password_generator.py  
    or run:
    password-generator

3. Weather CLI (updated in v0.2.0)
    Fetches real-time weather data using Open-Meteo.

    Usage
    Run as a module:

    bash
    python -m weather_cli.weather_cli --city New York
    python -m weather_cli.weather_cli --lat 37.075 --lon 15.286

    See [docs/usage_examples.md](docs/usage_examples.md) for more detailed examples and expected output.

## Running Tests

Run the full test suite with:

```bash
pytest
```

## Packaging & Distribution

This project uses `pyproject.toml` + `setuptools`. Console script entry points are defined so installing the package provides the `file-organizer`, `password-generator`, and `weather-cli` commands.

To build a source/wheel distribution (requires `build`):

```bash
pip install build
python -m build
```

## Development notes

- Use the `docs/usage_examples.md` to expand runnable examples.


## Contributing

Contributions are welcome. Please:

1. Open an issue describing the change
2. Create a branch, add tests, and open a pull request

## CI

Add a simple GitHub Actions workflow to run `pytest` on push and PRs. Example workflow should run on `ubuntu-latest` with Python 3.10+.

## License

MIT — see the [LICENSE](LICENSE) file.

## Author

Łukasz Perek — project and code samples used for portfolio and learning.
This project showcases practical CLI tools and documents the transition into software development and AI freelancing.

