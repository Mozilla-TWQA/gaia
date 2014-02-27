# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsDoNotTrack(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

        # make sure Do Not Track is off for the beginning of the test
        self.data_layer.set_setting('privacy.donottrackheader.enabled', False)
        self.settings = Settings(self.marionette)

    def test_enable_do_not_track_via_settings_app(self):
        """Enable do not track via the Settings app"""

        do_not_track_settings = self.settings.open_do_not_track_settings()

        # turn to "disallow tracking"
        do_not_track_settings.tap_disallow_tracking()

        # should be enabled
        self.assertEqual(self.data_layer.get_bool_pref('privacy.donottrackheader.enabled'), True)
        # should be 1
        self.assertEqual(self.data_layer.get_int_pref('privacy.donottrackheader.value'), 1)

        # turn to "allow tracking"
        do_not_track_settings.tap_allow_tracking()

        # should be enabled
        self.assertEqual(self.data_layer.get_bool_pref('privacy.donottrackheader.enabled'), True)
        # should be 0
        self.assertEqual(self.data_layer.get_int_pref('privacy.donottrackheader.value'), 0)

        # turn back to "no pref"
        do_not_track_settings.tap_do_not_have_pref_on_tracking()

        # should be disabled
        self.assertEqual(self.data_layer.get_bool_pref('privacy.donottrackheader.enabled'), False)
        # should be back to "no pref"
        self.assertEqual(self.data_layer.get_int_pref('privacy.donottrackheader.value'), -1)

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)