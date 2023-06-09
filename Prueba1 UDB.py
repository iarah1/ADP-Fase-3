# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:38:39 2023

@author: carlo
"""


# import schedule
import time
# import requests
import random
from time import sleep
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import math 
# import time
# from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
# import os
# import numpy as np
# import re

sleep(random.uniform(5.0, 7.0))
 
# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome() 
driver.implicitly_wait(30)
# Voy a la pagina que requiero
link='https://www.copart.com/vehicle-search-featured/buyitnow?displayStr=Buy%20It%20Now&from=%2FvehicleFinder&searchCriteria=%7B%22query%22:%5B%22*%22%5D,%22filter%22:%7B%22FETI%22:%5B%22buy_it_now_code:B1%22,%22lot_condition_code:CERT-D%22%5D,%22PRID%22:%5B%22damage_type_code:DAMAGECODE_AO%22,%22damage_type_code:DAMAGECODE_FD%22,%22damage_type_code:DAMAGECODE_FR%22,%22damage_type_code:DAMAGECODE_HL%22,%22damage_type_code:DAMAGECODE_MN%22,%22damage_type_code:DAMAGECODE_NW%22,%22damage_type_code:DAMAGECODE_RR%22%5D,%22YEAR%22:%5B%22lot_year:%5B2017%20TO%202023%5D%22%5D,%22TITL%22:%5B%22title_group_code:TITLEGROUP_C%22%5D,%22VEHT%22:%5B%22vehicle_type_code:VEHTYPE_V%22%5D%7D,%22searchName%22:%22%22,%22watchListOnly%22:false,%22freeFormSearch%22:false%7D'
driver.get(link)

sleep(random.uniform(5.0, 7.0))

# Busco el boton para cargar mas informacion


# driver.find_element_by_xpath("//select[@name='serverSideDataTable_length']/option[text()='100']").click()

driver.find_element(By.XPATH, "//span[@class='p-element p-dropdown-label p-inputtext ng-star-inserted'][@id='pr_id_3_label']").click()
#<span class="ng-star-inserted">100</span>
driver.implicitly_wait(30)

sleep(random.uniform(5.0, 7.0))

driver.find_element(By.XPATH, "//span[@class='ng-star-inserted'][text()='100']").click()

sleep(random.uniform(5.0, 10.0))

#Sacando listado de carros
#<span class="p-paginator-current ng-star-inserted">Showing 1 to 100 of 853 entries</span>

Numero_hojas = driver.find_element(By.XPATH, "//span[@class='blue-heading']").text

Numero_hojas = math.ceil(int(Numero_hojas)/100)

# len(containers)
Tiempo=time.strftime("%Y %m %d %H %M %S")

#cols=['Numero_lote','Anio_carro,Marca','Modelo','Locacion','Danio','Otros']
cols=['concatenado']
lst=[]



for Hoja in range(int(Numero_hojas)-1):
    
    containers = driver.find_elements(By.XPATH, "//tr[@class='p-element p-selectable-row ng-star-inserted']")
    
    for carros in containers[0:]: 
        Numero_lote = carros.find_element(By.XPATH, './/span[@class="search_result_lot_number p-bold blue-heading ng-star-inserted"]').text
        #<span _ngcontent-muv-c108="" class="search_result_lot_number p-bold blue-heading ng-star-inserted"><a _ngcontent-muv-c108="" href="/lot/46081273/clean-title-2018-mercedes-benz-c-300-4matic-ga-fairburn"> 46081273 </a></span>
        Anio_marca_modelo = carros.find_element(By.XPATH, './/span[@class="search_result_lot_detail ng-star-inserted"]').text
        #<span _ngcontent-imt-c108="" class="search_result_lot_detail ng-star-inserted"> 2018 CHEVROLET EQUINOX LT </span>
        Danio = carros.find_element(By.XPATH,'.//span[@class="text-black p-bold"]').text
        #<span _ngcontent-egk-c108="" class="text-black p-bold">Front End Damage</span>
        Locacion = carros.find_element(By.XPATH,'.//span[@class="search_result_yard_location_label blue-heading p-d-flex p-cursor-pointer p-bold"]').text
        #<span _ngcontent-egk-c108="" locationinfo="" class="search_result_yard_location_label blue-heading p-d-flex p-cursor-pointer p-bold"> IN - FORT WAYNE <span _ngcontent-egk-c108="" class="yard_location_arrow_icon"></span></span>
        Oferta = carros.find_element(By.XPATH,'.//span[@class="search_result_amount_block text-black p-bold"]').text
        #<span _ngcontent-egk-c108="" copartglobalcurrency="" class="search_result_amount_block text-black p-bold"><span class="currencyAmount">$300.00</span> <span class="currencyCode">USD</span></span>
        PrecioYa = carros.find_element(By.XPATH,'.//span[@class="search_result_amount_block text-black p-bold nowrap p-fs-14"]').text
        #<span _ngcontent-egk-c108="" copartglobalcurrency="" class="search_result_amount_block text-black p-bold nowrap p-fs-14"><span class="currencyAmount">$14,100.00</span> <span class="currencyCode">USD</span></span>
        concatenado = Numero_lote + ", " + Anio_marca_modelo + ", " + Danio + ", " + Locacion + ", " + Oferta.replace(",", "") + ", " + PrecioYa.replace(",", "") + ", " + str(Hoja)
        lst.append(concatenado)
    
    Boton_next_hoja=driver.find_element(By.XPATH, "//span[@class='p-paginator-icon pi pi-angle-right']") 
    #<span class="p-paginator-icon pi pi-angle-right"></span>
    Boton_next_hoja.click()
    driver.implicitly_wait(30)
    sleep(random.uniform(15.0, 19.0))

df1 = pd.DataFrame(lst, columns=cols)

df2 = df1['concatenado'].str.split(',', expand=True)

names=['Numero_lote','Anio_marca_modelo','Danio','Locacion', 'Oferta', 'PrecioYa','PaginaOrigen']

df2.columns=names

driver.close() #Cierro navegador

##################################################

f = open('C:/Users/carlo/OneDrive/WebScrapping/Databases/exp' + Tiempo + '.html','w')
a = df2.to_html()
f.write(a)
f.close()

#######################################################

####https://www.youtube.com/watch?v=bXRYJEKjqIM

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

# email_user = 'tlcrar23@gmail.com'
# email_password = 'tffplfxecykqbdsu'
# email_send = 'tlcrar23@gmail.com'

# subject = 'Correo de carros: ' + Tiempo
# msg = MIMEMultipart()
# msg['From'] = email_user
# msg['To'] = email_send
# msg['Subject'] = subject

# body = 'Hola, Este correo contiene un cuadro con carros en oferta!'
# msg.attach(MIMEText(body,'plain'))

# filename='exp' + Tiempo + '.html'
# attachment  =open(filename,'rb')

# part = MIMEBase('application','octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition',"attachment; filename= "+filename)

# msg.attach(part)
# text = msg.as_string()
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(email_user,email_password)

# server.sendmail(email_user,email_send,text)
# server.quit()
