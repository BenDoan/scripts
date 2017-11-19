#!/bin/bash

i=0

trap stop INT
function stop() {
    echo "Failed after $i iterations"
    exit $code
}

time while :; do
    $@

    code=$?
    if [[ $code -ne 0 ]]; then
        stop
    fi
    echo "Ran $i times"
    ((i++))
done
