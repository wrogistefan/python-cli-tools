# Usage Examples

**Project Usage Examples**

- **Install**: Create and activate a virtual environment, then install dependencies.

```
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```

- **Run tests**: `pytest`

**File Organizer**
- **File**: [file_organizer/file_organizer.py](file_organizer/file_organizer.py)
- **Purpose**: Organize files in a directory into subfolders by extension.
- **Command**:

```
# organize files in ./downloads
python -m file_organizer.file_organizer ./downloads
# or
python file_organizer/file_organizer.py ./downloads
```
- **Example output**:

```
Moved: report.pdf -> ./downloads/pdf
Moved: photo.jpg -> ./downloads/jpg
Moved: README -> ./downloads/no_extension
```

**Password Generator**
- **File**: [password_generator/password_generator.py](password_generator/password_generator.py)
- **Purpose**: Generate a random strong password.
- **Command**:

```
# default (12 chars)
python -m password_generator.password_generator
# custom length and options
python -m password_generator.password_generator -l 16 --no-specials
```
- **Example output**:

```
k9F3nAq2Zo1LmV7$
```

**Weather CLI**
- **File**: [weather_cli/weather_cli.py](weather_cli/weather_cli.py)
- **Purpose**: Print a short weather summary for a city (currently mocked).
- **Command**:
## Weather CLI — Usage

The Weather CLI supports two ways of specifying a location:

- by city name (`--city`)
- by geographic coordinates (`--lat` + `--lon`)

### Run as a module

```bash
python -m weather_cli.weather_cli --city New York
python -m weather_cli.weather_cli --lat 37.075 --lon 15.286

- **Example output**:

📍 Location: Syracuse, Italy (37.07542, 15.28664)

🌤️  Current Weather:
   🌡️  Temperature: 12.9°C
   💨  Wind Speed: 2.5 km/h
   🧭  Wind Direction: 270°
   ⏱️  Observation Time: 2025-12-25T17:45


**Notes & Next Steps**
- All three tools expose a `main()` and can be run as modules (`python -m <package>.<module>`).

- To integrate examples into the project README, copy relevant snippets from this file into README.md.
