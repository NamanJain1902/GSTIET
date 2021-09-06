#!/bin/bash

shopt -s expand_aliases

# Django Extension Commands
alias erd="python3 manage.py graph_models -a > erd.dot && python3 manage.py graph_models --pydot -a -g -o erd.png"

erd