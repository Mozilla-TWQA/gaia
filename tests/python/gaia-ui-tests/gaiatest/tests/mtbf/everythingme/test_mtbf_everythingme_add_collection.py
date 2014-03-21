# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.homescreen.app import Homescreen
from gaiatest.apps.homescreen.app import InstalledApp
import time

class TestEverythingMeAddCollection(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        self.connect_to_network()

    def test_everythingme_add_collection(self):

        homescreen = Homescreen(self.marionette)
	installedapp = InstalledApp(self.marionette,0)
	self.apps.switch_to_displayed_app()

        # For MTBF
	selected_item = ['Answers','Around Me','Arts & Crafts','Astrology','Autos','Work','Weddings']
	for index in range(len(selected_item)):
	        homescreen.open_context_menu().tap_add_collection()
        	time.sleep(3)
		homescreen.select(selected_item[index])
     		self.assertTrue(homescreen.is_app_installed(selected_item[index]),
                       "App %s not found on Homescreen" % selected_item[index])
	
	installedapp.tap_delete_collections()

    def tearDown(self):
	GaiaMtbfTestCase.tearDown(self)

