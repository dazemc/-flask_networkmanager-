import subprocess


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
        return False
    return True


if wifi_check():
    subprocess.run(["sh", "run.sh"], check=False)
