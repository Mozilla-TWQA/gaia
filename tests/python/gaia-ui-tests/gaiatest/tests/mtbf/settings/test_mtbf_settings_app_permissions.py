# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestAppPermissions(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_open_app_permissions(self):

        app_permissions_settings = self.settings.open_app_permissions_settings()

        # Tap on the app to open permissions details
        app_permissions_details = app_permissions_settings.tap_app('Homescreen')

        # Verify the permission is listed
        self.assertTrue(app_permissions_details.is_geolocation_listed)

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
