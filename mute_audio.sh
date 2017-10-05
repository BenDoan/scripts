#!/bin/bash

PULSE_RUNTIME_PATH="/run/user/$UID/pulse/" DISPLAY=:0 amixer -q -D pulse sset Master off
