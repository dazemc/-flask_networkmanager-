import os
import subprocess
import time

HOTSPOT_SSID = "Wipi"
HOTSPOT_PASS = "testing247"

cwd = os.getcwd()
service = f"""
[Unit]
Description=Wipi Portal
After=network.target
[Service]
WorkingDirectory={cwd}
ExecStart={cwd}/startup.sh
[Install]
WantedBy=default.target
"""


with open(f"{cwd}/wipi.service", "w", encoding="utf-8") as s_file:
    s_file.write(service)

subprocess.run(
    [
        "nmcli",
        "device",
        "wifi",
        "hotspot",
        "ssid",
        HOTSPOT_SSID,
        "password",
        HOTSPOT_PASS,
        "ifname",
        "wlan0",
    ],
    check=False,
)
time.sleep(3)
subprocess.run(
    [
        "nmcli",
        "networking",
        "off",
    ],
    check=False,
)
subprocess.run(
    [
        "nmcli",
        "connection",
        "modify",
        "Hotspot",
        "ipv4.addresses 192.168.6.9/24",
    ],
    check=False,
)
subprocess.run(
    [
        "nmcli",
        "networking",
        "on",
    ],
    check=False,
)
