#!/usr/bin/env python

"""Unit test for the main module of the 'hourdown'"""

import mock
import unittest

import main
import datetime as dt


class InputReactionTestCase(unittest.TestCase):
    
    @mock.patch('__builtin__.raw_input')
    def test_inquiry(self, raw_input):
        """Tests user interaction"""

        patcher = mock.patch('sys.stdout')
        patcher.start()

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


if __name__ == "__main__":
    unittest.main()
