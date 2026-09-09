#!/usr/bin/env python3
"""Validate that every internal link in the knowledge-base resolves to a built page.

This script models how links actually behave after deployment:

  * The site is a GitHub Pages *project* site, served under a subpath such as
    ``/knowledge-base/`` (derived from ``_config.yml``'s ``homepage`` or
    ``baseurl``).  A markdown link that starts with a leading ``/`` -- e.g.
    ``[Python](/programming/py/)`` -- would make the browser jump to the
    *domain root* (``brodante.github.io/programming/py/``), completely
    missing the site's subpath.  Those links are reported as broken.
  * Relative links (``programming/py/``, ``../``) are resolved against the
    page's own deployed URL and are the only form that works on a
    subpath-hosted site.

Checks:
  1. Every site page (has a ``permalink`` in its front matter) is collected
     into a permalink map.
  2. Every internal link in every page resolves to an existing page **below
     the site's base path** -- exactly as a browser would resolve it.

Runs from anywhere.  Depends only on the Python standard library.
"""

import os
import re
import sys
from urllib.parse import urljoin, urlsplit

REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

EXCLUDED_DIRS = {".git", ".github"}
LINK_RE = re.compile(r"(?<!`)\[[^\]]*\]\(([^)]+)\)")
URL_PREFIXES = ("http:", "https:", "mailto:", "tel:", "data:", "#", "<", "{", "\\")
ASSET_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
                    ".css", ".js", ".ico", ".woff", ".woff2", ".pdf")


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
            # Strip trailing comment like # explanation
            value = re.sub(r"\s+#.*$", "", value).strip()
            meta[key.strip().lower()] = value.strip().strip("\"'")
    return meta


def is_markdown(name):
    return name.lower().endswith(".md")


def site_base_path():
    """Determine the URL subpath the site is served under.

    Looks first at the ``baseurl`` key in ``_config.yml``, then at the
    path portion of the ``homepage`` key.  Defaults to the repo name.
    """
    cfg = os.path.join(REPO_ROOT, "_config.yml")
    if os.path.exists(cfg):
        meta = front_matter_meta(read_text(cfg))
        baseurl = meta.get("baseurl")
        if baseurl:
            return "/" + baseurl.strip("/")
        homepage = meta.get("homepage", "")
        if homepage and "github.io" in homepage:
            path = urlsplit(homepage).path.rstrip("/")
            if path:
                return path
    # Fall back to the directory name of the checkout (e.g. "/knowledge-base")
    return "/" + os.path.basename(REPO_ROOT).strip("/")


def collect_paths(basepath):
    """Map every deployed URL (including base path) to its markdown source."""
    pages = {}
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
                key = (basepath + permalink).rstrip("/") or "/"
                pages[key] = (rel, permalink)
    # The root index.md is always served at the site's base path
    home = os.path.join(REPO_ROOT, "index.md")
    if os.path.exists(home):
        pages.setdefault(basepath or "/", ("index.md", "/"))
    return pages


def deployed_base(path, basepath, pages):
    """Deployed URL base of a markdown file, or None if it's not a site page."""
    rel = os.path.relpath(path, REPO_ROOT).replace("\\", "/")
    if rel == "index.md":
        return (basepath or "/") + "/"
    meta = front_matter_meta(read_text(path))
    permalink = meta.get("permalink")
    if not permalink:
        return None
    if permalink.startswith(basepath):
        return permalink
    return basepath + permalink


def main():
    basepath = site_base_path()
    pages = collect_paths(basepath)
    errors = []

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for name in sorted(files):
            if not is_markdown(name):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, REPO_ROOT).replace("\\", "/")
            base = deployed_base(path, basepath, pages)
            if base is None:
                continue  # not part of the rendered site (README, CONTRIBUTING, ...)

            text = read_text(path)
            for match in LINK_RE.finditer(text):
                target = match.group(1).strip()
                if target.startswith(URL_PREFIXES):
                    continue  # external, protocol-prefixed, anchor, Liquid, or code
                if any(target.lower().endswith(ext) for ext in ASSET_EXTENSIONS):
                    continue  # asset reference, not a page

                if target.startswith("/"):
                    errors.append(
                        f"{rel}: absolute link `{target}` -> on a subpath-hosted "
                        f"site ({basepath}/) this resolves to the domain root and "
                        "404s. Use a RELATIVE link (no leading '/') instead."
                    )
                    continue

                resolved = urljoin("https://site" + base, target)
                path_part = urlsplit(resolved).path
                key = path_part.rstrip("/") or "/"

                if key not in pages:
                    errors.append(
                        f"{rel}: broken link -> `{target}` (resolves to {path_part})"
                    )

    if errors:
        print(f"❌ Found broken internal links (site base path: {basepath}/):")
        for err in sorted(set(errors)):
            print(f"   {err}")
        print(f"\n{len(set(errors))} broken link(s) found.")
        return 1

    print(f"✅ All internal links resolve correctly across {len(pages)} pages "
          f"(site base path: {basepath}/).")
    return 0


if __name__ == "__main__":
    sys.exit(main())