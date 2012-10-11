# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase


class TestCalculator(GaiaTestCase):

    _display_locator = ('id', 'display')
    _multiply_button_locator = ('id', 'multiply')
    _clear_button_locator = ('xpath', "//input[@value='C")
    _equals_button_locator = ('xpath', "//input[@value='=")
    _three_button_locator = ('xpath', "//input[@value='3")
    _five_button_locator = ('xpath', "//input[@value='5")

    def test_calculator_basic(self):
        # unlock the lockscreen if it's locked
        self.assertTrue(self.lockscreen.unlock())

        # launch the Calculator app
        app = self.apps.launch('Calculator')
        self.assertTrue(app.frame_id is not None)

        # switch into the Calculator's frame
        self.marionette.switch_to_frame(app.frame_id)
        url = self.marionette.get_url()
        self.assertTrue('calculator' in url, 'wrong url: %s' % url)

        # clear the calculator's display
        self.marionette.find_element(*self._clear_button_locator).click()

        # perform a 3*5 calculation
        self.marionette.find_element(*self._three_button_locator).click()
        self.marionette.find_element(*self._multiply_button_locator).click()
        self.marionette.find_element(*self._five_button_locator).click()
        self.marionette.find_element(*self._equals_button_locator).click()

        # verify the result
        display = self.marionette.find_element(*self._display_locator)
        self.assertEquals(display.text, '15', 'wrong calculated value!')

        # close the app
        self.apps.kill(app)
