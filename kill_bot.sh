#!/bin/bash
if [  -f .pid ]; then
	kill $(cat .pid)
	rm .pid
fi
