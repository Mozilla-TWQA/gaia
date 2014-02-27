# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestChangeLanguage(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()
        self.settings = Settings(self.marionette)

    def test_change_language_settings(self):
        language_settings = self.settings.open_language_settings()

        language_settings.select_language(u'Fran\u00E7ais')

        language_settings.go_back()

        # Verify that language has changed
        self.wait_for_condition(lambda m: self.settings.header_text == u'Param\u00E8tres')
        self.assertEqual(self.data_layer.get_setting('language.current'), "fr")

    def tearDown(self):
        language_settings = self.settings.open_language_settings()
        language_settings.select_language(u'English (US)')
        language_settings.go_back()

        GaiaMtbfTestCase.tearDown(self)
