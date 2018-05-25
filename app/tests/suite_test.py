# -*- coding: utf-8 -*-

import unittest
from tests.project import ProjectTestCase
from tests.home import HomeTestCase
from tests.bank import BankTestCase
from tests.service_project import ServiceProjectTestCase
from tests.contact import ContactTestCase
from tests.stage import StageTestCase
from tests.multimedia import MultimediaTestCase
from tests.property_type import PropertyTypeTestCase
from tests.contact_persists import ContactPersistsTestCase
from tests.operation_type import OperationTypeTestCase


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(ProjectTestCase))
    suite.addTest(loader.loadTestsFromModule(StageTestCase))
    suite.addTest(loader.loadTestsFromModule(MultimediaTestCase))
    suite.addTest(loader.loadTestsFromModule(BankTestCase))
    suite.addTests(loader.loadTestsFromModule(HomeTestCase))
    suite.addTests(loader.loadTestsFromModule(ServiceProjectTestCase))
    suite.addTest(loader.loadTestsFromModule(ContactPersistsTestCase))
    suite.addTest(loader.loadTestsFromModule(OperationTypeTestCase))
    suite.addTests(loader.loadTestsFromModule(ContactTestCase))
    suite.addTests(loader.loadTestsFromModule(PropertyTypeTestCase))
    return suite


if __name__ == '_main_':
    unittest.TextTestRunner(verbosity=2).run(suite())
