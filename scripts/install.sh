#!/bin/bash
echo "Checking for root"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
apt install git -y
git clone https://github.com/dazemc/flask_networkmanager.git
mv flask_networkmanager wipi_portal && cd wipi_portal
mkdir .venv
python3 -m venv .venv/
source .venv/bin/activate
pip install flask, flask_cors

