# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base
from gaiatest.apps.ui_tests.app import UiTests
import time

class MTBF_UiTests(Base):
    def __init__(self, marionette):
        Base.__init__(self, marionette)

    def back_to_main_screen(self):
        time.sleep(3)
        icon_back_sign = self.marionette.find_elements("css selector", "span.icon-back")
        icon_cancel = self.marionette.find_elements("css selector", "span.icon-close")
        icon_back = self.marionette.find_elements("id", "test-panel-back")
        recover_icons = icon_back_sign + icon_cancel + icon_back
        for icon in recover_icons:
            if icon.is_displayed():
                icon.tap()
