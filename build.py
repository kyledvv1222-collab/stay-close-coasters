"""Builds index.html (the hosted site) from src/app.html (the same source published as the Claude Artifact)."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / "src/app.html").read_text()
head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]
logo = re.search(r'<symbol id="logo" viewBox="0 0 43 39">(.*?)</symbol>', src, re.S).group(1)
(root / "icons/icon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180"><rect width="180" height="180" fill="#135358"/>'
    '<g transform="translate(40 44.7) scale(2.3256)" fill="#fff">' + logo + '</g></svg>')
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Stay Close conversation-starter coasters from PFLAG NYC.">
<meta name="theme-color" content="#135358">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" href="icons/icon.svg" type="image/svg+xml">
<style>html{{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}*,*::before,*::after{{box-sizing:inherit}}</style>
{head}
</head>
<body>
{body}
<script>if ("serviceWorker" in navigator) addEventListener("load", function(){{ navigator.serviceWorker.register("sw.js").catch(function(){{}}); }});</script>
</body>
</html>
"""
(root / "index.html").write_text(page)
print("built index.html")
