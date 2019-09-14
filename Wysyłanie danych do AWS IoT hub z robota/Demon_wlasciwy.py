#!/usr/bin/env python
import os
import basicPubSub
import threading
import time
import ReadRtdeData
import logMonitor
from _ast import If

class TestThread(threading.Thread):

    def __init__(self, name='TestThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
        self.LogLEN = 0
        self.LogInterval = 10#120 #interwal wysylania logow
        self.RTDEInterval = 5#20 #interwal wysylania danych procesowych robota
        self.timer = False
        self.timer2 = False
        self.daemonEnabled = True
        self.NewLogs = []
        self.RTDEPublishResult = True
        self.LogsPublishResult = True
        
    def sendLogs(self): 
        self.NewLogs, self.LogLEN = logMonitor.checkForNewLogs(self.LogLEN)  #Czytanie loga
        basicPubSub.publishPG_LOG("URPM-SN"+str(self.read_UR_SN()), self.NewLogs, self.read_UR_SN())
        self.timer = threading.Timer(self.LogInterval,self.sendLogs)
        self.timer.start()
    
    def sendRTDE(self):
        basicPubSub.publishPG_RTDE("URPM-SN"+str(self.read_UR_SN()), ReadRtdeData.odczyt_parametrow(), self.read_UR_SN())
        self.timer2 = threading.Timer(self.RTDEInterval,self.sendRTDE)
        self.timer2.start()
            
    def checkIfEnable(self):
        return self.daemonEnabled
        
    def read_UR_SN(self): #Odczyt numeru seryjnego robota
        output = os.popen("hostname").read()
        serial = output.strip("ur-")
        serial = serial.strip("/n")
        serial = serial.rstrip()
        return serial
    
    def run(self):
        """ main control loop """
        print "%s starts" % (self.getName(  ),)

        print "Wait 10 s to send data to cloud "
        time.sleep(10)
        self.LogLEN = logMonitor.readLogLen()    #Sprawdza dlugosc logu zapisana w pliku
        self.sendLogs()  #pierwsze wywolanie wysylania, potem automatycznie sie wysyla w interwale
        self.sendRTDE()  #pierwsze wywolanie wysylania, potem automatycznie sie wysyla w interwale
        
        while not self._stopevent.isSet():
            self._stopevent.wait(self._sleepperiod)
            time.sleep(10)
        print "%s ends" % (self.getName(  ),)

    def join(self, timeout=None):
        self.daemonEnabled = False
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)