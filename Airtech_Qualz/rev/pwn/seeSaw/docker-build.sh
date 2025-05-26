#!/bin/bash

docker build -t see-saw-pwn .

# to run container
# docker run --rm -d -p 9912:8000 see-saw-pwn:latest