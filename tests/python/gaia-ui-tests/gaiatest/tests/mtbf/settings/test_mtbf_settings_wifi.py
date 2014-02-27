# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsWifi(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()
        self.data_layer.disable_wifi()
        self.settings = Settings(self.marionette)

    def test_connect_to_wifi_via_settings_app(self):
        """ Connect to a wifi network via the Settings app

        https://github.com/mozilla/gaia-ui-tests/issues/342

        """
        self.marionette.switch_to_frame()
        self.marionette.switch_to_frame(self.app_id)
        self.wait_for_condition(lambda m: m.find_element('id', 'wifi-desc').text != '')
        wifi_settings = self.settings.open_wifi_settings()

        wifi_settings.enable_wifi()
        wifi_settings.connect_to_network(self.testvars['wifi'])

        # verify that wifi is now on
        self.assertTrue(self.data_layer.is_wifi_connected(self.testvars['wifi']), "WiFi was not connected via Settings app")

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
