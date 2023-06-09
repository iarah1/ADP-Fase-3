# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:38:44 2023

@author: carlo
"""

import pandas as pd
import numpy as np

import os

file_list = os.listdir("C:/Users/carlo/OneDrive/WebScrapping/Databases")

lista_bases=sorted(file_list,  key=None, reverse=True)

frame = pd.read_html("C:/Users/carlo/OneDrive/WebScrapping/Databases/" + lista_bases[0])

frame2=frame[0]

frame2[['Anio', 'Marca', 'Modelo']] = frame2.Anio_marca_modelo.str.split(pat=None, n=2, expand = True)

frame3 = frame2[['Numero_lote','Anio','Marca','Modelo','Danio','Locacion', 'Oferta', 'PrecioYa','PaginaOrigen']]



# from sqlalchemy import create_engine
# my_conn = create_engine("mysql+mysqlconnector://root:@localhost/adp")

# frame3.to_sql(con=my_conn, name='adp_subasta', if_exists='replace',index=False)



# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine

 
# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'adp'
 
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
 
 
if __name__ == '__main__':
 
    try:
       
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")
        
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


frame3.to_sql(con=engine, name='adp_subasta', if_exists='replace',index=False)

        
