#!/usr/bin/env python
# encoding=utf8

## EDIT THIS ##

waiting_sec = 5

### Local paths
download_dir = '/home/ubuntu/scrape_sistat' # EDIT THIS
exec_file = '/home/ubuntu/scrape_sistat/geckodriver' # EDIT THIS
variation_db_file = '/home/ubuntu/scrape_sistat/01_sistat_comune_variations_20190601.sqlite'
db_file = '/home/ubuntu/scrape_sistat/02_sistat_comune_variation_details_20190601.sqlite' # EDIT THIS

## - ##

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

types  = {'Acquisizione di Territorio' : 'territory_acquisition', 'Annessione' : 'annexation',
                  'Appartenenza' : 'change_part_of', 'Cambio Denominazione' : 'change_name',
                  'Cessione di Territorio' : 'territory_cession', 'Costituzione' : 'creation',
                  'Estinzione': 'extinction', 'Rinumerazione' : 'change_code'}


def updateDb():

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Clear log
    cursor.execute("DELETE FROM log;")
    conn.commit()
    
    # Clear place
    cursor.execute("DELETE FROM place;")
    conn.commit()

    # Load variations
    conn = sqlite3.connect(variation_db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comune_variation;")
    variations = cursor.fetchall()
    
    variation_tuples = []
    for variation in variations:
      if variation[5] == '':
        next
      else:
        this_sistat_id = int(variation[0])
        this_event_num = int(re.findall('\'(\d+)\'', variation[6])[1])
        this_event_type = types[variation[5]]
        this_javascript = variation[6]
        this_tuple = tuple([this_sistat_id, this_event_num, this_event_type, this_javascript])
        variation_tuples.append(this_tuple)
    
    # Load event_scope
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT sistat_id, event_num, event_type FROM event_scope;")
    event_scope = cursor.fetchall()
    
    for this_tuple in variation_tuples:
      if this_tuple[0:3:1] in event_scope:
        next
      else: 
        try:
          cursor = conn.cursor()
          cursor.execute("INSERT INTO log (sistat_id, event_num, event_type, javascript) VALUES (?, ?, ?, ?);", (this_tuple))
          conn.commit()
        except:
          pass
        
    # Load and write place
    conn = sqlite3.connect(variation_db_file)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT comuni_sistat_id AS sistat_id, comune_last_name AS last_name, comune_last_istat_cod AS last_istat_cod, 
    max(strftime('%Y-%m-%d',substr(data_inizio_validita, 7, 4) || '-' || substr(data_inizio_validita, 4, 2) || '-' || substr(data_inizio_validita, 1, 2))) AS max_date 
    FROM comune_variation GROUP BY comuni_sistat_id ORDER BY last_name;
    """)
    places = cursor.fetchall()
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for place in places:
      cursor.execute("INSERT INTO place (sistat_id, last_name, last_istat_cod) VALUES (?, ?, ?);", (place[0:3:1]))
      conn.commit()
      
    
    
def createDb():
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE log (
    sistat_id INT,
    event_num INT,
    event_type CHAR,
    javascript CHAR,
    PRIMARY KEY (sistat_id, event_num, event_type)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE place (
    sistat_id INT,
    last_name CHAR,
    last_istat_cod CHAR,
    PRIMARY KEY (sistat_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE event_scope (
    sistat_id INT,
    event_num INT,
    event_type CHAR,
    event_act CHAR,
    event_date CHAR,
    event_description CHAR,
    event_validity_from CHAR,
    event_validity_to CHAR,
    PRIMARY KEY (sistat_id, event_num, event_type)
    );
    """)

    cursor.execute("""
    CREATE TABLE event_territory_acquisition (
    sistat_id INT,
    event_num INT,
    event_from_name CHAR,
    event_from_istat_cod CHAR,
    event_from_area CHAR,
    event_from_population CHAR,
    event_from_extinction_flag CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_territory_cession (
    sistat_id INT,
    event_num INT,
    event_to_name CHAR,
    event_to_istat_cod CHAR,
    event_to_area CHAR,
    event_to_population CHAR,
    event_to_creation_flag CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_change_name (
    sistat_id INT,
    event_num INT,
    event_new_name CHAR,
    event_old_name CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_creation (
    sistat_id INT,
    event_num INT,
    event_from_name CHAR,
    event_from_istat_cod CHAR,
    event_from_area CHAR,
    event_from_population CHAR,
    event_from_extinction_flag CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_extinction (
    sistat_id INT,
    event_num INT,
    event_to_name CHAR,
    event_to_istat_cod CHAR,
    event_to_area CHAR,
    event_to_population CHAR,
    event_to_creation_flag CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_change_code (
    sistat_id INT,
    event_num INT,
    event_old_istat_cod CHAR,
    event_new_istat_cod CHAR
    );
    """)

    cursor.execute("""
    CREATE TABLE event_change_part_of (
    sistat_id INT,
    event_num INT,
    event_new_istat_cod CHAR,
    event_new_province CHAR,
    event_old_istat_cod CHAR,
    event_old_province CHAR
    );
    """)

    conn.commit()

    return
 
 
