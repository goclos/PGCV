#Skrypt loguje się do CMSu, otwiera plik CSV z danymi i dodaje na ich podstawie link do zielonego boxu pobierania
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
import sys
import csv
import urllib3
import requests
import shutil
import wget
import errno
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pdb

g = 0 #głębokość rekursji
wymiary = r"adres strony z wymiarami"
visio = r"adres innej strony"
rysunki3d= r"adres strony z rysunkami"
linki_pobieranie = []


#Utworzenie katalogu
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def zapisz_unikalna_lista(my_list):
    with open('Unik_log_stron_z_produktami.txt', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)

def zapisz_pobrany_link(link):
    pobrane = open("pobrane.txt","a+")
    pobrane.write("\n{0}".format(str(link)))
    pobrane.close()

def otworz_log_pobranych():
    pobrane = open("pobrane.txt")
    pobrane_linki = pobrane.read().split("\n") 
    pobrane.close() 
    return pobrane_linki

def pobierz_pliki(driver1, link):

    for item in otworz_log_pobranych(): #jesli już dany link został zużyty to leć do następnego
        if item == link and link != "" and link != 0:
            kontynuuj = True
            return

    #Nazwa produktu
    nazwa_produktu = driver1.find_element_by_class_name('Documentstext')
    symbol_str = nazwa_produktu.get_attribute("innerHTML")
    print("Nazwa produktu: ", symbol_str)
    symbol_str = symbol_str.replace('<!-- Product Certification Documents -->','')
    print("==4==")
    #pętla iterująca po plikach dla danego linku
    for i in range(2,100,2):    # Co 2 poniewaz tylko w pażystych wierszach są dane produktów
        #Sprawdzanie czy przypadkiem nie nastąpiło wylogowanie, a także próba zalogowania
        print("==5==")
        bar_url = driver1.current_url

        #Poniższy fragment sprawdza czy jest ten element jesli nie to probuje się przelogować
        try:
            element_testowy = find_element_by_id('//*[@id="form1"]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/a[1]')
        except:
            znacznik = "BRAK"
        znacznik="OK"


        while znacznik == "BRAK" :      #Petla sprawdzająca czy przypadkiem nie nastąpiło wylogowanie timeout i próba zalogowania do skutku
            print("Wylogowano! Próba zalogowania...")
            logowanie(driver1)
            proba_wczytania_tej_strony(str(r"{0}".format(link)))
            try:
                element_testowy = find_element_by_id('//*[@id="form1"]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/a[1]')
            except:
                time.sleep(5)
                continue
            break

        print("==6==")
        try:
            wiersz_pobieranie = driver1.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[{0}]/td[2]/a[1]'.format(str(i)))
            #old xpath: '//*[@id="main"]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/table/tbody/tr/td/table/tbody/tr[{0}]/td[2]/a[1]'.format(str(i))
        except:
            print("==7==")
            break
        print("==8==")
        link_do_pliku = wiersz_pobieranie.get_attribute('href')
        nazwa_pliku = wiersz_pobieranie.get_attribute('innerHTML')
        print("link do pliku:", link_do_pliku, "nazwa pliku:", nazwa_pliku)
        symbol_str = symbol_str.replace("?","-")
        symbol_str = symbol_str.replace("|","-")
        symbol_str = symbol_str.replace("<","-")
        symbol_str = symbol_str.replace(">","-")
        symbol_str = symbol_str.replace("/","-")
        symbol_str = symbol_str.replace("*","-")
        symbol_str = symbol_str.replace(":","-")

        try:
            wiersz_pobieranie.click()
        except:
            print("==9==")
            break


    print("Pobrano z: ", link)
    zapisz_pobrany_link(link)

def logowanie(driver):
    proba_wczytania_tej_strony('tu był link do strony')
    time.sleep(1)

    try:    #Próbuję znaleźć okienko logowania, jeśli go nie ma to znaczy jestem zalogowany i wychodzę z funkcji
        login = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtAccount"]')
    except:
        return

    login = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtAccount"]')
    login.clear()
    login.send_keys("login")

    haslo = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtPassword"]')
    haslo.clear()
    haslo.send_keys("hasło")
    remember_me = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_ChkRememberMe"]')
    remember_me.click()

    loguj = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_loginLink"]/img')
    loguj.click()

  

def logowanie_i_powrot_na_strone(driver, link_docelowy):

    proba_wczytania_tej_strony("tu był adres strony logowania")

    time.sleep(1)

    try:    #Próbuję znaleźć okienko logowania, jeśli go nie ma to znaczy jestem zalogowany i wychodzę z funkcji
        login = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtAccount"]')
    except:
        return

    login = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtAccount"]')
    login.clear()
    login.send_keys("login")

    haslo = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_txtPassword"]')
    haslo.clear()
    haslo.send_keys("hasło")
    remember_me = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_ChkRememberMe"]')
    remember_me.click()

    loguj = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolderMain_loginLink"]/img')
    loguj.click()
    proba_wczytania_tej_strony(link_docelowy)



