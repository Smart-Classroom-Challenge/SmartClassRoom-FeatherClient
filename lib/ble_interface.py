# SPDX-FileCopyrightText: 2021 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService


class BLEConnection():
    def __init__(self):
        self.ble = BLERadio()
        self.uart = UARTService()
        self.advertisement = ProvideServicesAdvertisement(self.uart)

        print('BLE initiated')
