import unittest

from bootstrap.container import MockAppServicesInjector


class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.service = MockAppServicesInjector.home()

    def home_test_1_count_highlight(self):
        self.assertEqual(len(self.service.highlight()), 4)
