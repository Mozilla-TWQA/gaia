# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.calendar.app import Calendar


class TestCalendar(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.today = datetime.date.today()
        # Determine the name and the year of the next month
        self.next_month_year = self.today.replace(day=1) + datetime.timedelta(days=32)

        self.calendar = Calendar(self.marionette)
        self.calendar.launch()

    def test_calendar_flick_through_months(self):
        # https://bugzilla.mozilla.org/show_bug.cgi?id=937085

        MONTH_YEAR_PATTERN = '%B %Y'

        self.calendar.flick_to_next_month()
        self.assertEquals(self.next_month_year.strftime(MONTH_YEAR_PATTERN),
                          self.calendar.current_month_year)

        self.calendar.flick_to_previous_month()
        self.assertEquals(self.today.strftime(MONTH_YEAR_PATTERN), self.calendar.current_month_year)


    def tearDown(self):
        self.calendar.tap_today_display_button()
        GaiaMtbfTestCase.tearDown(self)
