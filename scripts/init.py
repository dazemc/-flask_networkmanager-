import os
import subprocess

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

conn = """
[connection]
id=Hotspot
uuid=cfaa3398-fd2f-4a75-9ac7-c067fd2f1802
type=wifi
autoconnect=false
timestamp=1714880758

[wifi]
mode=ap
ssid=Wipi

[wifi-security]
group=ccmp;
key-mgmt=wpa-psk
pairwise=ccmp;
proto=rsn;
psk=testing247

[ipv4]
address1=192.168.6.9/24
method=shared

[ipv6]
addr-gen-mode=default
method=ignore
"""

with open(f"{cwd}/wipi.service", "w", encoding="utf-8") as s_file:
    s_file.write(service)

with open(f"{cwd}/Hotspot.nmconnection", "w", encoding="utf-8") as c_file:
    c_file.write(conn)
