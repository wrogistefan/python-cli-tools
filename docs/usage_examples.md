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

```
python -m weather_cli.weather_cli "New York"
# or
python weather_cli/weather_cli.py London
```
- **Example output**:

```
Weather in London: Sunny, 18°C
```

**Notes & Next Steps**
- All three tools expose a `main()` and can be run as modules (`python -m <package>.<module>`).
- To adapt `weather_cli` to a real API, add an API client and expose an environment variable for the API key.
- To integrate examples into the project README, copy relevant snippets from this file into README.md.
