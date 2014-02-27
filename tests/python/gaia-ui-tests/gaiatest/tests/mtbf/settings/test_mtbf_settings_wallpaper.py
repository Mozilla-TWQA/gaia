# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestWallpaper(GaiaMtbfTestCase):

    # default wallpaper
    _default_wallpaper_src = None

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.settings = Settings(self.marionette)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_change_wallpaper(self):
        # https://moztrap.mozilla.org/manage/case/3449/

        display_settings = self.settings.open_display_settings()

        self._default_wallpaper_src = display_settings.wallpaper_preview_src

        display_settings.choose_wallpaper(3)

        self.assertNotEqual(display_settings.wallpaper_preview_src[0:24], self._default_wallpaper_src[0:24])

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
