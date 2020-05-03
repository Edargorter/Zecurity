#!/bin/bash

export copy

cat passwords.txt | tail -n 1 | xclip -sel clip
