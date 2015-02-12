#!/usr/bin/env python3
""" Usage:
  github_traffic.py username
"""


import json
import sys

import perform

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen





def main():
    URL = "https://api.github.com/users/{}/repos".format(sys.argv[1])

    repos = json.loads(urlopen(URL).read().decode("utf-8"))
    for repo in repos:
        url = "{}/graphs/traffic".format(repo["html_url"])
        print("Opening {}".format(url))
        perform.firefox(url, no_return=True)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print(__doc__)
