#!/usr/bin/env python
# Usage: ./notify-low-battery.py (threshold)

import perform

import sys
import time

threshold = 15
if len(sys.argv) > 1:
    threshold = int(sys.argv[1])

total_battery_percent = 0
for line in perform.acpi().split("\n"):
    total_battery_percent += int(line.split(" ")[3].replace(",", "").replace("%", ""))

if total_battery_percent < threshold:
    perform._("i3-nagbar", "-m", "Low battery: {}%".format(total_battery_percent), nr=True)
    pid = perform._("ps aux | grep i3-nagbar | grep -v grep | awk '{ print $2 }'", shell=True)

    time.sleep(30)

    perform.kill(pid)
