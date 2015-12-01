# This file is part of the sale_pos_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SalePosSalesmanTestCase(ModuleTestCase):
    'Test Sale Pos Salesman module'
    module = 'sale_pos_salesman'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SalePosSalesmanTestCase))
    return suite