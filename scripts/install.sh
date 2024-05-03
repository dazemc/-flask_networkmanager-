#!/bin/bash
apt install git -y
git clone https://github.com/dazemc/flask_networkmanager.git
mv flask_networkmanager wipi_portal
cd wipi_portal
mkdir .venv
echo "Creating python venv..."
python3 -m venv .venv/
echo "Installing python packages..."
.venv/bin/pip install -r requirements.txt
exit