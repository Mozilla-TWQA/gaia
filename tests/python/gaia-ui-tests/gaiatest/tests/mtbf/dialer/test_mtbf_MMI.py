# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from MtbfTestCase import GaiaMtbfTestCase

from gaiatest.apps.phone.app import Phone
from gaiatest.mtbf_apps.phone.app import MTBF_Phone
from gaiatest.apps.phone.regions.attention_screen import AttentionScreen

IMEI_CODE = "*#06#"
CALL_FORWARDING_CODE = "*#21#"


class TestMMI(GaiaMtbfTestCase):

    def setUp(self):
        time.sleep(5)
        GaiaMtbfTestCase.setUp(self)

        self.phone = Phone(self.marionette)
        self.mtbf_phone = MTBF_Phone(self.marionette)
        self.phone.launch()

    def test_MMI_code_IMEI(self):
        # Dial the code
        self.phone.keypad.dial_phone_number(IMEI_CODE)

        attention_screen = AttentionScreen(self.marionette)
        self.assertEqual(attention_screen.message, self.testvars['imei'])

    def tearDown(self):
        # Close the imei message prompt
        self.marionette.switch_to_frame()
        self.marionette.switch_to_frame(self.phone.app.frame_id)
        self.marionette.find_element('id', 'mmi-close').tap()
        self.phone.tap_keypad_toolbar_button()

        GaiaMtbfTestCase.tearDown(self)
