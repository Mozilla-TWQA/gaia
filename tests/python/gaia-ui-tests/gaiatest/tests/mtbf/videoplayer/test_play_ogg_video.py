# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.videoplayer.app import VideoPlayer


class TestPlayOGGVideo(GaiaMtbfTestCase):

    def setUp(self):
        time.sleep(5)
        GaiaMtbfTestCase.setUp(self)

        # add video to storage
        self.push_resource('VID_0001.ogg', destination='DCIM/100MZLLA')

        self.video_player = VideoPlayer(self.marionette)
        self.video_player.launch()
        self.marionette.refresh()
        self.apps.switch_to_displayed_app()
        self.wait_for_element_displayed('css selector', 'div.img')

    def test_play_ogg_video(self):
        """https://moztrap.mozilla.org/manage/case/2478/"""

        # video_player.wait_for_progress_bar_complete()

        # Assert that there is at least one video available
        self.assertGreater(self.video_player.total_video_count, 0)

        first_video_name = self.video_player.first_video_name

        # Click on the first video.
        fullscreen_video = self.video_player.tap_first_video_item()

        # Video will play automatically
        # We'll wait for the controls to clear so we're 'safe' to proceed
        time.sleep(2)

        # We cannot tap the toolbar so let's just enable it with javascript
        fullscreen_video.display_controls_with_js()

        # The elapsed time > 0:00 denote the video is playing
        zero_time = time.strptime('00:00', '%M:%S')
        self.assertGreater(fullscreen_video.elapsed_time, zero_time)

        # Check the name too. This will only work if the toolbar is visible.
        self.assertEqual(first_video_name, fullscreen_video.name)

    def tearDown(self):
        self.marionette.find_element('id', 'thumbnails-single-delete-button').tap()
       
        self.wait_for_element_displayed('css selector', 'button.modal-dialog-confirm-ok.confirm')
        self.marionette.find_element('css selector', 'button.modal-dialog-confirm-ok.confirm').tap()
        GaiaMtbfTestCase.tearDown(self)
