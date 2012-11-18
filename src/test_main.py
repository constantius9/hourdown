#!/usr/bin/env python

"""Unit test for the main module of the 'hourdown'"""

import mock
import unittest
from StringIO import StringIO
import datetime as dt
import sys
from textwrap import dedent

import main


class StdoutOutputTestCase(unittest.TestCase):
    """Tests whether the stuff is printed correctly."""

    def setUp(self):
        self.patcher_stdout = mock.patch('sys.stdout', StringIO())
        self.patcher_stdout.start()

    def test_show_info(self):
        patcher_datetime = mock.patch('datetime.datetime')
        patcher_datetime.start()
        date, hours_left = dt.datetime.now(), 100
        s = "You have {0} hours left. Set date is {1}.\n".format(
            hours_left, date)
        main.print_info(date, hours_left)
        self.assertEquals(sys.stdout.getvalue(), s)
        patcher_datetime.stop()
        sys.stdout.truncate(0)

    def test_show_actions(self):
        main.print_actions()
        s = """
            Choose action:
                1 - Set time/date
                2 - Add a project
                3 - Journal time spending
                4 - Show journal
                5 - Exit
            """
        self.assertEquals(sys.stdout.getvalue(), dedent(s))
        sys.stdout.truncate(0)

    def tearDown(self):
        self.patcher_stdout.stop()


class InputReactionTestCase(unittest.TestCase):
    """Tests whether the user input is handled correctly."""    

    @mock.patch('__builtin__.raw_input')
    def test_inquiry(self, raw_input):
        """Tests user interaction"""

        patcher_stdout = mock.patch('sys.stdout')
        patcher_stdout.start()
        patcher_datetime = mock.patch('datetime.datetime')
        patcher_datetime.start()

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

        patcher_stdout.stop()
        patcher_datetime.stop()

    def test_dispatch(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(StdoutOutputTestCase)
    suite.addTest(InputReactionTestCase)
    return suite


if __name__ == "__main__":
    unittest.main()
