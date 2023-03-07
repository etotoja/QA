#proby testow automatycznych - otworzenie przegladarki Edge

from selenium import webdriver

driver = webdriver.Edge() #bez sciezki bo sterowniki są dodane do PATH
driver.get("https://www.google.pl") #otworzenie danego adresu url
while(True):
    pass