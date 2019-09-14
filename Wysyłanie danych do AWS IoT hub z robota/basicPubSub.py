'''
/*
 * Skrypt zmodyfikowany
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''
import sys, os, time

#Aktywuje kozystanie z wirtualnego srodowiska z zainstalowanymi bibliotekami
activate_this = 'venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import argparse
import json
import datetime

ROOTCA = "Cert/AmazonRootCA1.pem.txt"          #Certyfiakty
CRT = "Cert/ff46d06c4c-certificate.pem.crt"
KEY = "Cert/ff46d06c4c-private.pem.key"
HOST = "Tu był endpoint"
PORT = "8883"


def publishPG_LOG(clientId, newLogs, ROBO_SN):
    #parametry:
    host = HOST
    port = PORT
    rootca = ROOTCA
    crt = CRT
    key = KEY
    
    
    # Init AWSIoTMQTTClient
    myAWSIoTMQTTClient = None
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootca, key, crt)
    
    
    # AWSIoTMQTTClient connection configuration
    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    
    # Connect to AWS IoT
    while True:
        try:
            myAWSIoTMQTTClient.connect()
        except:
            print "PG:error, unable connect to broker"
            time.sleep(5)
            continue
        break
    

    #Wysylanie wiadomosci z nowymi logami
    if newLogs: 
        topic = "/URPM/"+ROBO_SN+"/Logs"
        message = {}
        message['Timestamp'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        message['RobotLogs'] = newLogs
        messageJson = json.dumps(message)
        print 'Zawartosc message json: ',messageJson
        print 'topic: ', topic
        result = myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        print 'Published topic %s: %s\n' % (topic, messageJson)
        print 'Send result: ',result
    else:
        print "There was no new logs"
        result = False
    myAWSIoTMQTTClient.disconnect()
    return result
    
    
def publishPG_RTDE(clientId, RTDEdata, ROBO_SN):
    #parametry:
    host = HOST
    port = PORT
    rootca = ROOTCA
    crt = CRT
    key = KEY
    
    # Init AWSIoTMQTTClient
    myAWSIoTMQTTClient = None
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootca, key, crt)
    
    
    # AWSIoTMQTTClient connection configuration
    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    
    # Connect to AWS IoT
    while True:
        try:
            myAWSIoTMQTTClient.connect()
        except:
            print "PG:error, unable connect to broker"
            time.sleep(5)
            continue
        break
    
    #Wysylanie wiadomosci z danymi RTDE
    topic = "/URPM/"+ROBO_SN+"/RTDEdata"
    message = {}
    message['Timestamp'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    message['RobotProcessData'] = RTDEdata
    messageJson = json.dumps(message)
    print 'Zawartosc message json: ',messageJson
    print 'topic: ', topic
    try:
        result = myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    except:
        result = False
        print 'Publish failed!'
    print 'Published topic %s: %s\n' % (topic, messageJson)
    print 'Wynik wyslania: ',result
    myAWSIoTMQTTClient.disconnect()
    return result


if __name__ == "__main__":
    #Aktywuje kozystanie z wirtualnego srodowiska z zainstalowanymi bibliotekami
    activate_this = 'venv/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))
    RTDEdata = {"WaznaWartosc1RTDE":123,"WaznaWartosc2RTDE":456,"WaznaWartosc3RTDE":789}
    newLogs = ["To jest sciemniony wpis logu\n", "a to kolejny\n", "No to moze jescze jedne :)\n"]
    publishPG_LOG("TESTPG", RTDEdata ,"14100715")