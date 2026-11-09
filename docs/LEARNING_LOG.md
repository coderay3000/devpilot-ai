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


## Session 2 – 2026-11-05 – Phase 1: Requirements

### Concepts learned
- Requirements document: scope, non-goals, constraints, acceptance criteria
- Non-goal vs acceptance criterion
- Keeping a requirements doc short and MVP-focused

### Files implemented
- `docs/REQUIREMENTS.md`

### What I implemented
- Reviewed the requirements draft, asked for a shorter version, accepted it unchanged
- Committed and pushed it to `main`

### What I understood / did not understand
- Understood: the requirements doc fixes the project scope; the config
  reads `.env`; field names are not case-sensitive; real environment
  variables override `.env`; `BaseSettings` checks types but not whether
  a value is valid (for example `LOG_LEVEL=banana` is accepted).
- Not clear yet: none

### Bugs encountered / fixed
- Pushed before committing `REQUIREMENTS.md`, so the file was not on GitHub; fixed by committing and pushing again

### Tests performed
- `git status` and `git log --oneline` to confirm commit and push state

### Remaining problems
- None known

### Next task
- Phase 2, Day 1: configuration (settings loaded from `.env`)


## Session 3 – 2026-11-06 – Phase 2: Logging

### Concepts learned
- Log levels, numeric severity and threshold filtering
- `logging.basicConfig` (`level`, `format`) and format placeholders
- Keyword arguments and quoted strings
- `Literal` to restrict a setting to allowed values
- Two validation layers: Pydantic (config) and `logging` (setup)

### Files implemented
- `app/core/logging_config.py`
- `app/core/config.py` (updated: `log_level` restricted with `Literal`)

### What I implemented
- `setup_logging(level)` that configures the root logger
- Restricted `log_level` to the five allowed level names

### What I understood / did not understand
- Understood: `setup_logging` configures how logging behaves (level and format) but does not produce logs itself; `basicConfig` sets up the root logger once and named loggers inherit from it; logging has no relation with config until we pass `settings.log_level` (an attribute, no brackets) to `setup_logging(...)`.
- Not clear yet: none

### Bugs encountered / fixed
- Wrote `basicConfig(level=, format=%(asctime)s)`: missing value and unquoted string; fixed with a value and quotes

### Tests performed
- `setup_logging('INFO')` showed `info`, hid `debug`
- `setup_logging('banana')` raised `ValueError` from the `logging` module
- Not tested: `LOG_LEVEL=banana` and lowercase `info` in `.env`

### Remaining problems
- `setup_logging` is not called anywhere yet (needs `main.py`)

### Next task
- `docs/PROJECT_GUIDE.md` first version


## Session 4 – 2026-11-06 – Project guide and HTTP basics

### Concepts learned
- HTTP request and response; methods and status code families
- GitHub unauthenticated rate limit (60 requests/hour per IP)
- Rate-limit headers; Unix timestamp
- Failed requests (404) also consume rate limit
- `curl.exe -I` to inspect headers

### Files implemented
- `docs/PROJECT_GUIDE.md` (first version, drafted by Claude, reviewed by me)

### What I implemented
- Reviewed, saved, committed, and pushed the project guide
- Ran `curl.exe -I` against an existing and a missing repository

### What I understood / did not understand
- Understood: the URL must be validated locally before calling the API, because failed requests also use up the rate limit (60/hour without a token); we fetch only relevant files, not the whole repository, for the same reason.
- Not clear yet:  

### Bugs encountered / fixed
- None

### Tests performed
- Existing repo returned `200 OK`; missing repo returned `404 Not Found`
- `X-RateLimit-Remaining` went from 58 to 57 across the two calls

### Remaining problems
- None known

### Next task
- Phase 3 design: GitHub URL parsing, `SecretStr`, `httpx`


## Session 5 – 2026-11-09 – Phase 3: GitHub URL parser

### Concepts learned
- URL anatomy and `urllib.parse.urlparse`
- Exact hostname matching (not `in` / `startswith`) and why
- Custom exception class
- `re.fullmatch`, character sets, raw strings
- `str.removesuffix` vs `rstrip`
- Validation layers: allowed characters vs allowed values (`.` and `..`)
- Function vs class for stateless logic

### Files implemented
- `app/github/url_parser.py`, `app/github/__init__.py`

### What I implemented
- `parse_github_url(url) -> (owner, repo)` with `InvalidGitHubURLError`
- Decisions: `http` and `https` allowed; URLs without a scheme rejected

### What I understood / did not understand
- Understood: scheme ,hostname ,path,how to parse the url and how to validate it
- Not clear yet: ..

### Bugs encountered / fixed
- Wrote a class header with function parameters (`SyntaxError`); fixed by using `def`
- Used `parsed.schema` instead of `parsed.scheme`
- `https://github.com/a/..` was accepted in the first test run (the regex allows dots); fixed by rejecting `.` and `..` explicitly

### Tests performed
- 11-case REPL test: valid URLs, trailing slash, `.git`, extra path, spaces, missing repo, wrong host, lookalike host, no scheme, empty string, `..`
- First run: 10 of 11 behaved as expected

### Remaining problems
- Exception message is the same for every failure reason

### Next task
- Phase 3: GitHub API client (`httpx`, `SecretStr`, status-code handling)