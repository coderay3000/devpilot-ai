# DevPilot AI – Learning Log

## Session 1 – 2026-11-05 – Environment setup


### Files implemented
- `.gitignore` (Python template + own block), `.env.example`, `requirements.txt`
- `app/__init__.py`, `app/core/__init__.py`, `tests/.gitkeep`, `docs/.gitkeep`
- Created by GitHub (not by me): `README.md`, `LICENSE`

### What I implemented
- Created the GitHub repo, cloned it, opened it in VS Code
- Created `.venv`, activated it, selected it as the interpreter
- Created the base folder structure and ignore rules
- Created `.env` (local, ignored) and `.env.example` (committed)
- Installed `pydantic-settings==2.16.2` and pinned it
- First commit and push to `main`


### Bugs encountered / fixed
- Ran a placeholder path (`cd path/to/devpilot-ai`) literally; I was already in the right folder
- `venv\Scripts\Activate` failed because the folder is `.venv` (missing the dot); fixed with the correct name
- `SyntaxError: '(' was never closed` from an extra bracket in `python -c`; fixed by balancing brackets


### Next task
- Phase 1: write the requirements document (MVP scope, non-goals, 5 example user questions)