def enterEventTerritoryAcquisition(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_territory_acquisition (sistat_id, event_num, event_from_name, event_from_istat_cod, event_from_area, event_from_population, event_from_extinction_flag) 
    VALUES(?, ?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_from_name'], event_dict['event_from_istat_cod'], event_dict['event_from_area'], event_dict['event_from_population'], event_dict['event_from_extinction_flag']))
    
    conn.commit()
    
    print(event_dict)
    return
  

def enterEventTerritoryCession(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_territory_cession (sistat_id, event_num, event_to_name, event_to_istat_cod, event_to_area, event_to_population, event_to_creation_flag) 
    VALUES(?, ?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_to_name'], event_dict['event_to_istat_cod'], event_dict['event_to_area'], event_dict['event_to_population'], event_dict['event_to_creation_flag']))
    
    conn.commit()
    
    print(event_dict)
    return
  

def enterEventChangeName(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_change_name (sistat_id, event_num, event_new_name, event_old_name) 
    VALUES(?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_new_name'], event_dict['event_old_name']))
    
    conn.commit()
    
    print(event_dict)
    return

def enterEventCreation(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_creation (sistat_id, event_num, event_from_name, event_from_istat_cod, event_from_area, event_from_population, event_from_extinction_flag) 
    VALUES(?, ?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_from_name'], event_dict['event_from_istat_cod'], event_dict['event_from_area'], event_dict['event_from_population'], event_dict['event_from_extinction_flag']))
    
    conn.commit()
    
    print(event_dict)
    return
  

def enterEventExtinction(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_extinction (sistat_id, event_num, event_to_name, event_to_istat_cod, event_to_area, event_to_population, event_to_creation_flag) 
    VALUES(?, ?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_to_name'], event_dict['event_to_istat_cod'], event_dict['event_to_area'], event_dict['event_to_population'], event_dict['event_to_creation_flag']))
    
    conn.commit()
    
    print(event_dict)
    return
  
  
def enterEventChangeCode(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_change_code (sistat_id, event_num, event_new_istat_cod, event_old_istat_cod) 
    VALUES(?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_new_istat_cod'], event_dict['event_old_istat_cod']))
    
    conn.commit()
    
    print(event_dict)
    return
  
  
def enterEventChangePartOf(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_change_part_of (sistat_id, event_num, event_new_istat_cod, event_new_province, event_old_istat_cod, event_old_province) 
    VALUES(?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_new_istat_cod'], event_dict['event_new_province'], event_dict['event_old_istat_cod'], event_dict['event_old_province']))
    
    conn.commit()
    
    print(event_dict)
    return
  

def enterEventScope(event_dict):
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO event_scope (sistat_id, event_num, event_type, event_act, event_date, event_description, event_validity_from, event_validity_to) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """, (event_dict['sistat_id'], event_dict['event_num'], event_dict['event_type'], event_dict['event_act'], event_dict['event_date'], event_dict['event_description'], event_dict['event_validity_from'], event_dict['event_validity_to']))
    
    conn.commit()
    
    print(event_dict)
    return
  
  
def getTableNumberRows(n):
  
  return(len(driver.find_elements_by_xpath('//*/table[%s]/tbody/tr' % str(n))))
  
  
def parseTableHeaders(n):
  
    res = driver.find_elements_by_xpath('//*/table[%s]/tbody/tr[2]/th' % str(n))
    table_headers = []
    for th in res:
      th_text = th.text
      table_headers.append(th_text)
      
    return(table_headers)
    
  
def parseTableContent(n, r=3):
  
    res = driver.find_elements_by_xpath('//*/table[%s]/tbody/tr[%s]/td' % (str(n), str(r)))
    table_content = []
    for td in res:
      td_text = td.text
      table_content.append(td_text)
      
    return(table_content)
  

def parseEventScope(event_scope):

    table1_headers = parseTableHeaders(1)
    table1_content = parseTableContent(1)
    table2_headers = parseTableHeaders(2)
    table2_content = parseTableContent(2)
    event_scope['event_act'] = table1_content[table1_headers.index("Tipo provvedimento")]
    event_scope['event_date'] = table1_content[table1_headers.index("Data provvedimento")]
    event_scope['event_description'] = table1_content[table1_headers.index("Descrizione")]
    event_scope['event_validity_from'] = table2_content[table2_headers.index("Inizio")]
    event_scope['event_validity_to'] = table2_content[table2_headers.index("Fine")]
    enterEventScope(event_scope)
    
    return
      
      
def parseEventTerritoryCession(event_scope):
  
    table_headers = parseTableHeaders(3)
    for i in range(3, getTableNumberRows(3)):
      this_table_row = parseTableContent(n=3, r=i)
      this_event_territory_cession = event_scope
      this_event_territory_cession['event_to_name'] = this_table_row[table_headers.index("Denominazione")]
      this_event_territory_cession['event_to_istat_cod'] = this_table_row[table_headers.index("Codice Istat")]
      this_event_territory_cession['event_to_area'] = this_table_row[table_headers.index("Superficie acquisita")]
      this_event_territory_cession['event_to_population'] = this_table_row[table_headers.index("Popolazione acquisita")]
      this_event_territory_cession['event_to_creation_flag'] = this_table_row[table_headers.index("Flag costituzione")]
      enterEventTerritoryCession(this_event_territory_cession)
      
    return
  
def parseEventTerritoryAcquisition(event_scope):
  
    table_headers = parseTableHeaders(3)
    for i in range(3, getTableNumberRows(3)):
      this_table_row = parseTableContent(n=3, r=i)
      this_event_territory_acquisition = event_scope
      this_event_territory_acquisition['event_from_istat_cod'] = this_table_row[table_headers.index("Codice Istat e Denominazione")]
      this_event_territory_acquisition['event_from_name'] = this_table_row[table_headers.index("Codice Istat e Denominazione") + 1]
      this_event_territory_acquisition['event_from_area'] = this_table_row[table_headers.index("Superficie ceduta") + 1]
      this_event_territory_acquisition['event_from_population'] = this_table_row[table_headers.index("Popolazione ceduta") + 1]
      this_event_territory_acquisition['event_from_extinction_flag'] = this_table_row[table_headers.index("Flag estinzione") + 1]
      enterEventTerritoryAcquisition(this_event_territory_acquisition)
      
    return
  
  
def parseEventChangeCode(event_scope):
  
    table_headers = parseTableHeaders(3)
    table_content = parseTableContent(3)
    event_change_code = event_scope
    event_change_code['event_old_istat_cod'] = table_content[table_headers.index('Codice Istat precedente')]
    event_change_code['event_new_istat_cod'] = table_content[table_headers.index('Codice Istat')]
    enterEventChangeCode(event_change_code)
    
    return

def parseEventChangeName(event_scope):
  
    table_headers = parseTableHeaders(3)
    table_content = parseTableContent(3)
    event_change_name = event_scope
    event_change_name['event_old_name'] = table_content[table_headers.index('Denominazione corrente')]
    event_change_name['event_new_name'] = table_content[table_headers.index('Denominazione precedente')]
    enterEventChangeName(event_change_name)
    
    return
  
def parseEventExtinction(event_scope):
  
    table_headers = parseTableHeaders(n=3)
    for i in range(3, getTableNumberRows(n=3)):
      this_table_row = parseTableContent(n=3, r=i)
      this_len_diff = len(this_table_row) - len(table_headers)
      this_event_extinction = event_scope
      event_to_name_j = [j for j, n in enumerate(table_headers) if n == 'Denominazione'][1]
      this_event_extinction['event_to_name'] = this_table_row[event_to_name_j+this_len_diff]
      event_to_istat_cod_j = [j for j, n in enumerate(table_headers) if n == 'Codice Istat'][1]
      this_event_extinction['event_to_istat_cod'] = this_table_row[event_to_istat_cod_j+this_len_diff]
      this_event_extinction['event_to_area'] = this_table_row[table_headers.index('Superficie acquisita')+this_len_diff]
      this_event_extinction['event_to_population'] = this_table_row[table_headers.index('Popolazione acquisita')+this_len_diff]
      this_event_extinction['event_to_creation_flag'] = this_table_row[table_headers.index('Flag costituzione')+this_len_diff]
      enterEventExtinction(this_event_extinction)
      
    return
  
  
def parseEventCreation(event_scope):
  
    table_headers = parseTableHeaders(n=3)
    for i in range(3, getTableNumberRows(n=3)):
      this_table_row = parseTableContent(n=3, r=i)
      this_len_diff = len(this_table_row) - len(table_headers)
      this_event_creation = event_scope
      event_from_name_j = [j for j, n in enumerate(table_headers) if n == 'Denominazione'][1]
      this_event_creation['event_from_name'] = this_table_row[event_from_name_j+this_len_diff]
      this_event_creation['event_from_istat_cod'] = this_table_row[table_headers.index('Codice\nComune')+this_len_diff]
      this_event_creation['event_from_area'] = this_table_row[table_headers.index('Superficie ceduta')+this_len_diff]
      this_event_creation['event_from_population'] = this_table_row[table_headers.index('Popolazione ceduta')+this_len_diff]
      this_event_creation['event_from_extinction_flag'] = this_table_row[table_headers.index('Flag estinzione')+this_len_diff]
      enterEventCreation(this_event_creation)
    
    return
  
def parseEventChangePartOf(event_scope):
  
    table_headers = parseTableHeaders(3)
    table_content = parseTableContent(3)
    event_change_part_of = event_scope
    event_change_part_of['event_old_istat_cod'] = table_content[table_headers.index('Codice Istat precedente')]
    event_change_part_of['event_new_istat_cod'] = table_content[table_headers.index('Codice Istat attuale')]
    event_change_part_of['event_old_province'] = table_content[table_headers.index('Denominazione provincia precedente')]
    event_change_part_of['event_new_province'] = table_content[table_headers.index('Denomininazione provincia attuale')]
    enterEventChangePartOf(event_change_part_of)

    return
  
def parseEventDetails():
  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log;")
    events = cursor.fetchall()
    
    # Reach website
    driver.get(base_url)
    driver.find_element_by_xpath("//*/a[@title = 'Ricerca gerarchica']").click()
    print "Now at `Ricerca gerarchica`."
    sleep(waiting_sec + randint(5,10))
    driver.find_element_by_xpath("//*/a[@title = 'Comuni']").click()
    print "Now at `Comuni`."
    sleep(waiting_sec  + randint(5,10))
    driver.find_element_by_xpath("//*[@id='StoriUaId']/li[1]/a").click()
    print "Now at `li[6]`."
    sleep(waiting_sec + randint(5,10))
    
    for event in events:
      this_event_scope = {}
      this_event_scope['sistat_id'] = event[0]
      this_event_scope['event_num'] = event[1]
      this_event_scope['event_type'] = event[2]
      this_javascript = event[3]
      if this_javascript == '':
        next
      driver.execute_script(this_javascript.replace("%20", " "))
      sleep(waiting_sec + randint(5,10))
      parseEventScope(this_event_scope)
      sleep(waiting_sec + randint(5,10))
      
      if this_event_scope['event_type'] == 'territory_acquisition':
        parseEventTerritoryAcquisition(this_event_scope)
        
      if this_event_scope['event_type'] == 'change_part_of':
        parseEventChangePartOf(this_event_scope)
        
      if this_event_scope['event_type'] == 'change_name':
        parseEventChangeName(this_event_scope)
        
      if this_event_scope['event_type'] == 'territory_cession':
        parseEventTerritoryCession(this_event_scope)
        
      if this_event_scope['event_type'] == 'creation':
        parseEventCreation(this_event_scope)
        
      if this_event_scope['event_type'] == 'extinction':
        parseEventExtinction(this_event_scope)
        
      if this_event_scope['event_type'] == 'change_code':
        parseEventChangeCode(this_event_scope)
        
    return
    
    
def main():
  try:
    if os.path.exists(db_file) is False:
      createDb()
    updateDb()
    parseEventDetails()
    display.stop()
  except Exception, e:
    print e
    return
  

while True:
        # driver = webdriver.PhantomJS()
        # driver = webdriver.Chrome()
        main()
        print "Sleeping for 30 mins."
        sleep(30*60)
