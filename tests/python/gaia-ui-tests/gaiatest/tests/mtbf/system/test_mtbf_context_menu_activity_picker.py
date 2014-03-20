# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.ui_tests.app import UiTests
from gaiatest.mtbf_apps.ui_tests.app import MTBF_UiTests


class TestContextMenuActivityPicker(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.ui_tests = UiTests(self.marionette)
        self.ui_tests.launch()

        self.mtbf_ui_tests = MTBF_UiTests(self.marionette)
        self.mtbf_ui_tests.back_to_main_screen()

    def test_context_menu_activity_picker(self):
        self.ui_tests.tap_ui_button()

        context_menu_page = self.ui_tests.tap_context_menu_option()
        context_menu_page.switch_to_frame()

        activities_list = context_menu_page.long_press_context_menu_body()

        self.assertTrue(activities_list.is_menu_visible)
        self.assertTrue(activities_list.options_count == 4)

        activities_list.tap_cancel()

        self.assertFalse(activities_list.is_menu_visible)

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