def sprawdzenie_czy_strona_wczytana(driver,link):
    try:
        myElem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FooterCenter"]/div/font')))
        print("Page is ready!")
        return "READY"
    except TimeoutException:
        print("Ładowanie trwa zbyt długo! Próba zalogowania...")
        while True:
            logowanie_i_powrot_na_strone(driver,link)
            if driver.current_url == link:
                break
        return "READY"

def czy_sa_pliki_do_pobrania(driver):
    if str(driver.current_url) == str(visio):#Wyjątek dla głownego katalogu do pobierania visio
        return "NIE"
    try: #unikalny xpath kóry jest tylko na stronie z plikami do pobrania
        Jest = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/a[1]')
    except:#nie
        return "NIE"
    linki_pobieranie.append(driver.current_url) #TAK. Zapisuje link do strony z pobieraniami
    log = open("log_stron_z_produktami.txt","a+")
    log.write("\n{0}".format(str(driver.current_url)))
    log.close()
    print("!!!To jest strona z plikami do Pobrania:", driver.current_url)
    pobierz_pliki(driver, driver.current_url)
    return "TAK"

def czy_sa_linki_do_czytania(driver):
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="tblFileData"]/tbody/tr[1]/td/a[1]')
    except:
        print("Nie ma linków do czytania! Strona: ",driver.current_url)
        return "NIE"
    return "TAK"


    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

#Czyta i zwraca linki
def czytaj_linki(driver, current_directory):
    proba_wczytania_tej_strony(current_directory)
    linki_out = []

    #Poniższe warunki sprawdzają czy sa pliki do pobrania albo czy strona jest pusta.
    if czy_sa_pliki_do_pobrania(driver) == "TAK": #Tutaj oprócz sprawdzania zapisywany jest link do listy
        return ["PLIKI"]
    else:
        if czy_sa_linki_do_czytania(driver) == "NIE":
            return ["BEZ_LINKOW"]
    #elems = driver.find_elements_by_xpath('//a[@href]')
    elems_subblue = driver.find_elements_by_class_name("SubBlue")
    #Ta pęla iteruje po linkach, sprawdza czy są to linki do podkatalogów i jeśli tak to zapisuje je do listy
    for elem in elems_subblue:
        if  str(elem.get_attribute("href"))[0:77] != r"tu był link do strony": #Usuwanie niepotrzebnych linków ()
            continue

        linki_out.append(elem.get_attribute("href"))
        print("     Link na tej stronie: ",elem.get_attribute("href"))
    return linki_out #zwaraca listę linków ze znalezionymi pod kategoriami

###Pętla rekurencyjna, wazna!
def rekurencyjne_pelzanie_po_stronach(driver,odczytywana_strona,g):#zmienna g to głębokość rekurencji.
    print(g)
    odczytane_linki = czytaj_linki(driver, odczytywana_strona)
    for przeszukiwana_strona in odczytane_linki:
        print(g)
        print("Przeszukiwana strona:",przeszukiwana_strona)
        if odczytane_linki[0] == "PLIKI" or odczytane_linki[0] == "BEZ_LINKOW":
            continue
        rekurencyjne_pelzanie_po_stronach(driver, przeszukiwana_strona,g+1)#Tutaj inkrementuję zmienną g
        g = g-1#tutaj dekrementuje zmienną g
        print(g)


def proba_wczytania_tej_strony(link_in):
    while True:
        try:
            driver.get(link_in)
        except TimeoutException:
            print("Timeout! Próba kolejnego wczytania strony... ")
            continue
        print("Sukces, strona wczytana!", link_in)
        break


if __name__ == "__main__":


    chromeOptions = webdriver.ChromeOptions()


    chromeOptions.add_argument(r"user-data-dir=C:\Users\HP\AppData\Local\Google\Chrome\User Data\\")

    driver = webdriver.Chrome(r"C:\Chromedriver_Selenium\chromedriver.exe", options=chromeOptions)
    logowanie(driver)
    proba_wczytania_tej_strony('tu był link do strony')
    start_time = time.time()


    zawartosc_marker_in = ""

    marker_in = open("marker.txt", "r")
    zawartosc_marker_in = marker_in.readline()
    zawartosc_marker_in = zawartosc_marker_in.replace('\n','')
    print("zawartosc_marker_in(STR): ",zawartosc_marker_in)
    marker_in.close()


    #proba_wczytania_tej_strony(odczytywana)
    if zawartosc_marker_in !="DRZEWO_PLIKOW_PRZESZUKANE":
        print("DRZEWO_PLIKOW nie PRZESZUKANE")

        proba_wczytania_tej_strony(visio)
        ###Najważniejszy i najtrudniejszy element:
        rekurencyjne_pelzanie_po_stronach(driver,visio,0)

        #zapisywanie markera do pliku, z informacją że że drzewo zostało przeszukane
        marker = open("marker.txt","w")
        marker.write("DRZEWO_PLIKOW_PRZESZUKANE")
        marker.close()
    else:
        print("DRZEWO_PLIKOW PRZESZUKANE")


    driver.close()

    print("Koniec! Udało się! (chyba)")
