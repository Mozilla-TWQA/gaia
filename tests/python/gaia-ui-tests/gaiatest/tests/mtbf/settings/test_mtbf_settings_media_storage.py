# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsMediaStorage(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_settings_media_storage(self):
        media_storage_settings = self.settings.open_media_storage_settings()

        # Check that no media is on the device
        self.assertEqual(media_storage_settings.music_size, '0 B')
        self.assertEqual(media_storage_settings.pictures_size, '0 B')
        self.assertEqual(media_storage_settings.movies_size, '0 B')

        # Push media to the device
        self.push_resource('VID_0001.3gp', destination='DCIM/100MZLLA')
        self.push_resource('IMG_0001.jpg', destination='DCIM/100MZLLA')
        self.push_resource('MUS_0001.mp3', destination='DCIM/100MZLLA')

        # Access 'Media storage' in Settings
        self.mtbf_settings.back_to_main_screen()
        self.marionette.refresh()
        media_storage_settings = self.settings.open_media_storage_settings()

        # Check that media storage has updated to reflect the newly pushed media
        self.assertEqual(media_storage_settings.music_size, '120 KB')
        self.assertEqual(media_storage_settings.pictures_size, '348 KB')
        self.assertEqual(media_storage_settings.movies_size, '120 KB')

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
