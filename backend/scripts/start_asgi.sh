#!/bin/bash
daphne backend.asgi:application --bind 0.0.0.0 --port 9000

#daphne SSL
# sudo daphne -e ssl:443:privateKey=privkey.pem:certKey=fullchain.pem backend.asgi:application