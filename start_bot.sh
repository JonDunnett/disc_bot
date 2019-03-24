#!/bin/bash
echo "Starting bot $(date)--------------------------------------------------------------------------------------------------------" >> .bot_log
(&>>.bot_log python3 ./src/disc_bot.py &)
pgrep -n python3 > .pid
