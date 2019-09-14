#Skrypt loguje się do CMSu, otwiera plik CSV z danymi i dodaje na ich podstawie link do zielonego boxu pobierania
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
import sys
import csv

def powitanie():
    if len(sys.argv) < 2:	#Sprawdzane czy program usuchomiony został z argumentem
        print("Podaj nazwę (ten sam katalog) lub lub ścieżkę do pliku z danymi wejściowymi")
        print("Przykład:")
        print("CMS_Dod_linku_Pob.py input.xlsx")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Za dużo argumentów podaj tylko 1")
        sys.exit(1)

    csv = str(sys.argv[1])
    return csv

def logowanie(driver):

    driver.get("adres CMSu")
    time.sleep(2)

    login = driver.find_element_by_name("email")
    login.clear()
    login.send_keys("tu był login")

    haslo = driver.find_element_by_name("pass")
    haslo.send_keys("a tu hasło")
    haslo.submit()
    #Zalogowany
    time.sleep(2)


def dodajLinkDok(NazwaDok, typDok, Link, produktID, driver, NazwaDokEn):
    driver.get("tu był adres"+str(produktID))
    time.sleep(1)
    typdok_select = Select(driver.find_element_by_name("file[0][product_type]")) #znajdz element typ dokumentu
    typdok_select.select_by_value(str(typDok))  #wybierz wartość "O" czyli pozostałe

    nazwadok = driver.find_element_by_css_selector('input[name="file[0][display_name]"]') #Nazwa pl
    nazwadok.send_keys(NazwaDok)

    nazwadok_en = driver.find_element_by_css_selector('input[name="file[0][display_name_en]"]') #Nazwa EN
    nazwadok_en.send_keys(NazwaDokEn)

    linkdok = driver.find_element_by_name("file[0][display_link]")  #link
    linkdok.send_keys(Link)

    linkdok.submit()



if __name__ == "__main__":

    plikZid = powitanie()
    driver = webdriver.Chrome()
    logowanie(driver)
    with open(plikZid) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            if row[0] == "":
                break

            print(row[2], row[1], row[3], row[0], row[4]) #NazwaDok, typDok, Link, produktID, driver, NazwaDokEn
            dodajLinkDok(row[2], row[1], row[3], row[0], driver,row[4])
            dodajLinkDok(row[5], row[1], row[7], row[0], driver,row[6])
            print(row[5], row[1], row[7], row[0], driver,row[6])

            #print(row)
    driver.close()


    #while True:
