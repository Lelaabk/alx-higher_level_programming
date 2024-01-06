#!/bin/bash
# Makes request to to 0.0.0.0:5000/catch_me causing server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
