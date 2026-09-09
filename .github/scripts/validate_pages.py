#!/usr/bin/env python3
"""Validate that every internal link in the knowledge-base resolves to a built page.

Checks:
  1. Every site page (has `permalink` in its front matter) is discoverable.
  2. Every internal link in every page points to an existing permalink.

Runs from anywhere — the repo root is derived from this script's location.
Depends only on the Python standard library.
"""

import os
import re
import sys
from urllib.parse import urljoin, urlsplit

REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

EXCLUDED_DIRS = {".git", ".github"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_PREFIXES = ("http:", "https:", "mailto:", "tel:", "data:", "#", "<")


def read_text(path):
    with open(path, encoding="utf-8-sig") as fh:
        return fh.read()


def front_matter_meta(text):
    """Parse the flat key:value front matter of a markdown file."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta = {}
    for line in text[3:end].splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "layout")):
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            meta[key.strip().lower()] = value.strip().strip("\"'")
    return meta


def is_markdown(name):
    return name.lower().endswith(".md")


def collect_paths():
    """Map every normalized permalink to the markdown file that serves it."""
    pages = {}  # normalized URL path -> (source file, permalink)
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for name in files:
            if not is_markdown(name):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, REPO_ROOT).replace("\\", "/")
            meta = front_matter_meta(read_text(path))
            permalink = meta.get("permalink", "")
            if permalink and permalink.startswith("/"):
                key = permalink.rstrip("/") or "/"
                pages[key] = (rel, permalink)
    # The root index.md is always served at "/"
    home = os.path.join(REPO_ROOT, "index.md")
    if os.path.exists(home):
        pages.setdefault("/", ("index.md", "/"))
    return pages


def deployed_base(path, pages):
    """The deployed URL of a markdown file, or None if it's not a site page."""
    rel = os.path.relpath(path, REPO_ROOT).replace("\\", "/")
    if rel == "index.md":
        return "/"
    meta = front_matter_meta(read_text(path))
    return meta.get("permalink") or None


def main():
    pages = collect_paths()
    errors = []

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for name in sorted(files):
            if not is_markdown(name):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, REPO_ROOT).replace("\\", "/")
            base = deployed_base(path, pages)
            if base is None:
                continue  # not part of the rendered site (README, CONTRIBUTING, ...)

            text = read_text(path)
            for match in LINK_RE.finditer(text):
                target = match.group(1).strip()
                if target.startswith(URL_PREFIXES) or ":" in target.split("/", 1)[0]:
                    continue  # external, anchor-only, or protocol-prefixed
                target = target.split("#")[0].strip()
                if not target:
                    continue

                resolved = urljoin("https://site" + base, target)
                path_part = urlsplit(resolved).path
                key = path_part.rstrip("/") or "/"

                if key not in pages:
                    errors.append(
                        f"{rel}: broken link -> `{target}` (resolves to {path_part})"
                    )

    if errors:
        print("❌ Found broken internal links:")
        for err in sorted(set(errors)):
            print(f"   {err}")
        print(f"\n{len(set(errors))} broken link(s) found.")
        return 1

    print(f"✅ All internal links resolve correctly across {len(pages)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())