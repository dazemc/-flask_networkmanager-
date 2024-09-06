#!/bin/bash
ip link set usb0 down || true # this is for dev can be commented out
python startup.py