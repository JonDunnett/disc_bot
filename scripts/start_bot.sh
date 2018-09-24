#!/bin/bash
(&>.bot_log python3 ../src/disc_bot.py &)
pgrep -n python3 > .pid

