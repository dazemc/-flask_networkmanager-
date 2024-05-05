#!/bin/bash
apt update && apt install git iwd -y
git clone https://github.com/dazemc/flask_networkmanager.git
mv flask_networkmanager wipi_portal
cd wipi_portal
mkdir .venv
echo "Creating python venv..."
python3 -m venv .venv/
echo "Installing python packages..."
.venv/bin/pip install -r requirements.txt
chmod +x scripts/*.sh
rm -f /etc/NetworkManager/conf.d/iwd.conf && touch /etc/NetworkManager/conf.d/iwd.conf
echo "[device]\nwifi.backend=iwd" | tee /etc/NetworkManager/conf.d/iwd.conf
cd scripts
touch wipi.service
python init.py
rm -f /etc/systemd/system/wipi.service
cp wipi.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable wipi.service && systemctl disable wpa_supplicant && systemctl enable iwd
reboot & exit