# -*- coding: utf-8 -*-

"""
    tests.controllers.controller_test_base

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import unittest
from ..http_response_catcher import HttpResponseCatcher
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.configuration import Configuration

class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.api_client = MessageMediaMessagesClient()
        cls.request_timeout = 30
        cls.assert_precision = 0.01


    def setUp(self):
        """Method called once before every test in a test class."""
        self.response_catcher = HttpResponseCatcher()
        self.controller.http_call_back =  self.response_catcher

    