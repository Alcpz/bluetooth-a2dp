# Setting Bluetooth Audio Device to High Fidelity in Ubuntu 20.04

This guide explains how to set your Bluetooth audio device to high fidelity automatically in Ubuntu 20.04 when it connects.

## Prerequisites

- Ubuntu 20.04
- A Bluetooth audio device
- The `bluez-tools` package, which provides the `bt-device` command. 
    `sudo apt-get install blueztools`.

## Steps

1. Add executable permissions to `set-bluetooth-a2dp-quality.py`
2. Change `bt_device_name` in the script to match your device.
3. Create a Udev rule

    ```shell
    sudo vim /etc/udev/rules.d/99-bluetooth-a2dp-high-fidelity.rules
    ```

    ```bash
    ACTION=="add", SUBSYSTEM=="bluetooth", KERNEL=="hci0", ATTRS{name}=="Your Bluetooth Device Name", RUN+="/path/to/set-bluetooth-a2dp-quality.sh"
    ```
  
4. Replace "Your Bluetooth Device Name" with the actual name of your Bluetooth audio device.

5. Save the file and restart your computer for the changes to take effect.

Your Bluetooth audio device should now be set to high fidelity automatically when it connects.
