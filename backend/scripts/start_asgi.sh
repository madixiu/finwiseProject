#!/bin/bash
daphne backend.asgi:application --bind 0.0.0.0 --port 9000

#daphne SSL
# daphne -e ssl:443:privateKey=key.pem:certKey=cert.pem backend.asgi:application --port 9000