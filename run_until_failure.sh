#!/bin/bash

i=0

trap stop INT
function stop() {
    echo "Failed after $i iterations"
    exit $code
}

while :; do
    $@

    code=$?
    if [[ $code -ne 0 ]]; then
        stop
    fi
    ((i++))
done
