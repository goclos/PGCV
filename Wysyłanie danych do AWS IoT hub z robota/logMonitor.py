import time
from _ast import If
from __builtin__ import True
import itertools


LogDir="/root/log_history.txt"  #Lokalizacja logo
#LogDir="/home/ur/log_history.txt" #Miejsce z logami na symulatorze

LogCountStorage = "LogCountStorage.txt" #Plik zapamietujacy ile logow zostalo wyslanych
LogLEN=0

###Glowna funkcja:
def checkForNewLogs(LastLineCount):   #Sprawdza czy sa nowe logi
    filename = LogDir 
    i=0
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    fileLen = i+1
    if readLogLen() == 0 and fileLen > 1000:    #Warunek do nie wysylania zbyt duzego logu, przy pierwszym uruchomieniu urcapa
        writeReadedLogCount(fileLen)
        return [''], fileLen
    newLines = checkForNewLines(LastLineCount, fileLen) #Sprawdzam czy log ma nowe linie
    newLogs = readNewLines(filename,newLines,fileLen)   #Czytam nowe linie w logu
    writeReadedLogCount(fileLen)    #Zapisuje wynik do pliku, aby w razie restartu nie przesylac juz raz przeslanych logow
    return newLogs, fileLen

def readLogLen():   #Czyta ile logow zostalo ostantnio przeczytanych, zapisane w pliku
    filename = LogCountStorage
    memoryFile = open(filename, "r")
    ReadedLines = int(memoryFile.readline())
    memoryFile.close()  
    return ReadedLines

def writeReadedLogCount(lineCount):  #Zapisuje aktualna dlugosc logow
    filename = LogCountStorage
    memoryFile = open(filename, "w")
    memoryFile.write(str(lineCount))

def checkForNewLines(lastLines, currentLines):  #Sprawdza czy sa nowe linie od ostatniej iteracji
    diff = 0
    if currentLines > lastLines:
        diff = currentLines - lastLines
    return diff

def readNewLines(file, newlines, fileLen):  #Odczytuje nowe logi
    newlinesContent = []
    print "newlines: ", newlines, "fileLen",fileLen
    with open(file, "r") as textFile:
        for line in itertools.islice(textFile, fileLen-newlines, fileLen):
            newlinesContent.append(line)
    return newlinesContent


if __name__ == "__main__":
    LogLEN = readLogLen()
    while True:     
        NewLogs, LogLEN = checkForNewLogs(LogLEN)
        print "NewLogs: ",NewLogs, "LogLEN: ",LogLEN
        time.sleep(10)
