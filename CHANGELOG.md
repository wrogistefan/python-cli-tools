

# Changelog

All notable changes to this project will be documented in this file.

## [0.2.1] - 2025-01-XX
### Fixed
- Resolved compatibility issue with Python 3.12 causing `weather-cli` to fail due to outdated `requests` dependency.
- Ensured correct dependency resolution when installing from TestPyPI and PyPI.

### Added
- Explicit `requests>=2.31.0` dependency in `pyproject.toml` to guarantee compatibility with Python 3.12+.
- Improved reliability of `weather-cli` by enforcing modern HTTP stack.

### Changed
- Updated packaging metadata to ensure consistent installation behavior across environments.
- Minor internal cleanup in preparation for future CLI additions.

### Notes
- This release is a maintenance update focused on stability and compatibility.
- No breaking changes introduced.

## [0.2.0] — 2025-12-25
### Added
- Weather CLI now performs real HTTP requests using Open-Meteo
- Added live weather output formatting
- Updated README to reflect real Weather CLI functionality

### Fixed
- Corrected usage examples for Weather CLI
- Improved documentation consistency

### Changed
- Bumped project version to 0.2.0

---

## [0.1.0] — Initial Release
### Added
- File Organizer CLI
- Password Generator CLI
- Weather CLI (mocked version)
- Project structure, tests, packaging, and documentation
