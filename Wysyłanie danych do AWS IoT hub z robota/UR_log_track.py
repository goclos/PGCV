#!/usr/bin/env python

import time
import sys
import os

#Aktywuje kozystanie z wirtualnego srodowiska z zainstalowanymi bibliotekami
activate_this = 'venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import Demon_wlasciwy


title = ""
licznik = 0


def set_title(new_title):
	global title
	title = new_title
	return title

def get_title():
	tmp = ""
	if str(title):
		tmp = title
	else:
		tmp = "No title set"
	return tmp + " (Python)"

def get_message(name):
	if str(name):
		return str(name) + ", welcome to PolyScope!" + "nazwa_pliku: "
	else:
		return "No name set"

def loop():
	while True:
		licznik = licznik + 1
		sys.stdout.write(licznik + ". Moj demon dziala!")
		time.sleep(5)
	

sys.stdout.write("MyDaemon daemon started")
sys.stderr.write("MyDaemon daemon started")

server = SimpleXMLRPCServer(("127.0.0.1", 40405))
server.register_function(set_title, "set_title")
server.register_function(get_title, "get_title")
server.register_function(get_message, "get_message")
server.register_function(loop, "loop")

#PG wklad - nowy watek
testthread = Demon_wlasciwy.TestThread()
testthread.start()
#PG wklad - nowy watek

server.serve_forever()
	