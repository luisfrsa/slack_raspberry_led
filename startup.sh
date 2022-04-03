#!/bin/bash

## to enable auto-startup ## 
# save it unto /etc/rc.local
# sleep 15;
# git -C /home/pi/Desktop/slack_raspberry_led pull origin master;
# sudo su -c 'python3 /home/pi/Desktop/slack_raspberry_led/main.py &' & 

## testing from CLI ## 
# bashrc 
# sudo su -c 'python3 /home/pi/Desktop/slack_raspberry_led/main.py;'

## to kill all processs ## 
# sudo kill -9 $(pgrep -f slack_raspberry_led)
