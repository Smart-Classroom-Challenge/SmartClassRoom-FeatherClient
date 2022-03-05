# SPDX-FileCopyrightText: 2021 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_airlift.esp32 import ESP32

class BLU():
    def __init__(self):
        self.esp32 = ESP32(
            reset=board.D12,
            gpio0=board.D10,
            busy=board.D11,
            chip_select=board.D13,
            tx=board.TX,
            rx=board.RX,
        )
        self.adapter = esp32.start_bluetooth()
        self.ble = BLERadio(adapter)
        self.uart = UARTService()
        self.advertisement = ProvideServicesAdvertisement(uart)


