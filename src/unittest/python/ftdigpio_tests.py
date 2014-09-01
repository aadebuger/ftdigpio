# -*- coding: utf-8 -*-
'''
Created on 2014年9月1日

@author: aadebuger
'''
import unittest
import ftd2xx.ftd2xx

class Test(unittest.TestCase):


    def testName(self):
        print 'ftd2xx'
        a= ftd2xx.ftd2xx.listDevices(0)
        print 'a=',a
        print 'getLibraryVersion()=',ftd2xx.ftd2xx.getLibraryVersion()
        print 'getDeviceInfoDetail=',ftd2xx.ftd2xx.getDeviceInfoDetail(0)
        myf = ftd2xx.ftd2xx.open(0)
#        myftd2xx =  ftd2xx.ftd2xx.FTD2XX(myf)
        ret = myf.getStatus()
        print 'getBitMode()=',myf.getBitMode()
        bitmask = 0x11 << 1;
        myf.setBitMode(0xff,0x20)
        
        print 'ret=',ret
        
        myf.close();
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()