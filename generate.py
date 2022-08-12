#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

MODULES = [
    ("bloghead", "https://github.com/nhanb/bloghead"),
    ("shark", "https://github.com/nhanb/shark"),
]

HOME_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width" />
  <title>Nhân's Go modules</title>
</head>
<body>
  <h1>Modules:</h1>
  <ul>
{modules}
  </ul>
  <p>This page was autogerated from the source code <a href="https://github.com/nhanb/go.imnhan.com">here</a>.</p>
</body>
</html>
"""

MODULE_TEMPLATE = """\
<!DOCTYPE html>
<head>
  <title>{name}</title>
  <meta name="go-import" content="go.imnhan.com/{name} git {repo}">
  <meta http-equiv="refresh" content="0;URL='{repo}'">
  <meta name="viewport" content="width=device-width">
<body>
  Redirecting you to the <a href="{repo}">project page</a>...
"""


def gen_homepage():
    modules = "\n".join(
        f'    <li>go.imnhan.com/{name} → <a href="{repo}">{repo}</a></li>'
        for name, repo in MODULES
    )
    html = HOME_TEMPLATE.format(modules=modules)
    with open("index.html", "w") as f:
        f.write(html)


def gen_module(name, repo):
    try:
        shutil.rmtree(name)
    except FileNotFoundError:
        pass

    os.mkdir(name)
    file_path = Path(name) / "index.html"
    html = MODULE_TEMPLATE.format(name=name, repo=repo)
    with open(file_path, "w") as f:
        f.write(html)


if __name__ == "__main__":
    for name, repo in MODULES:
        print(name, "->", repo)
        gen_module(name, repo)

    gen_homepage()
