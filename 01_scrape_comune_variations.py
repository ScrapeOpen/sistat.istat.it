#!/usr/bin/env python
# encoding=utf8

from datetime import datetime
from time import sleep
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sqlite3
import sys
import os.path
from random import randint
import re

# Selenium setting
download_dir = '/home/ubuntu/scrape_sistat' # EDIT THIS
exec_file = '/home/ubuntu/scrape_sistat/geckodriver' # EDIT THIS


display = Display(visible=0, size=(1024, 768))
display.start()

# Firefox settings
options = Options()
# options.set_headless(headless=True)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_dir)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
driver = webdriver.Firefox(capabilities=cap, firefox_options=options, executable_path=exec_file)

base_url = 'http://sistat.istat.it/'
db_file = '/home/ubuntu/scrape_sistat/01_sistat_comune_variations_20190601.sqlite'

waiting_sec = 10

def createDb():

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE pages_completed (
    page INT PRIMARY KEY,
    status INT DEFAULT 0 
    );
               """)

    for i in range(1, 346): # EDIT THIS according to last page
        cursor.execute("INSERT INTO pages_completed (page) VALUES (?);", (i,))

    cursor.execute("""
    CREATE TABLE comune_completed (
    sistat_id INT PRIMARY KEY,
    status INT DEFAULT 1 
    );
               """)

    cursor.execute("""
    CREATE TABLE comune_variation (
    comuni_sistat_id INT,
    comune_last_name CHAR,
    comune_last_istat_cod CHAR,
    data_inizio_validita CHAR,
    data_fine_validita CHAR,
    tipo_variazione CHAR,
    tipo_variazione_script CHAR,
    tipo_documento CHAR,
    data_publicazione CHAR
    );
               """)
    
    conn.commit()

    return

def getLastPage():

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT MIN(page) from pages_completed WHERE status = 0;')

    conn.commit()

    return(cursor.fetchone()[0])


def getCompletedComuni():

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('SELECT sistat_id from comune_completed;')

    conn.commit()

    comuni_istat_id = []

    for row in cursor.fetchall():
        comuni_istat_id.append(row[0])

    return(comuni_istat_id)


def clickGoBack(driver):

    driver.find_element_by_xpath("//*/a[@class='tools_back_page']").click()
    sleep(waiting_sec + randint(1,5))
    return driver

def clickNextPage(driver):

    driver.find_element_by_xpath("//*/a[@class='tools_pag_successiva']").click()
    sleep(waiting_sec + randint(1,5))
    return driver


def storeComuneData(comune_data):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO comune_variation (comuni_sistat_id, data_inizio_validita, data_fine_validita, tipo_variazione, tipo_variazione_script, tipo_documento, data_publicazione, comune_last_istat_cod, comune_last_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (comune_data['comuni_sistat_id'], comune_data['data_inizio_validita'], comune_data['data_fine_validita'], comune_data['tipo_variazione'], comune_data['tipo_variazione_script'], comune_data['tipo_documento'], comune_data['data_publicazione'], comune_data['comune_last_istat_cod'], comune_data['comune_last_name']))
    conn.commit()

    return

def updateComuneCompleted(comune_sistat_id):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comune_completed (sistat_id) VALUES (?);", (comune_sistat_id,))
    conn.commit()
    return


def updatePagesCompleted(page):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("UPDATE pages_completed SET status = 1 WHERE page = ?;", (page,))
    conn.commit()
    return


def getComuneData(sistat_id, driver, i):

    comune_last_istat_cod = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" + str(i) + "]/td[3]").text
    comune_last_name = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" + str(i) + "]/td[4]").text

    try:
        driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" + str(i) + "]/td[7]/a").click()
        sleep(waiting_sec + randint(1,4))
    except:
        comune_data = {'data_inizio_validita' :  "", 'data_fine_validita' :  "", 'tipo_variazione': "", 'data_publicazione': "", 'comuni_sistat_id': sistat_id, 'tipo_documento': "", 'tipo_variazione_script': "", 'comune_last_istat_cod': comune_last_istat_cod, 'comune_last_name': comune_last_name}
        storeComuneData(comune_data)
        return

    trs_comune = driver.find_elements_by_xpath("//*[@id='tabella1']/tbody/tr")
    sleep(waiting_sec + randint(1,4))
    
    for j in range(3, len(trs_comune)+1):

        data_inizio_validita = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[1]").text
        
        data_fine_validita = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[2]").text
        tipo_variazione =  driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[5]").text
        tipo_variazione_script = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[5]/a").get_attribute("href")
        tipo_documento =  driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[6]").text
        data_publicazione =  driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(j) + "]/td[7]").text
        print tipo_variazione
        if tipo_variazione not in ['Acquisizione di Territorio', 'Annessione', 'Appartenenza', 'Cambio Denominazione', 'Cessione di Territorio', 'Costituzione', 'Estinzione', 'Rinumerazione']:
            driver.get_screenshot_as_file('/home/ubuntu/scrape_sistat/snapshot/' + 'document_error_' + str(sistat_id) + "_" + datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + '.png')
            print '/home/ubuntu/scrape_sistat/snapshot/' + 'document_error_' + str(sistat_id) + "_" + datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + '.png'
            raise ValueError('Not an accepted tipo di documento')

        comune_data = {'data_inizio_validita' :  data_inizio_validita, 'data_fine_validita' :  data_fine_validita, 'tipo_variazione': tipo_variazione, 'tipo_variazione_script': tipo_variazione_script, 'data_publicazione': data_publicazione, 'comuni_sistat_id': sistat_id, 'tipo_documento': tipo_documento, 'comune_last_istat_cod': comune_last_istat_cod, 'comune_last_name': comune_last_name}
        storeComuneData(comune_data)

    driver = clickGoBack(driver)
    return

def goToNextPage(current_page, driver):

        updatePagesCompleted(current_page)
        # driver = navigateToPage(current_page + 1, driver)
        clickNextPage(driver)
        return driver


def navigateToPage(page, driver):

        print "Navigating to page " + str(page) + "..."
        driver.find_element_by_xpath("//*/input[@name = 'pag']").send_keys(str(page))
        sleep(waiting_sec + randint(1,4))
        driver.find_element_by_xpath("//*/a[@class = 'tools_pag_selezionata']").click()
        sleep(waiting_sec + randint(1,3))

        return driver
        

def main(driver):

    try:
    
        if os.path.exists(db_file) is False:
            createDb()

        print(getLastPage())

        driver.get(base_url)

        driver.find_element_by_xpath("//*/a[@title = 'Ricerca gerarchica']").click()
        print "Now at `Ricerca gerarchica`."
        sleep(waiting_sec + randint(1,4))
        driver.find_element_by_xpath("//*/a[@title = 'Comuni']").click()
        print "Now at `Comuni`."
        sleep(waiting_sec  + randint(1,4))
        driver.find_element_by_xpath("//*[@id='StoriUaId']/li[1]/a").click()
        print "Now at `li[6]`."
        sleep(waiting_sec + randint(1,4))

        if getLastPage() > 1:

            driver = navigateToPage(getLastPage(), driver)

        current_page = getLastPage()

        while True:

            print "Current page: " + str(current_page)  + "."

            trs = driver.find_elements_by_xpath("//*[@id='tabella1']/tbody/tr")

            for i in range(3, len(trs)+1):
                sistat_id = ""
                sistat_id = driver.find_element_by_xpath("//*[@id='tabella1']/tbody/tr[" +  str(i) + "]/td[4]/a").get_attribute('href')
                sistat_id = re.search('\d{1,8}', sistat_id).group(0)
                if sistat_id == "":
                    driver.get_screenshot_as_file('/home/ubuntu/scrape_sistat/snapshot/' + 'sistat_id_error' + str(sistat_id) + "_" + datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + '.png')
                    raise ValueError("No sistat_id")

                print "sistat id: " + str(sistat_id)
                
                if int(sistat_id) in getCompletedComuni():
                    print "next"
                    continue

                getComuneData(sistat_id, driver, i)
                updateComuneCompleted(sistat_id)

                # sleep(waiting_sec + randint(1,4))

            if (current_page <= 345):
                driver = goToNextPage(current_page, driver)
                current_page += 1
            else:
                driver.quit()
                display.stop()
                sys.exit()

    except Exception, e:
        print e
        return
    
    return

keep_scraping = True

while True:
        # driver = webdriver.PhantomJS()
        # driver = webdriver.Chrome()
        main(driver)
        print "Sleeping for 60 mins."
        sleep(60*60)
