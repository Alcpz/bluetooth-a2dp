#!/usr/bin/python3
"""
Set your Bluetooth audio device to high fidelity automatically in Ubuntu 20.04 when it connects
"""
import subprocess
import re

def switch_to_a2dp(device_mac_address):
    """
    Switches the specified Bluetooth device to the A2DP profile.

    Args:
        device_mac_address (str): The MAC address of the Bluetooth device.
    """
    subprocess.run(
        ["pacmd", "set-card-profile", f"bluez_card.{device_mac_address.replace(':', '_')}", "a2dp_sink"]
        )


def get_device_mac_address(device_name):
    """
    Gets the MAC address of a Bluetooth device with the specified name.

    Args:
        device_name (str): The name of the Bluetooth device.

    Returns:
        str: The MAC address of the Bluetooth device, 
             or an empty string if the device was not found.
    """
    bt_device_output = subprocess.run(["bt-device", "-l"], capture_output=True, text=True)
    for line in bt_device_output.stdout.split("\n"):
        if device_name in line:
            return re.search(r"\((.*)\)", line).group(1)


def main() -> None:
    """
    Set your Bluetooth audio device to high fidelity automatically in Ubuntu 20.04 when it connects
    """
    DEVICE_NAME = "WH-1000XM4"

    device_mac_address = get_device_mac_address(DEVICE_NAME)
    if device_mac_address:
        switch_to_a2dp(device_mac_address)
    else:
        print("Bluetooth device not found")


if __name__ == "__main__":
    main()
