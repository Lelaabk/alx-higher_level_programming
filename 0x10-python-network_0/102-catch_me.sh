#!/bin/bash
# Makes request to to 0.0.0.0:5000/catch_me causing server to respond with "You got me!"
curl -sL -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
