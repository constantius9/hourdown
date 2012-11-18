#!/usr/bin/env python

"""Unit test for the main module of the 'hourdown'"""

import mock
import unittest
from StringIO import StringIO
import datetime as dt
import sys

import main


class StdoutOutputTestCase(unittest.TestCase):
    """Tests whether the stuff is printed correctly."""

    def setUp(self):
        sys.stdout = self.captured = StringIO()

    def test_show_info(self):
        pass

    def test_show_actions(self):
        main.print_actions()
        self.assertEquals(self.captured,
            """Choose action:
            1 - Set time/date
            2 - Add a project
            3 - Journal time spending
            4 - Show journal
            5 - Exit
            """)

    def tearDown(self):
        sys.stdout = sys.__stdout__


class InputReactionTestCase(unittest.TestCase):
    """Tests whether the user input is handled correctly."""    

    @mock.patch('__builtin__.raw_input')
    def test_inquiry(self, raw_input):
        """Tests user interaction"""

        patcher = mock.patch('sys.stdout')
        patcher.start()
        patcher2 = mock.patch('datetime.datetime')
        patcher2.start()

        raw_input.return_value = '1'
        choice = main.inquiry(hours_left=100, date_time=dt.datetime.now())
        self.assertEquals(choice, '1')
        raw_input.return_value = '2'
        choice = main.inquiry(hours_left=100, date_time=dt.datetime.now())
        self.assertEquals(choice, '2')
        raw_input.return_value = '3'
        choice = main.inquiry(hours_left=100, date_time=dt.datetime.now())
        self.assertEquals(choice, '3')
        raw_input.return_value = '4'
        choice = main.inquiry(hours_left=100, date_time=dt.datetime.now())
        self.assertEquals(choice, '4')
        raw_input.return_value = '5'
        choice = main.inquiry(hours_left=100, date_time=dt.datetime.now())
        self.assertEquals(choice, '5')

        patcher.stop()
        patcher2.stop()

    def test_dispatch(self):
        pass


if __name__ == "__main__":
    unittest.main()
