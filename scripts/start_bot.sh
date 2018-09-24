#!/bin/bash
(&>.bot_log python3 disc_bot_example.py &)
pgrep -n python3 > .pid

