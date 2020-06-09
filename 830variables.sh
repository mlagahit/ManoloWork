#!/bin/bash

greeting="welcome"

user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! Today is $day, which is the best ay of the entire >week<"

echo "Your Bash Shell version is: $BASH_VERSION. Cool!"
