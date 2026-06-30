# ResearchMate AI

## Day 1

Project started.

Goal:
Build an Agentic AI platform that helps researchers analyze papers,
compare methodologies, generate literature reviews, and suggest
potential research opportunities.

Status:
- Project idea finalized
- Development environment prepared
- Git installed
- Python installed
- VS Code configured

Next:
Initialize Git repository and create project architecture.



## Day 2 – Milestone 1 Complete

Objective

Set up the complete development environment and build the first working backend for ResearchMate AI.

Tasks Completed
1. Git & GitHub Setup
Configured Git globally with username and email.
Initialized the local Git repository.
Connected the project to the GitHub remote repository.
Resolved repository naming issues.
Fixed Git authentication conflict caused by cached credentials from another GitHub account.
Successfully pushed the project to GitHub.
2. Project Structure

Created the initial project structure with:

backend/
README.md
LICENSE
PROJECT_JOURNAL.md
requirements.txt
.gitignore
3. Python Environment
Created a Python virtual environment (.venv).
Activated the virtual environment.
Verified isolated package installation.
4. Backend Setup

Installed:

FastAPI
Uvicorn

Generated requirements.txt using:

pip freeze > requirements.txt

5. First Backend Application

Created the first FastAPI application.

Implemented:

Application metadata
Root endpoint (/)
JSON response
Automatic Swagger documentation

Converted the API endpoint from synchronous to asynchronous:

async def root()

to follow modern FastAPI development practices.

6. API Testing

Successfully started the backend server using:

uvicorn backend.main --reload

Verified:

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Both endpoints worked successfully.

7. Git Workflow

Performed the second project commit.

Commit message:

Setup FastAPI backend

Successfully pushed the commit to GitHub.

Challenges Faced
Repository Name Typo

Initially created the repository with an incorrect name.

Solution:
Renamed the repository on GitHub and updated the remote URL.

Authentication Error (403)

Git attempted to authenticate using cached credentials from another GitHub account.

Solution:
Removed the old GitHub credentials from Windows Credential Manager and authenticated using the correct account.

Python Cache

Observed the automatically generated pycache folder.

Solution:
Updated .gitignore to exclude Python cache files from version control.

Knowledge Gained

During this milestone I learned:

Git basics
GitHub repository management
Remote repositories
Virtual environments
Python package management
FastAPI fundamentals
Uvicorn server
REST API basics
Swagger/OpenAPI documentation
Async API endpoints
Professional Git commit workflow
Current Project Status

Milestone 1 completed successfully.

Working Features:

GitHub repository
FastAPI backend
REST API
Swagger documentation
Virtual environment
Dependency management
Next Milestone

Milestone 2: Document Processing Engine

Objectives:

Build PDF Upload API
Validate uploaded files
Store research papers
Prepare the backend for PDF text extraction
Personal Reflection

Today marked the transition from project planning to actual software development. The backend is operational, version control is fully configured, and the development workflow is established. Resolving Git authentication and repository issues provided practical experience with real-world development challenges. This milestone creates a strong foundation for implementing AI-powered document processing in the upcoming phases.

# Day 3 - Document Ingestion Pipeline

## Goals
- Build a PDF upload endpoint
- Save uploaded PDFs
- Extract text using PyMuPDF
- Extract metadata
- Improve backend architecture

## Completed
- Created Upload API
- Added PDF validation
- Saved uploaded PDFs to backend/uploads
- Generated UUID-based filenames
- Extracted full PDF text
- Extracted metadata (title, DOI, publication date, abstract)
- Added Pydantic response model
- Refactored business logic into PDFService
- Implemented MetadataService

## Challenges
- Fixed circular import issue
- Corrected project folder structure
- Learned FastAPI response models
- Refactored code for better maintainability

## Status
Document ingestion pipeline is complete and tested.
Ready to start AI pipeline.