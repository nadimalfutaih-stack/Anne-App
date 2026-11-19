#!/usr/bin/env python3
"""Wraps prototyp/index.html into a complete page at docs/index.html for GitHub Pages."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
body = (root / "prototyp" / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="apple-mobile-web-app-title" content="Mein Tag">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""
out = head + "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
(root / "docs" / "index.html").write_text(out, encoding="utf-8")
(root / "docs" / ".nojekyll").write_text("", encoding="utf-8")
print("docs/index.html geschrieben")
