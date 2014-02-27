# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestBluetoothSettings(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.settings = Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_toggle_bluetooth_settings(self):
        """ Toggle Bluetooth via Settings - Networks & Connectivity

        https://moztrap.mozilla.org/manage/case/3346/

        """
        bluetooth_settings = self.settings.open_bluetooth_settings()

        self.assertFalse(bluetooth_settings.is_bluetooth_enabled)
        bluetooth_settings.enable_bluetooth()

        self.assertTrue(self.data_layer.get_setting('bluetooth.enabled'))

    def tearDown(self):

        # Disable Bluetooth
        self.data_layer.set_setting('bluetooth.enabled', False)

        GaiaMtbfTestCase.tearDown(self)
