#!/bin/bash
rm -f master.zip
wget https://github.com/dazemc/flask_networkmanager/archive/refs/heads/master.zip
unzip master.zip
mv flask_networkmanager-master wipi_portal
cd wipi_portal
mkdir .venv
echo "Creating python venv..."
python3 -m venv .venv/
echo "Installing python packages..."
.venv/bin/pip install -r requirements.txt
chmod +x scripts/*.sh
cd scripts
rm -f /etc/systemd/system/wipi.service
rm -f /etc/NetworkManager/system-connections/Hotspot*
touch wipi.service
python init.py
mv wipi.service /etc/systemd/system/wipi.service
systemctl daemon-reload && systemctl enable wipi.service && systemctl start wipi.service
exit