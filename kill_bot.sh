#!/bin/bash
if [  -f .pid ]; then
	kill $(cat .pid)
	rm .pid
	echo "Killing bot $(date) --------------------------------------------------------------------------------------------------------" >> .bot_log
fi
