# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestBluetoothSettings(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        # Bluetooth host object
        self.bluetooth_host = BluetoothHost(self.marionette)

        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)

        self.mtbf_settings.back_to_main_screen()

    def test_toggle_bluetooth_settings(self):
        """Toggle Bluetooth via Settings - Networks & Connectivity

        https://moztrap.mozilla.org/manage/case/6071/
        """
        device_name = str(time.time())

        bluetooth_settings = self.settings.open_bluetooth_settings()
        bluetooth_settings.enable_bluetooth()

        bluetooth_settings.tap_rename_my_device()
        bluetooth_settings.type_phone_name(device_name)
        bluetooth_settings.tap_update_device_name_ok()

        bluetooth_settings.enable_visible_to_all()

        # Now have host machine inquire and shouldn't find our device
        device_found = self.bluetooth_host.is_device_visible(device_name)
        self.assertTrue(device_found, "Host should see our device (device discoverable mode is ON)")

    def tearDown(self):

        # Disable Bluetooth
        self.data_layer.set_setting('bluetooth.enabled', False)

        GaiaMtbfTestCase.tearDown(self)
