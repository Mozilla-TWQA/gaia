# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.homescreen.app import Homescreen
import time

class TestEverythingMeSearchPanel(GaiaMtbfTestCase):


    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

    def test_launch_packaged_app_from_search_panel(self):
        """Launch packaged app from homescreen search panel.

        https://github.com/mozilla/gaia-ui-tests/issues/1169
        """
        app_name = 'Calendar'
	homescreen = Homescreen(self.marionette)
        self.apps.switch_to_displayed_app()

        search_panel = homescreen.tap_search_bar()
        search_panel.wait_for_everything_me_loaded()
        search_panel.type_into_search_box(app_name)

        results = search_panel.installed_apps
	self.assertEqual(results[0].name, app_name)
        results[0].tap()

        self.assertEqual(self.apps.displayed_app.name.lower(), app_name.lower())

    def tearDown(self):
	GaiaMtbfTestCase.tearDown(self)
