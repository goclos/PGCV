#!/usr/bin/env python
# Copyright (c) 2016, Universal Robots A/S,
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Universal Robots A/S nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL UNIVERSAL ROBOTS A/S BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import logging
import time
import sys
from IN import ADJ_FREQUENCY
#sys.path.append('..')
import rtde.rtde as rtde
import rtde.rtde_config as rtde_config


def odczyt_statusu_pracy():
    host = "127.0.0.1"
    port = 30004
    config = "ReadRtdeStatus.xml" #parametry odczytywane z rabota w html
    frequency = 2
    
    logging.basicConfig(level=logging.INFO)
    
    conf = rtde_config.ConfigFile(config)
    output_names, output_types = conf.get_recipe('out')

    con = rtde.RTDE(host, port)
    con.connect()
    
    # get controller version
    con.get_controller_version()
    
    # setup recipes
    if not con.send_output_setup(output_names, output_types, frequency):
        logging.error('Unable to configure output')
        sys.exit()
    
    #start data synchronization
    if not con.send_start():
        print 'Unable to start synchronization'
        sys.exit()

    try:
        state = con.receive() #odczyt odebranych danych
        if state is not None:
            Robot_data = konwersja_danych(state, output_names) #Konwersja danych z obiektu state do slownika parametr:wartosc
    except:
        logging.error("Read RTDE status failed \n Next attempt in 3 s")
            
    
    sys.stdout.write("\rRead RTDE status Data Complete!            \n")
    con.send_pause()
    con.disconnect()
    #print Robot_data
    Robot_data = Robot_data["robot_status_bits"]
    #print type(Robot_data)
    #print Robot_data
    return Robot_data


def konwersja_danych(RTDEdata, paraName): # Fucnkja zwraca slownik z danymi procesowymi z robota
    RobotData = {}
    #print paraName
    for element in paraName:
        RobotData [element] = getattr(RTDEdata, element)
    return RobotData


def odczyt_parametrow():
    host = "127.0.0.1"
    port = 30004
    config = "ReadRtdeConf.xml" #parametry odczytywane z rabota w html
    frequency = 100
    logging.basicConfig(level=logging.INFO)
    conf = rtde_config.ConfigFile(config)
    output_names, output_types = conf.get_recipe('out')
    Robot_data = {}
    con = rtde.RTDE(host, port)
    
    while True:
        try:
            con.connect()   #Connection with RTDE
            con.get_controller_version() #Get version
            if not con.send_output_setup(output_names, output_types, frequency):
                logging.error('Unable to configure output, wait 3 s, and try again')
                time.sleep(3)
                continue
            if not con.send_start(): #start data synchronization
                print 'Unable to start synchronization, next try in 3 s'
                time.sleep(3)
                continue
            while True:
                try:
                    state = con.receive() #odczyt odebranych danych
                except:
                    print 'Unable to receive data'
                    time.sleep(3)
                    continue
                break
            Robot_data = konwersja_danych(state, output_names) #Konwersja danych z obiektu state do slownika parametr:wartosc
        except:
            sys.stdout.write("Connect/Read RTDE failed \nNext try in 3 s")
            time.sleep(3)
            continue
        break

    sys.stdout.write("\rRead RTDE Data Complete!            \n")
    con.send_pause()
    con.disconnect()
    #print Robot_data
    return Robot_data
    
    
if __name__ == "__main__":
    #odczyt_parametrow()
    odczyt_statusu_pracy()

