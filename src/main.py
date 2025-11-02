"""Script to change the MAC address of the default network interface."""

import platform

from subprocess import run, PIPE
from src.wireless import new_mac_address, get_default_interface_name

system = platform.system()

interface_name = get_default_interface_name()
mac_address_with_colons = new_mac_address(colons=True)

if system == "Windows":
    pass
elif system in ["Linux", "Darwin"]:  # MacOS returns 'Darwin'
    run(
        ["./linux.sh", interface_name, mac_address_with_colons],
        check=True,
        stdout=PIPE,
        stderr=PIPE,
    )
else:
    print("Unsupported OS")
