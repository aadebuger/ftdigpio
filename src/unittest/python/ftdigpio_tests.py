# -*- coding: utf-8 -*-
'''
Created on 2014年9月1日

@author: aadebuger
'''
import unittest
import ftd2xx.ftd2xx

class Test(unittest.TestCase):


    def testName(self):
        ftd2xx.ftd2xx.listDevices(0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()