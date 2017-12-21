#!/usr/bin/env python3
"""
Monitors a website for changes
"""

import argparse
import difflib
import json
import os
import smtplib

from email.mime.text import MIMEText

try:
    from urllib.request import urlopen
    from urllib.parse import quote_plus
except ImportError:
    from urllib2 import urlopen
    from urllib import quote_plus

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "SITE-WATCHER-DATA")


def load_hist_file():
    fname = os.path.join(SCRIPT_DIR, "site-watcher-history.json")
    if not os.path.exists(fname):
        return {}
    with open(fname) as f:
        return json.load(f)

def save_hist_file(hist_file):
    fname = os.path.join(SCRIPT_DIR, "site-watcher-history.json")
    with open(fname, "w+") as f:
        return json.dump(hist_file, f)


def display_changes(before, after):
    for line in difflib.unified_diff(before.split("\n"), after.split("\n")):
        print(line)


def email_changes(to, url, before, after):
    diff = "\n".join(difflib.unified_diff(before.split("\n"), after.split("\n")))
    frm = "site-watcher"

    msg = MIMEText(diff)
    msg['Subject'] = 'Changes for {}'.format(url)
    msg['From'] = frm
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.sendmail(frm, to, msg.as_string())
    s.quit()


def main(args):
    hist_file = load_hist_file()
    url = args.url
    if not url.startswith("http"):
        url = "http://" + url

    last = hist_file.get(url, {}).get("text")
    page = b"".join(urlopen(url).readlines()).decode("utf-8").replace("\r\n", "\n")

    if url not in hist_file:
        hist_file[url] = {}
    hist_file[url]["text"] = page
    save_hist_file(hist_file)

    if last and last != page:
        if args.display == "print":
            display_changes(last, page)
        elif args.display == "email":
            email_changes("site-changes@flainted.com", url, last, page)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('url', help='the url')
    parser.add_argument('display', choices=["print", "email"], help='how to display results')

    args = parser.parse_args()
    main(args)
