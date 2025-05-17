#Gestor de la base de datos del servidor

import sqlite3
from datetime import datetime

DB_NAME = 'rfid_data.db'

# Crear las tablas si no existen
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
    cursor.execute('''
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

# Validar si el UID está registrado
def validar_uid(uid):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT nombre FROM usuarios WHERE uid = ?',(uid,))
    resultado = cursor.fetchone()
    conn.close
    if resultado:
        return resultado[0] #retorna un nombre si existe
    else:
        return None


# Registrar un acceso si el UID es válido# Registrar un acceso si el UID es válido
def registrar_acceso(uid, lector):
    nombre = validar_uid(uid)
    if nombre:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO accesos (uid, fecha, tipo, lector) VALUES (?,?,?,?)',
                       (uid,fecha,"Entrada",lector))
        
        conn.commit()
        conn.close()
        print(f"[ACCESO] {nombre} ({uid}) - {fecha} - {lector}")
        return True
    else:
        print(f"[DENEGADO] tarjeta no registrada")
        return False
if __name__ == "__main__":
    init_db()
    print("[INFO] Base de datos inicializada")
