#!/bin/bash

API_URL="127.0.0.1:8080"

# Log file to store the health check results
LOG_FILE="/var/log/health_check.log"

http_response=$(curl -s -o /dev/null -w "%{http_code}" "$API_URL")

if [ "$http_response" == "200" ]; then
    echo "$(date): API at $API_URL is reachable - Health check passed" >> "$LOG_FILE"
else
    echo "$(date): API at $API_URL is unreachable - Health check failed (HTTP $http_response)" >> "$LOG_FILE"
fi

