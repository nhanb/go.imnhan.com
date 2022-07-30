#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

html_template = """\
<head>
    <meta name="go-import" content="go.imnhan.com/{name} git {repo}">
    <meta http-equiv="refresh" content="0;URL='{repo}'">
<body>
    Redirecting you to the <a href="{repo}">project page</a>...
"""


def gen_module(name, repo):
    try:
        shutil.rmtree(name)
    except FileNotFoundError:
        pass

    os.mkdir(name)
    file_path = Path(name) / "index.html"
    html = html_template.format(name=name, repo=repo)
    with open(file_path, "w") as f:
        f.write(html)


with open("modules.txt", "r") as f:
    for line in f.readlines():
        name, repo = line.split(" ", maxsplit=1)
        repo = repo.strip()  # removes trailing newline & any possible double space
        gen_module(name, repo)
        print("Generated", name, "->", repo)
