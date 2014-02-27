# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.calendar.app import Calendar


class TestCalendar(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.calendar = Calendar(self.marionette)
        self.calendar.launch()

    def test_check_today_date(self):

        # We get the actual time of the device
        _seconds_since_epoch = self.marionette.execute_script("return Date.now();")
        now = datetime.utcfromtimestamp(_seconds_since_epoch / 1000)

        self.assertEquals(now.strftime('%B %Y'), self.calendar.current_month_year)
        self.assertIn(now.strftime('%a %b %d %Y'), self.calendar.current_month_day)

    def tearDown(self):
        
        GaiaMtbfTestCase.tearDown(self)
