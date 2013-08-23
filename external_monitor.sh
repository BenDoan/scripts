#!/bin/bash
#activates external monitors when they are connected and deactivates
#them when they are disconnected

INTERNAL_SCREEN=eDP1
INTERNAL_RESOLUTION=1920x1080
EXTERNAL_SCREEN=VGA1
EXTERNAL_RESOLUTION=1440x900

function activate_external {
    xrandr --output $INTERNAL_SCREEN --mode $INTERNAL_RESOLUTION
    xrandr --output $EXTERNAL_SCREEN --mode $EXTERNAL_RESOLUTION --right-of $INTERNAL_SCREEN
    MONITOR=$EXTERNAL_SCREEN
}

function deactivate_external {
    xrandr --auto
    MONITOR=none
}

function vga_connected {
    ! xrandr | grep $EXTERNAL_SCREEN | grep -q disconnected
}

function vga_active {
    [[ $MONITOR = $EXTERNAL_SCREEN ]]
    return $?
}

while true; do
    if ! vga_active && vga_connected; then
        activate_external
    fi

    if vga_active && ! vga_connected; then
        deactivate_external
    fi
    sleep 5s
done
