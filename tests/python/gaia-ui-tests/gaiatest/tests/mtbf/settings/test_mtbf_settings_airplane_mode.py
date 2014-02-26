# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestAirplaneMode(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.data_layer.disable_wifi()
        self.data_layer.connect_to_cell_data()
        self.data_layer.connect_to_wifi()
        self.data_layer.set_setting('geolocation.enabled', 'true')

        self.app_id = self.launch_by_touch("Settings")
        self.settings = Settings(self.marionette)
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_toggle_airplane_mode(self):

        # Switch on Airplane mode
        self.settings.toggle_airplane_mode()

        # wait for wifi to be disabled, this takes the longest when airplane mode is switched on
        self.wait_for_condition(lambda s: 'Disabled' in self.settings.wifi_menu_item_description)

        # check Wifi is disabled
        self.assertFalse(self.data_layer.is_wifi_connected(self.testvars['wifi']), "WiFi was still connected after switching on Airplane mode")

        # check that Cell Data is disabled
        self.assertFalse(self.data_layer.get_setting('ril.data.enabled'), "Cell Data was still connected after switching on Airplane mode")

        # check GPS is disabled
        self.assertFalse(self.data_layer.get_setting('geolocation.enabled'), "GPS was still connected after switching on Airplane mode")

        # switch back to app frame
        self.apps.switch_to_displayed_app()

        # Switch off Airplane mode
        self.settings.toggle_airplane_mode()

        # Wait for wifi to be connected, because this takes the longest to connect after airplane mode is switched off
        self.wait_for_condition(lambda s: 'Connected to ' + self.testvars['wifi']['ssid'] in self.settings.wifi_menu_item_description, timeout=40)

        # check Wifi is enabled
        self.assertTrue(self.data_layer.is_wifi_connected(self.testvars['wifi']), "WiFi was not connected after switching off Airplane mode")

        # check that Cell Data is enabled
        self.assertTrue(self.data_layer.get_setting('ril.data.enabled'), "Cell data was not connected after switching off Airplane mode")

        # check GPS is enabled
        self.assertTrue(self.data_layer.get_setting('geolocation.enabled'), "GPS was not enabled after switching off Airplane mode")

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
