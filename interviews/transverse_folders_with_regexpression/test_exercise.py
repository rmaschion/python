import os,sys

import logging
from transverse_dir import TransverseDir
import unittest

class TestRegularExpressionCount(unittest.TestCase):
    """
    Overview:   Validates Regular Expression Count class
    Approach:   Executes positive testcases expecting the plot graph be displayed at end
                Executes negative testcases expecting handled exceptions
    Disclaimer: Not all possible or recommended tests were implemented in this exercise

                Code developed expecifically for this exercise.
    """
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)

    def setUp(self):
        self.logger.addHandler(self.stream_handler)
        self.logger.info("*" * 5 + "TRANSVERSE DIR TEST SUITE - STARTED" + "*" * 5)
        self.transverse = TransverseDir("./test")

    def test1_positive_test(self):
        self.transverse.compile_regular_expression(("Logfile"))
        self.transverse.walkdir()
        testResult = self.transverse.get_results_list()
        self.assertTrue(isinstance(testResult, dict), "Expected a dictionary as test results")
        self.transverse.print_results()
        self.transverse.plot_results()

    def test2_bad_regExpression_test(self):
        self.transverse.compile_regular_expression(("*&&^()(#()test"))
        self.transverse.walkdir()
        testResult = self.transverse.get_results_list()
        self.assertTrue(isinstance(testResult, dict), "Expected a dictionary as test results")
        self.transverse.print_results()
        self.transverse.plot_results()

    def test3_bad_root_path_test(self):
        self.transverse.root_dir = "/notexistent"
        self.transverse.compile_regular_expression(("Logfile"))
        self.transverse.walkdir()
        testResult = self.transverse.get_results_list()
        self.assertTrue(len(testResult), "No result was found")
        self.transverse.walkdir()
        self.transverse.print_results()
        self.transverse.plot_results()

    def tearDown(self):
        self.logger.info("*" * 5 + "TRANSVERSE DIR TEST SUITE - ENDED" + "*" * 5)
        self.logger.removeHandler(self.stream_handler)


if __name__ == '__main__':
    unittest.main()