# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.homescreen.app import Homescreen
import time

class TestEverythingMeLaunchApp(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        self.connect_to_network()

    def test_launch_everything_me_app(self):
        # https://github.com/mozilla/gaia-ui-tests/issues/69

        app_name = ['Twitter','Flickr','Linkedin']
        homescreen = Homescreen(self.marionette)
        self.apps.switch_to_displayed_app()

        for index in range(0,len(app_name)):
        	search_panel = homescreen.tap_search_bar()
        	search_panel.wait_for_everything_me_loaded()
		search_panel.type_into_search_box(app_name[index])
		search_panel.wait_for_everything_me_results_to_load()
		results = search_panel.results

		if app_name[index] == results[0].name:
			results[0].tap()
			homescreen.touch_home_button()
			time.sleep(1)
			homescreen.touch_home_button() 
    
    def tearDown(self):
	GaiaMtbfTestCase.tearDown(self)
