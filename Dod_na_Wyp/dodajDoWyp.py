#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import mechanize
import pandas as pd
import sys


def dodaj(symbol, numer_ser, opis, cena, producent, grupa, ciastko ):
	symbol = str(symbol)
	symbol = symbol.strip()

	numer_ser = str(numer_ser)
	numer_ser = numer_ser.strip()

	opis = u''.join((opis)).encode('utf-8').strip() 

	cena = str(cena)
	cena = cena.strip()

	producent = str(producent).strip()
	grupa = str(grupa).strip()


	Opis_staly = "stan nowy, jest to tzw. leżak magazynowy. "	#opis stały
	URL="Tu był link"

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
	br.set_simple_cookie(name = "PHPSESSID", value=str(ciastko), domain="Tu była witryna", path='/')
	br.open(URL)

	br.select_form(nr = 0)

	br.form["post[symbol_unique]"] = "wyp@"+numer_ser+"@"+symbol
	br.form["post[symbol]"] = symbol
	br.form["post[product_desc]"] = opis+", "+Opis_staly+"SN:"+numer_ser
	br.form["post[product_producer]"] = [producent]
	br.form["post[product_class]"] = [grupa]
	br.form["post[price]"] = cena
	br.form["post[warranty]"] = "1M"
	br.form["post[warehouse_select]"] = ["11"]
	br.form["post[warehouse_qty]"] = ["1"]
	br.submit()
	print "Dodano ",symbol, numer_ser
	return symbol

def odczytXlsx(plik):	
	xl = pd.ExcelFile(plik, encoding='utf-8')
	df1 = xl.parse('Arkusz1') 


if __name__ == "__main__":
	if len(sys.argv[1:]) < 1:	
		print u"Podaj nazwę (ten sam katalog) lub lub ścieżkę do pliku xlsx ze wsadem produktów, oraz drugi argument - ciasteczko sesji PHPSESSID skopiowane z ---"
		print u"Przykład:"
		print u"dodajDoWyp.py wsadwyp.xlsx <ciastko> (długość ciastka=32 znaki)"
		sys.exit(1)
	if len(sys.argv[1:]) > 2:
		print u"Za dużo argumentów podaj tylko 2"
		sys.exit(1)
	excel = str(sys.argv[1])
	ciacho = str(sys.argv[2])

	dataframe = odczytXlsx(excel)
	File = open("dodaneDoWyp.txt","w")


	for i in range(0, 1):	
		dodany = dodaj( dataframe.iloc[i][0] , dataframe.iloc[i][2], dataframe.iloc[i][1], dataframe.iloc[i][3],  dataframe.iloc[i][4], dataframe.iloc[i][5] , ciacho )

		dodany = str(dodany + " " + str(dataframe.iloc[i][2]) + "\n")
		File.write(dodany)

	File.close()
