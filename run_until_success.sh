#!/bin/bash

i=0

trap stop INT
function stop() {
    echo "Succeeded after $i iterations"
    exit $code
}

time while :; do
    $@


    ((i += 1))
    code=$?
    if [[ $code -eq 0 ]]; then
        stop
    fi
    echo "Ran $i times"
done
