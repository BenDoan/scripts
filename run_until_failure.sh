#!/bin/bash

i=0
while :; do
    $@

    code=$?
    if [[ $code -ne 0 ]]; then
        echo "Failed after $i iterations"
        exit $code
    fi
    ((i++))
done
