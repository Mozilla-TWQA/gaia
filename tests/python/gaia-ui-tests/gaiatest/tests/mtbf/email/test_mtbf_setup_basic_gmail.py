# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette import SkipTest

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.email.app import Email
import time

class TestSetupGmail(GaiaMtbfTestCase):

    def setUp(self):
        try:
            self.testvars['email']['gmail']
        except KeyError:
            raise SkipTest('account details not present in test variables')

        GaiaMtbfTestCase.setUp(self)
        self.connect_to_network()

        self.email = Email(self.marionette)
        self.email.launch()

    def test_setup_basic_gmail(self):
        # setup basic gmail account
        self.email.basic_setup_email(self.testvars['email']['gmail']['name'],
                                     self.testvars['email']['gmail']['email'],
                                     self.testvars['email']['gmail']['password'])

        # check header area
        self.assertTrue(self.email.header.is_compose_visible)
        self.assertTrue(self.email.header.is_menu_visible)
        self.assertEqual(self.email.header.label, 'Inbox')

        # check toolbar area
        self.assertTrue(self.email.toolbar.is_edit_visible)
        self.assertTrue(self.email.toolbar.is_refresh_visible)

        # check account has emails
        self.email.wait_for_emails_to_sync()
        self.assertGreater(len(self.email.mails), 0)

    def tearDown(self):
	self.email.delete_top_email_account()
	GaiaMtbfTestCase.tearDown(self)
