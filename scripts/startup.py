import subprocess
import time
import logging

# give the device a little time to connect to pre-existing networks
time.sleep(30)

def wifi_check() -> bool:
    s = subprocess.check_output(
        [
            "nmcli",
            "-f",
            "IN-USE",
            "dev",
            "wifi",
        ]
    ).decode("utf-8")

    if "*" in s:
        logging.debug("Wifi in use, not enabling AP mode...")
        return False
    logging.debug("Wifi not in use, setting up AP mode...")
    return True


if wifi_check():
    subprocess.run(["sh", "run.sh"], check=False)
