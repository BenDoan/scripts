#!/bin/bash

num=$((RANDOM % 10))
if [[ num -ge 8 ]]; then
    echo "Failure"
    exit 1
else
    echo "Success"
    exit 0
fi
