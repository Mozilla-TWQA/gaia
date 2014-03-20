# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsGPS(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

        # make sure GPS is on for the beginning of the test
        self.data_layer.set_setting('geolocation.enabled', 'true')

    def test_enable_gps_via_settings_app(self):
        """ Enable GPS via the Settings app

        https://moztrap.mozilla.org/manage/case/2885/

        """

        # should be on by default
        self.wait_for_condition(lambda m: self.settings.is_gps_enabled)

        # turn off
        self.settings.disable_gps()

        # should be off
        self.assertFalse(self.data_layer.get_setting('geolocation.enabled'), "GPS was not enabled via Settings app")

        # turn back on
        self.settings.enable_gps()

        # should be on
        self.assertTrue(self.data_layer.get_setting('geolocation.enabled'), "GPS was not disabled via Settings app")

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
