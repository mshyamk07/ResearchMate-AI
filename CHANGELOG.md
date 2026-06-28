# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**, and this project follows Semantic Versioning principles where applicable.

---

## [0.1.0] - Day 2 - Milestone 1

### Added

* Initial GitHub repository setup.
* Python virtual environment (`.venv`).
* FastAPI backend.
* Uvicorn development server.
* Root API endpoint (`/`).
* Automatic Swagger/OpenAPI documentation (`/docs`).
* Project documentation (`README.md`, `PROJECT_JOURNAL.md`).
* Dependency management using `requirements.txt`.
* Git ignore rules for Python cache and virtual environment.

### Changed

* Converted the root API endpoint from synchronous (`def`) to asynchronous (`async def`) for improved scalability.

### Fixed

* Corrected GitHub repository naming.
* Resolved Git authentication conflict caused by cached credentials from another GitHub account.
* Excluded `__pycache__` from version control using `.gitignore`.

---

## Upcoming

### Milestone 2

* PDF upload endpoint
* File validation
* PDF storage
* Initial document processing pipeline
