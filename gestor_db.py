#Gestor de la base de datos del servidor

import sqlite3
from datetime import datetime

DB_NAME = 'rfid_data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL, 
                   uid TEXT UNIQUE NOT NULL,
                   tipo TEXT
                   )
                ''')
    cursor.executeU('''
                    CREATE TABLE IF NOT EXISTS accesos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    uid TEXT UNIQUE NOT NULL,
                    fecha TEXT NOT NULL,
                    tipo TEXT,
                    lector TEXT
                    )
                ''')
    conn.commit()
    conn.close()

    #def validar_uid(uid):
   #     conn = sqlite3.connect(DB_NAME)
