# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestWallpaper(GaiaMtbfTestCase):

    # default wallpaper
    _default_wallpaper_settings = None
    _new_wallpaper_settings = None

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_change_wallpaper(self):
        # https://moztrap.mozilla.org/manage/case/3449/

        display_settings = self.settings.open_display_settings()

        self._default_wallpaper_settings = self.data_layer.get_setting('wallpaper.image')

        # Open activities menu
        activities_menu = display_settings.pick_wallpaper()

        # choose the source as wallpaper app
        wallpaper = activities_menu.tap_wallpaper()
        wallpaper.tap_wallpaper_by_index(3)

        self.apps.switch_to_displayed_app()

        self._new_wallpaper_settings = self.data_layer.get_setting('wallpaper.image')

        self.assertNotEqual(self._default_wallpaper_settings, self._new_wallpaper_settings)

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
