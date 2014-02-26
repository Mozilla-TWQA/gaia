# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestPowerSaveMode(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.data_layer.disable_wifi()
        self.data_layer.connect_to_cell_data()
        self.data_layer.connect_to_wifi()
        self.data_layer.set_setting('geolocation.enabled', 'true')
        self.data_layer.set_setting('bluetooth.enabled', 'true')

        self.settings = Settings(self.marionette)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_power_save_mode(self):
        # Tap on Battery menu item.
        battery_settings = self.settings.open_battery_settings()
        battery_settings.toggle_power_save_mode()

        # Wait for Cell Data to be disabled.
        self.wait_for_condition(lambda m: not self.data_layer.is_cell_data_connected)

        # Wait for Wi-Fi to be disabled.
        self.wait_for_condition(lambda m: not self.data_layer.is_wifi_connected(self.testvars['wifi']))

        # Check if Cell Data is disabled.
        self.assertFalse(self.data_layer.get_setting('ril.data.enabled'))

        # Check if GPS is disabled.
        self.assertFalse(self.data_layer.get_setting('geolocation.enabled'),)

        # Check if Bluetooth is diabled.
        self.assertFalse(self.data_layer.get_setting('bluetooth.enabled'))

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
