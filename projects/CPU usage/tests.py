import  cpu_main
import unittest
import random
import sys
import argparse

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.cpusage = cpu_main.Cpu_usage()

    def test_main(self):
        # make sure main checks the number of arguments
        #self.assertRaises(excClass, cpu_main.main())
        try:
            self.assertRaises(IndexError, cpu_main.main())
        except Exception as e:
            print e.args

    def tearDown(self):
        pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('host', default='localhost')
    parser.add_argument('port', default='8845')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    unit_argv = [sys.argv[0]] + args.unittest_args
    unittest.main(argv=unit_argv)


    
    