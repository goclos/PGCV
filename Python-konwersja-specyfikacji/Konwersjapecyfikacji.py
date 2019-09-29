#Skrypt loguje się do CMSu, otwiera plik CSV z danymi i dodaje na ich podstawie link do zielonego boxu pobierania
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os
import sys
from selenium.webdriver.common.keys import Keys
import errno
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#import pyautogui  #<== need this to click on extension
import re
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


tabelaWynikowa = " "
wczytano = False
driver = False

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def CzytajNazwySekcji():
    global tabelaWynikowa
    global driver
    for i in range(1, 1000):
        try:
            tytulSekcji = driver.find_element_by_xpath('//*[@id="specifications"]/div/div[1]/div/div/div[{0}]/button/div/h3'.format(str(i)))
        except:
            break
        tytulSekcji = tytulSekcji.get_attribute('innerHTML')
        tytulSekcji = cleanhtml(tytulSekcji)
        tabelaWynikowa = tabelaWynikowa +'<ul>\n<li class="podpis_tabeli">{0}</li>\n</ul>\n'.format(tytulSekcji)
        tabelaWynikowa = tabelaWynikowa + '<table>\n<tbody>\n'
        CzytajWierszeSekcji(i)

def CzytajWierszeSekcji(NumerSekcji):
    global tabelaWynikowa
    global driver
    for i in range(1, 1000):
        try:
                                                      #//*[@id="specifications"]/div/div[1]/div/div/div[2]/div/ul/li[1]/h4
            nazwaCechy = driver.find_element_by_xpath('//*[@id="specifications"]/div/div[1]/div/div/div[{0}]/div/ul/li[{1}]/h4'.format(str(NumerSekcji),str(i)))
                                                        #//*[@id="specifications"]/div/div[1]/div/div/div[2]/div/ul/li[1]/div/p
            wartoscCechy = driver.find_element_by_xpath('//*[@id="specifications"]/div/div[1]/div/div/div[{0}]/div/ul/li[{1}]/div/p'.format(str(NumerSekcji),str(i)))
        except:
            tabelaWynikowa = tabelaWynikowa + '</tbody>\n</table>\n'
            break
        nazwaCechy = nazwaCechy.get_attribute('innerHTML')
        wartoscCechy = wartoscCechy.get_attribute('innerHTML')
        nazwaCechy = cleanhtml(nazwaCechy)  #Czyszczenie z tagów html
        wartoscCechy = cleanhtml(wartoscCechy)  #Czyszczenie z tagów html
        tabelaWynikowa = tabelaWynikowa + '<tr>\n'  #Otwieramy wiersz
        tabelaWynikowa = tabelaWynikowa + '<td>{0}</td>\n'.format(nazwaCechy) #Dodajemy Nazwę cechy
        tabelaWynikowa = tabelaWynikowa + '<td>{0}</td>\n'.format(wartoscCechy) #Dodajemy wartość cechy
        tabelaWynikowa = tabelaWynikowa + '</tr>\n' #Zamykamy wiersz


def konwertuj():
    global tabelaWynikowa
    tabelaWynikowa = ""
    if str(e1.get()) == "" or str(e1.get()) == None:
        messagebox.showinfo("Źle","Źle, to pole nie może być puste!")
        return
    global wczytano
    if wczytano == False:
        messagebox.showinfo("Źle","Źle, najpier musisz nacisnąć 'Wczytaj'")
        return
    global driver
    # Wspolrzedne do klikniecia w rozszerzenie
    #x, y = pyautogui.locateCenterOnScreen('GT3.png')
    # Klikniecie w rozszerzenie
    #pyautogui.click(x, y)
    # Wspolrzedne przycisku "przetłumacz"
    #time.sleep(1)
    #x, y = pyautogui.locateCenterOnScreen('przetlumacz.png')
    #pyautogui.click(x, y)
    CzytajNazwySekcji()
    #driver.close()
    czas = datetime.now().strftime('%H%M%S')
    Html_file= open("tabelka{0}.html".format(str(czas)),"w")
    Html_file.write(tabelaWynikowa)
    Html_file.close()
    messagebox.showinfo("Sukces!", "Udało się! Sprawdź czy w tym samym katalogu co program jest plik o nazwie 'Tabelka.html'")


def initChromeDriver():
    executable_path = "chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = executable_path
    chrome_options = Options()
    chrome_options.add_extension('Google Traduction-Chrome Web Store_v2.0.7.crx')
    global driver
    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

def exit():
    global driver
    try:
        driver.quit()
    except:
        pass
    sys.exit()

def wczytajStrone():
    if str(e1.get()) == "" or str(e1.get()) == None:
        messagebox.showinfo("Źle","Źle, to pole nie może być puste!")
        return
    global driver
    driver.get(str(e1.get()))
    messagebox.showinfo("Sukces","Strona została wczytana")
    global wczytano
    wczytano = True


if __name__ == "__main__":
    initChromeDriver()

    master = tk.Tk()
    master.resizable(False, False)
    master.title("Konwersja specyfikacji Moxa")
    tk.Label(master,text="Wklej adres z moxa.com z specyfikacją produktu (#specifications) poniżej, i 'Wczytaj stronę'\nPrzed klinięciem 'Konwertuj' kliknij na rozszerzeniu Google Translator w otwartej przeglądarce i 'Przetłumacz tę stronę'").grid(row=0, columnspan=2, padx=10)

    e1 = tk.Entry(master, width=100)
    e1.grid(row=1, columnspan=2)
    tk.Button(master,text='1.Wczytaj stronę',command=lambda: wczytajStrone()).grid(row=3,column=0,sticky=tk.W,pady=4, padx=100)
    tk.Button(master,text='2.Konwertuj', command=konwertuj).grid(row=3, column=1,sticky=tk.W,pady=4,padx=100)
    master.protocol("WM_DELETE_WINDOW", lambda: exit())
    tk.mainloop()
