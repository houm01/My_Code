#!/bin/bash

scores=80;

if [[ $scores -ge 85 ]]; then
     echo "very good";
elif [[ $scores -gt 75 ]]; then
     echo "good";
elif [[ $scores -gt 60 ]]; then
     echo "pass";
else 
     echo "no pass"
fi
