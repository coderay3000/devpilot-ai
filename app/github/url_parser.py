import re
from urllib.parse import urlparse


class InvalidGitHubURLError(ValueError):
    def __init__(self):
        super().__init__("Invalid GitHub URL. Please provide a valid GitHub repository URL.")


def parse_github_url(url: str) -> tuple[str, str]:
    url = url.strip()
    parsed = urlparse(url)

    if parsed.scheme != "https":
        raise InvalidGitHubURLError()
    if parsed.hostname != "github.com":
        raise InvalidGitHubURLError()

    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        raise InvalidGitHubURLError()

    owner, repo = parts[0], parts[1]

    repo = repo.removesuffix(".git")

    if re.fullmatch(r"[A-Za-z0-9-]+", owner) is None:
        raise InvalidGitHubURLError()
    if re.fullmatch(r"[A-Za-z0-9._-]+", repo) is None:
        raise InvalidGitHubURLError()
    if repo in (".", ".."):
        raise InvalidGitHubURLError()

    return owner, repo
      