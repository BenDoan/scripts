#!/usr/bin/env python3

"""
Usage:
    github_traffic.py username
"""

import perform
from urllib import request
import json
import sys


URL = "https://api.github.com/users/{}/repos".format(sys.argv[1])

repos = json.loads(request.urlopen(URL).read().decode("utf-8"))
for repo in repos:
    url = "{}/graphs/traffic".format(repo["html_url"])
    print("Opening {}".format(url))
    try:
        perform.firefox(url)
    except perform.StandardErrorException as e:
        print("Error: ", e)


