#!/bin/bash

if [ -d venv ]; then
    source ./venv/bin/activate
else
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirnments.txt
fi
