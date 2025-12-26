

# Changelog

All notable changes to this project will be documented in this file.

## v0.2.6 — 2025-12-26
🔐 GPG Signature Verified  
This release confirms full GPG signing integration using key 9EC4ECA6A8A65C76. Tag test-gpg is cryptographically verified and recognized by GitHub.

🛠️ Secure Publish Workflow Finalized  
The publish.yml workflow now enforces GPG tag verification before triggering PyPI deployment. Only signed tags from the verified keyholder can initiate releases.

📦 Metadata and Badge Block Polished  
README badges for PyPI, tests, publish status, and license are finalized. All links and labels are stable and production-ready.

🧾 CHANGELOG and Versioning Synced  
Version v0.2.6 supersedes v0.2.5 for internal consistency. All release artifacts are aligned with signed tag and verified commit

## 0.2.3 — 2025-12-26

### Added
- First official PyPI release of python-cli-tools.
- Automated publishing workflow using GitHub Actions.
- Improved project structure with PEP 621 compliant pyproject.toml.

### Fixed
- Removed legacy metadata issues related to TestPyPI incompatibility.
- Ensured clean build process and reproducible packaging.

### Notes
- TestPyPI is no longer used due to outdated metadata validation.


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
