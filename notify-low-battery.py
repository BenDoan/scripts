#!/usr/bin/env python
# Usage: ./notify-low-battery.py [threshold]

import sys
import time

import perform

battery_threshold = 15
if len(sys.argv) > 1:
    battery_threshold = int(sys.argv[1])

# acpi output looks like:
# Battery 0: Unknown, 5%
# Battery 1: Discharging, 1%, 00:01:15 remaining
total_battery_percent = 0
charging = False
for line in perform.acpi().split("\n"):
    total_battery_percent += int(line.split(" ")[3].replace(",", "").replace("%", ""))

    if "charging" in line.lower():
        charging = True
        break

if total_battery_percent < battery_threshold and not charging:
    msg = "Low battery: {}%".format(total_battery_percent)

    perform._("notify-send", msg)
    perform._("i3-nagbar", "-m", msg, nr=True)
    nag_pid = perform._("ps aux | grep i3-nagbar | grep -v grep | awk '{ print $2 }'", shell=True)


    time.sleep(45)
    perform.kill(nag_pid)
