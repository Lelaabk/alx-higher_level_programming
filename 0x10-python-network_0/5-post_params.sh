#!/bin/bash
# Takes in url and sends post request with specific parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
