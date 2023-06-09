# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:30:27 2023

@author: carlo
"""


import pandas as pd
import numpy as np

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
        

 
query1 = "select adp_user.username,  adp_busqueda.* from adp_user left join adp_busqueda on (adp_user.cliente_id=adp_busqueda.cliente_id);"
clientes = pd.read_sql_query(query1,engine)

# args = '(0, 0, 0, 0, 0, \'\')


a=0
b=''

clientes = clientes.reset_index()  # make sure indexes pair with number of rows


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




for index, row in clientes.iterrows():

    args = '('+ str(row['marca']) + str(',') + str(row['modelo']) + str(',')+ str(row['anio']) + str(',')+ str(row['damageid']) + str(',')+ str(row['state']) + str(',\'')+ str(b) + str('\'') +')'

    query2 = 'CALL adp.adp_busqueda_subasta'+args
    preferencias = pd.read_sql_query(query2,engine)


    email_user = 'tlcrar23@gmail.com'
    email_password = 'tffplfxecykqbdsu'
    email_send = str(row['username'])
    
    subject = 'Coincidencias para su busqueda de carros ' #+ Tiempo
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    
 
    info_cuerpo_correo = preferencias.loc[:, preferencias.columns.drop(['PaginaOrigen'])]
    # #info_cuerpo_correo_lst=info_cuerpo_correo.values.tolist()
    # # el mensaje del correo dira: Coincidencias para su busqueda de carros
    # # body = 'Hola, Este correo contiene un cuadro con carros en oferta! \n\n' + info_cuerpo_correo.to_html()
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     {0}
    #   </body>
    # </html>
    # """.format(info_cuerpo_correo.to_html())
    rowCount = len(info_cuerpo_correo) 
    if rowCount==0:
        html = """\
                <html>
                    <head>
                        <style>
                            p {
                                font-weight: bold;
                                font-size: 1.2em;
                            }
                        </style>
                    </head>
                    <body>
                        <p>Lo lamentamos, su búsqueda no tuvo resultados</p>
                    </body>
                </html>
        """
    else:
        html = """\
        <html>
        <head></head>
        <body>
        {0}
        </body>
        </html>
        """.format(info_cuerpo_correo.to_html())
    
    
    
    #msg.attach(MIMEText(body,'plain'))
    msg.attach(MIMEText(html, 'html'))
    
    #filename='exp' + Tiempo + '.html'
    #attachment  =open(filename,'rb')
    
    #part = MIMEBase('application','octet-stream')
    #part.set_payload((attachment).read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition',"attachment; filename= "+filename)
    
    #msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    
    server.sendmail(email_user,email_send,text)
    server.quit()


#cerrando conexion de DB
engine.dispose()