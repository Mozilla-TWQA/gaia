# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase

from gaiatest.apps.phone.app import Phone
from gaiatest.mtbf_apps.phone.app import MTBF_Phone
from marionette.errors import JavascriptException


class TestDialerAirplaneMode(GaiaMtbfTestCase):

    def setUp(self):

        GaiaMtbfTestCase.setUp(self)

        self.phone = Phone(self.marionette)
        self.mtbf_phone = MTBF_Phone(self.marionette)
        self.phone.launch()

    def test_dialer_airplane_mode(self):
        # https://moztrap.mozilla.org/manage/case/2282/

        # Disable the device radio, enable Airplane mode
        self.data_layer.set_setting('airplaneMode.enabled', True)
        time.sleep(5)

        # Check that we are in Airplane mode
        self.assertTrue(self.data_layer.get_setting('airplaneMode.enabled'))

        # Make a call
        test_phone_number = self.testvars['remote_phone_number']
        self.phone.keypad.dial_phone_number(test_phone_number)
        self.phone.keypad.tap_call_button(switch_to_call_screen=False)

        # Check for the Airplane mode dialog
        self.phone.wait_for_confirmation_dialog()

        # Verify the correct dialog text for the case
        self.assertEqual("Airplane mode activated", self.phone.confirmation_dialog_text)
        self.marionette.find_element('xpath', '//button[text()="OK"]').tap()

        # Verify that there is no active telephony state; window.navigator.mozTelephony.active is null
        self.assertRaises(JavascriptException, self.marionette.execute_script,
                          "return window.navigator.mozTelephony.active.state;")

    def tearDown(self):
        self.data_layer.set_setting('airplaneMode.enabled', False)
        time.sleep(5)

        self.marionette.switch_to_frame()
        self.marionette.switch_to_frame(self.phone.app.frame_id)
        self.phone.tap_keypad_toolbar_button()

        GaiaMtbfTestCase.tearDown(self)
