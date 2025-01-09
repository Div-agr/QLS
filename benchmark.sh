#!/bin/bash

exec python3 time_execution_server.py &

cat input.txt | python3 time_execution_client.py
