#!/bin/bash

if [[ $# -eq 2 ]]; then
    succeed_rate=$1
else
    succeed_rate=0.1
fi

modulus=$(echo "$succeed_rate * 100 / 1" | bc)
num=$((RANDOM % $modulus))
if [[ num -ge 8 ]]; then
    echo "Failure"
    exit 1
else
    echo "Success"
    exit 0
fi
