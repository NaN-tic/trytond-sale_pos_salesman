#!/usr/bin/env python
# This file is part of the sale_pos_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

import sys
import os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class SalePOSSalesmanTestCase(unittest.TestCase):
    '''
    Test Sale POS Salesman module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_pos_salesman')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('sale_pos')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            SalePOSSalesmanTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
