#!/usr/bin/env python
"""
Opens the traffic page for every repository of a user.

Usage:
  github_traffic.py username
"""


import json
import sys
import time

import perform

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

def main():
    URL = "https://api.github.com/users/{}/repos".format(sys.argv[1])
    repos = json.loads(urlopen(URL).read().decode("utf-8"))
    sorted_repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)

    for repo in sorted_repos:
        url = "{}/graphs/traffic".format(repo["html_url"])
        print("Opening {}".format(url))
        perform.firefox(url, nr=True)
        time.sleep(.75)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print(__doc__)
