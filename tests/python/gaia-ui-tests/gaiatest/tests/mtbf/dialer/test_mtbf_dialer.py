# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase

from gaiatest.apps.phone.app import Phone
from gaiatest.mtbf_apps.phone.app import MTBF_Phone


class TestDialer(GaiaMtbfTestCase):

    def setUp(self):
        time.sleep(5)
        GaiaMtbfTestCase.setUp(self)

        self.phone = Phone(self.marionette)
        self.mtbf_phone = MTBF_Phone(self.marionette)
        self.phone.launch()

    def test_dialer_make_call(self):
        # https://moztrap.mozilla.org/manage/case/1298/

        test_phone_number = self.testvars['remote_phone_number']
        call_screen = self.phone.keypad.call_number(test_phone_number)

        # Wait for call screen to be dialing
        call_screen.wait_for_outgoing_call()

        # Wait for the state to get to at least 'dialing'
        active_states = ('dialing', 'alerting', 'connecting', 'connected')
        call_screen.wait_for_condition(
            lambda m: self.data_layer.active_telephony_state in active_states,
            timeout=30)

        if len(test_phone_number) <= 12:
            # Check the number displayed is the one we dialed
            self.assertEqual(test_phone_number, call_screen.outgoing_calling_contact)
        else:
            self.assertEqual(test_phone_number[:2], call_screen.outgoing_calling_contact[:2])

    def tearDown(self):
        # Switch back to main frame before Marionette loses track bug #840931
        self.marionette.switch_to_frame()

        # In case the assertion fails this will still kill the call
        # An open call creates problems for future tests
        self.data_layer.kill_active_call()

        self.marionette.switch_to_frame()
        self.marionette.switch_to_frame(self.phone.app.frame_id)
        self.mtbf_phone.general_tear_down()

        GaiaMtbfTestCase.tearDown(self)
