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


link_wyb_symboli = "Tu była strona"

def logowanie(driver):
    driver.get(" tu była strona")
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





def zapisz_sym_do_listy(driver):
    lista=[]
    Resource_Center = driver.find_element_by_xpath('//*[@id="success"]/div/div/div[1]/a/img')
    Resource_Center.click()
    time.sleep(1)
    driver.get(link_wyb_symboli)


    element = driver.find_element_by_xpath("//select[@id='Products']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        #print("Content is: %s" % option.get_attribute("value"))
        if option.get_attribute("value") != "":
            lista.append(option.get_attribute("value"))

        #if len(lista) > 10:
        #    break

    return lista

#Utworzenie katalogu
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def wybierz_symbol_listy(driver1, index_value):
    wybierz = Select(driver1.find_element_by_xpath("//select[@id='Products']")) #znajdz liste rozwiajana
    wybierz.select_by_value(str(index_value))  #wybierz wartosc z wczesnej zapsianej listy
    query = driver1.find_element_by_xpath('//*[@id="tblFileData"]/tbody/tr/td[1]/table/tbody/tr/td/form/input')
    query.click()
    bar_url = driver1.current_url
    while bar_url== "Link do strony" or bar_url == "link do strony" or bar_url == "link do strony" :
        return True #Wylogowano,
    return False

def idz_do_lista_cert(driver2):
    logowanie(driver2)
    driver.get("link do strony")
    Resource_center = driver2.find_element_by_xpath('//*[@id="success"]/div/div/div[1]/a/img')
    Resource_center.click()

    Certification_link = driver2.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[9]/td/a')
    Certification_link.click()


def pobierz_cert(driver1, index_value):

    #Te 2 symbole zawierają znak zapytania z czym nie radzi sobie wget, i wyżuca bład, daltego sa pomijane przy pobieraniu
    if int(index_value) == 4388 or int(index_value) ==4217 or int(index_value)==133:
        return True


    driver1.get(link_wyb_symboli)   #Przejscie do wyboru produktów


    #Pętla która czeka aż strona się wczyta, a konkretnie lista rozwiajana do wyboru symboli
    while True:
        try:
            zalogowano = driver1.find_element_by_xpath('//*[@id="Products"]')   #sprawdź czy strona wyboru produktu już sie wczytała
        except:
            print("Nie wczytano strony wyboru produktów")
            idz_do_lista_cert(driver1)
            time.sleep(5)
            continue #Niestety jeszcze nie
        break #Udało się więc przerwij pętlę



    #Sprawdzanie czy przypadkiem nie nastąpiło wylogowanie, a także próba zalogowania
    if driver1.current_url != link_wyb_symboli:
        print("Wylogowano! Próba zalogowania_a...")
        logowanie(driver1)
        time.sleep(4)
        #driver1.get(link_wyb_symboli)
        return True


    if wybierz_symbol_listy(driver1,index_value) == True:
        logowanie(driver1)
        return True

    #Nazwa produktu
    nazwa_produktu = driver1.find_element_by_xpath('//*[@id="main"]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/table/tbody/tr/td/h1')
    symbol_str = nazwa_produktu.get_attribute("innerHTML")
    symbol_str = symbol_str.replace('<!-- Product Certification Documents -->','')

    #pętla iterująca po plikach dla danego symbolu
    for i in range(2,100,2):    # Co 2 poniewaz tylko w pażystych wierach są dane produktów

        #Sprawdzanie czy przypadkiem nie nastąpiło wylogowanie, a także próba zalogowania
        bar_url = driver1.current_url
        while bar_url== "strona była" or bar_url == "strona" or bar_url == "strona" :
            print("Wylogowano! Próba zalogowania_b...")
            logowanie(driver1)
            time.sleep(5)
            return True #Wylogowano,

        link_pobieranie = 0
        #print(i)
        try:
            wiersz_pobieranie = driver1.find_element_by_xpath('//*[@id="main"]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/div/table/tbody/tr/td/table/tbody/tr[{0}]/td[2]/a[1]'.format(str(i)))
        except:
            break
        link_do_pliku = wiersz_pobieranie.get_attribute('href')
        nazwa_pliku = wiersz_pobieranie.get_attribute('innerHTML')
        #r = requests.get(link_do_pliku)
        print("Przed replace",symbol_str)
        #Stworzenie katalogu
        symbol_str = symbol_str.replace("?","-")
        symbol_str = symbol_str.replace("|","-")
        symbol_str = symbol_str.replace("<","-")
        symbol_str = symbol_str.replace(">","-")
        symbol_str = symbol_str.replace("/","-")
        symbol_str = symbol_str.replace("*","-")
        symbol_str = symbol_str.replace(":","-")
        print("Po replace",symbol_str)

        temp_dir = r"C:\Users\PiotrG\Documents\MoxaCertyfikaty\{}".format(symbol_str)
        print(temp_dir)
        mkdir_p(temp_dir)
        try:
            wget.download(url=link_do_pliku, out=temp_dir)# to nazwa pliku pdf robi problem, a konk. "?"
        except:
            break




if __name__ == "__main__":

    driver = webdriver.Chrome()
    logowanie(driver)

    lista_symboli = zapisz_sym_do_listy(driver)

    i=0
    log = open("log.txt","r")
    linie = log.readlines()
    #print(linie)
    i = int(linie[-1].replace("\n",""))
    print("Liczba symboli z ppobranymi certami: {}".format(i))
    log.close()
    powtorz = False #zmienna powtarzajaca ostatni inex

    for n in range(i, len(lista_symboli)):
        if powtorz:
            n=n-1
            powtorz = False

        #print(lista_symboli[n])
        powtorz = pobierz_cert(driver, lista_symboli[n])
        if powtorz:
            print("Powtarzam jeszcze raz produkt o ID:", lista_symboli[n])
            continue


        print("\nPobrano certyfikaty dla {0} / {1} produktów".format(n,len(lista_symboli)))

        log = open("log.txt","a+")
        log.write("\n{0}".format(str(n)))
        log.close()


    #print(lista_symboli)
    driver.close()
