# DevPilot AI – Requirements (MVP)

## Problem
Understanding an unfamiliar GitHub repository is slow: browsing the
tree, opening files, and searching names by hand. DevPilot lets a user
paste a repo URL and ask questions, answered from the real code with
file citations.

## In scope
- Accept a public GitHub repo URL; reject invalid ones with a clear error.
- Fetch metadata and file tree via the GitHub API; skip secrets,
  binaries, generated files, and dependencies.
- Index code in chunks with file path and line numbers.
- Answer questions using only retrieved chunks, citing file + lines.
- Save conversations in PostgreSQL; resume earlier ones.
- Expose repository tools via an MCP server, used by an MCP client,
  orchestrated by LangGraph.

## Non-goals
- Private repositories
- Modifying repos or running their code
- Anything not listed above (add it to the roadmap, not the MVP)

## Example questions
1. "Where is authentication handled?"
2. "What does `src/utils/retry.py` do?"
3. "Does this project support Kubernetes?" (not in the repo; the system
   must say nothing was found, not invent an answer)

## Constraints
- GitHub API rate limit (60/hr unauthenticated)
- Limited LLM context, so only a few chunks per question

## Done when
- An invalid URL gives a clear error and makes no API call.
- `.env` and binaries are never fetched.
- Every answer cites a retrieved file, or says nothing was found.
- Restarting the app keeps the chat history.