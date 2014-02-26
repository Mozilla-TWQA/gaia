# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsPasscode(GaiaMtbfTestCase):

    # Input data
    _input_passcode = ['7', '9', '3', '1']

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)
        self.app_id = self.launch_by_touch("Settings")
        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()
        self.settings = Settings(self.marionette)

    def test_set_passcode_by_settings(self):
        """ Set a passcode using Settings app

        https://github.com/mozilla/gaia-ui-tests/issues/477

        """

        phone_lock_settings = self.settings.open_phone_lock_settings()

        phone_lock_settings.enable_passcode_lock()
        phone_lock_settings.create_passcode(self._input_passcode)

        passcode_code = self.data_layer.get_setting('lockscreen.passcode-lock.code')
        passcode_enabled = self.data_layer.get_setting('lockscreen.passcode-lock.enabled')
        self.assertEqual(passcode_code, "".join(self._input_passcode), 'Passcode is "%s", not "%s"' % (passcode_code, "".join(self._input_passcode)))
        self.assertEqual(passcode_enabled, True, 'Passcode is not enabled.')

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
