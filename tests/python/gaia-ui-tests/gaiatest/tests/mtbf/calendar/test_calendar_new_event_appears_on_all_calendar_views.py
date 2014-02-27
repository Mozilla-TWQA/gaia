# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime, timedelta

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.calendar.app import Calendar


class TestCalendar(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        
        self.calendar = Calendar(self.marionette)
        self.calendar.launch()

    def test_that_new_event_appears_on_all_calendar_views(self):

        # We get the actual time of the device
        _seconds_since_epoch = self.marionette.execute_script("return Date.now();")
        now = datetime.utcfromtimestamp(_seconds_since_epoch / 1000)

        # We know that the default event time will be rounded up 1 hour
        event_start_date_time = now + timedelta(hours=1)

        event_title = 'Event Title %s' % str(event_start_date_time.time())
        event_location = 'Event Location %s' % str(event_start_date_time.time())

        new_event = self.calendar.tap_add_event_button()

        # create a new event
        new_event.fill_event_title(event_title)
        new_event.fill_event_location(event_location)

        new_event.tap_save_event()

        # assert that the event is displayed as expected in month view
        self.assertIn(event_title, self.calendar.displayed_1st_event_text_in_month_view(event_start_date_time))
        self.assertIn(event_location, self.calendar.displayed_1st_event_text_in_month_view(event_start_date_time))

        # switch to the week display
        self.calendar.tap_week_display_button()
        self.assertIn(event_title, self.calendar.displayed_1st_event_text_in_week_view(event_start_date_time))

        # switch to the day display
        self.calendar.tap_day_display_button()
        self.assertIn(event_title, self.calendar.displayed_1st_event_text_in_day_view(event_start_date_time))
        self.assertIn(event_location, self.calendar.displayed_1st_event_text_in_day_view(event_start_date_time))

        # for clean up
        self.event_start_date_time = event_start_date_time

    def tearDown(self):
        # Clean up
        self.calendar.tap_month_display_button()
        events = self.calendar.displayed_events_in_month_view(self.event_start_date_time)
        # Usually, only has one event and it's hard-coded.
        # If necessary, fix it by reloading and enumerating events.

        # The event index is from 1, not 0.
        first_event = self.calendar.tap_first_event(events)
        first_event.tap_edit_event()
        first_event.tap_delete_event()

        GaiaMtbfTestCase.tearDown(self)
