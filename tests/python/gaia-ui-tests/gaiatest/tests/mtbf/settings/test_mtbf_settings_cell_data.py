# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.mtbf_apps.settings.app import MTBF_Settings
from gaiatest.apps.settings.app import Settings


class TestSettingsCellData(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.settings = Settings(self.marionette)
        self.settings.launch()

        self.mtbf_settings = MTBF_Settings(self.marionette)
        self.mtbf_settings.back_to_main_screen()

    def test_enable_cell_data_via_settings_app(self):
        """ Enable cell data via the Settings app

        https://moztrap.mozilla.org/manage/case/1373/

        """
        self.mtbf_settings.wait_for_cellanddata()
        cell_and_data_settings = self.settings.open_cell_and_data_settings()

        # verify that a carrier is displayed
        self.assertTrue(len(cell_and_data_settings.carrier_name) > 0)

        # enable cell data
        self.assertFalse(cell_and_data_settings.is_data_enabled)
        cell_data_prompt = cell_and_data_settings.enable_data()

        # deal with prompt that sometimes appears (on first setting)
        if cell_data_prompt.is_displayed:
            # Cell data should not be enabled until we turn it on via the prompt
            self.assertFalse(cell_and_data_settings.is_data_enabled)
            self.assertFalse(self.data_layer.get_setting('ril.data.enabled'), "Cell data was enabled before responding to the prompt")
            cell_data_prompt.turn_on()

        # Wait for cell data to be turned on
        self.wait_for_condition(lambda m: cell_and_data_settings.is_data_enabled)

        # verify that cell data is now enabled and connected
        self.assertTrue(self.data_layer.is_cell_data_enabled, "Cell data was not enabled via Settings app")
        self.wait_for_condition(lambda m: self.data_layer.is_cell_data_connected,
                                message="Cell data was not connected via Settings app")

    def tearDown(self):
        GaiaMtbfTestCase.tearDown(self)
