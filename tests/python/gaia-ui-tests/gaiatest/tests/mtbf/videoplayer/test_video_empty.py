# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.videoplayer.app import VideoPlayer


class TestVideoEmpty(GaiaMtbfTestCase):

    def setUp(self):
        time.sleep(5)
        GaiaMtbfTestCase.setUp(self)

        self.video_player = VideoPlayer(self.marionette)
        self.video_player.launch()
        self.marionette.refresh()
        self.apps.switch_to_displayed_app()

    def test_empty_video(self):
        """https://moztrap.mozilla.org/manage/case/3660/
        Requires to be no videos on SDCard, which is the default.
        """

        # video_player.wait_for_progress_bar_not_visible()

        # Verify title when no videos
        self.assertEqual(self.video_player.empty_video_title, 'Add videos to get started')

        # Verify text when no videos
        # Note: Text will need to be updated if/when Bug 834477 is fixed
        self.assertEqual(self.video_player.empty_video_text, 'Load videos on to the memory card.')

    def tearDown(self):
        self.marionette.find_element('id', 'thumbnails-single-delete-button').tap()
       
        self.wait_for_element_displayed('css selector', 'button.modal-dialog-confirm-ok.confirm')
        self.marionette.find_element('css selector', 'button.modal-dialog-confirm-ok.confirm').tap()
        GaiaMtbfTestCase.tearDown(self)
