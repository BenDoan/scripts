#!/usr/bin/env python
# Usage: ./notify-low-battery.py [threshold]

import re
import sys
import time

import perform

battery_threshold = 200
if len(sys.argv) > 1:
    battery_threshold = int(sys.argv[1])

# acpi output looks like:
# Battery 0: Unknown, 5%
# Battery 1: Discharging, 1%, 00:01:15 remaining
total_battery_percent = 0
charging = True
for line in perform.acpi().split("\n"):
    battery_percent = int(re.findall("(\d+)%", line)[0])
    total_battery_percent += battery_percent

    if "discharging" in line.lower():
        charging = False

if total_battery_percent < battery_threshold and not charging:
    msg = "Low battery: {}%".format(total_battery_percent)

    perform._("notify-send", msg)
    perform._("i3-nagbar", "-m", msg, nr=True)
    nag_pid = perform._("ps aux | grep i3-nagbar | grep -v grep | awk '{ print $2 }'", shell=True)


    time.sleep(45)
    perform.kill(nag_pid)
