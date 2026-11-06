# DevPilot AI – Project Guide

## 1. Objective
A repository-aware coding assistant. The user pastes a public GitHub
repository URL and asks questions in chat. Answers are built from the
real code and cite file paths and line ranges.

## 2. MVP scope
See `docs/REQUIREMENTS.md`. Public repos only, GitHub API ingestion,
keyword search, saved conversations, read-only (no repo changes).

## 3. Architecture (planned)
User query -> LangGraph workflow -> MCP client -> MCP server tools
(GitHub + index) -> LLM answer -> save to PostgreSQL -> response.
Only a few retrieved chunks go to the LLM, never the whole repository.

## 4. Folder structure (current)
devpilot-ai/
- app/core/config.py          settings loaded from `.env`
- app/core/logging_config.py  logging setup
- tests/                      (empty)
- docs/                       LEARNING_LOG, REQUIREMENTS, PROJECT_GUIDE

Planned folders (created when their phase starts): app/github,
app/indexing, app/mcp_server, app/mcp_client, app/db, app/graph, app/api.

## 5. Module responsibilities (implemented)
- `config.py`: defines `Settings` (`app_env`, `log_level`) and a
  `settings` object. Reads `.env`; OS environment variables override it.
- `logging_config.py`: `setup_logging(level)` configures the root
  logger (level + format). Not called anywhere yet.

## 6. Technology stack
Python 3.12, pydantic-settings (config), standard `logging`.
Planned: httpx/GitHub REST API, PostgreSQL + SQLAlchemy, MCP,
LangGraph, FastAPI, pytest, Docker.

## 7. Planned, not yet designed
Database schema, MCP tools, API endpoints, indexing strategy.
(Details are decided in Phases 4-9.)

## 8. Design decisions so far
- Config fails fast: `app_env` has no default; wrong or missing
  values stop the app at startup.
- `log_level` is restricted to DEBUG/INFO/WARNING/ERROR/CRITICAL
  (default INFO).
- `setup_logging` takes the level as an argument, so it does not
  depend on `config.py`.
- Secrets live only in `.env` (git-ignored); `.env.example` lists
  key names only.
- Only keys used by the current phase are active in `.env`.
- GitHub API ingestion for the MVP; keyword search before embeddings.

## 9. Dependencies between modules
`logging_config` and `config` are independent. A caller (future
`main.py`) will pass `settings.log_level` to `setup_logging`.

## 10. Status
Done: environment setup, requirements, config, logging setup.
Next: this guide, then Phase 3 (GitHub ingestion).
Pending: everything from Phase 3 onward.

## 11. Known limitations
- `env_file='.env'` is a relative path (run from the repo root).
- `setup_logging` is not wired into an entry point yet.
- Lowercase `LOG_LEVEL` behaviour is untested.

## 12. Security considerations
- `.env` is never committed (verified with `git ls-files`).
- Validation errors can print secret values; secret fields will use
  `SecretStr` when they are added (Phase 3).
- Never log tokens or API keys.
- Least privilege: the MVP needs no write token.

## 13. Assumptions to confirm
- MCP transport: stdio for the MVP (decide in Phase 5).
- Default branch only; single local user.
