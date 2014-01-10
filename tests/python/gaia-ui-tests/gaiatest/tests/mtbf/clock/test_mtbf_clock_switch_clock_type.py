# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.clock.app import Clock
import time


class TestClockSwitchClockType(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.clock = Clock(self.marionette)
        self.app_id = self.launch_by_touch("Clock")
        time.sleep(5)

        if len(self.marionette.find_elements('id', 'alarm-close')) > 0:
            if self.marionette.find_element('id', 'alarm-close').is_displayed():
                self.marionette.find_element('id', 'alarm-close').tap()
        if len(self.marionette.find_elements('id', 'alarm-tab')) > 0:
            self.wait_for_element_displayed('id', 'alarm-tab')
            self.marionette.find_element('id', 'alarm-tab').tap()

    def test_clock_switch_clock_type_and_show_time_date(self):
        """ Switch the clock type and show time and date
        https://moztrap.mozilla.org/manage/case/1770
        https://moztrap.mozilla.org/manage/case/1771
        """

        # switch to digital clock and check the date, time, state for digital clock
        if self.clock.is_analog_clock_displayed:
            self.clock.tap_analog_display()
        self.assertTrue(self.clock.is_digital_clock_displayed, "The digital clock should be displayed.")
        self.assertTrue(self.clock.is_day_and_date_displayed, "The date of digital clock should be displayed.")
        self.assertTrue(self.clock.is_24_hour_state_displayed, "The hour24-state of digital clock should be displayed.")

        # switch to analog clock and check the date, time for analog clock
        self.clock.tap_digital_display()
        self.assertTrue(self.clock.is_analog_clock_displayed, "The analog clock should be displayed.")
        self.assertTrue(self.clock.is_day_and_date_displayed, "The date of digital clock should be displayed.")
        self.assertFalse(self.clock.is_24_hour_state_displayed, "The hour24-state of digital clock should be displayed.")
