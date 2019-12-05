import mysql.connector


class Basededatos:


    def __init__(self, db):
        self.mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="Agenda_AM")
        self.micursor = self.mibase.cursor()
        
        print("Hola")   

    def crearbd(self,):
        try:
            self.mibase = mysql.connector.connect(host="localhost", user="root", passwd="" )
            self.micursor = self.mibase.cursor()
            self.micursor.execute("CREATE DATABASE Agenda_AM")
            self.mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="Agenda_AM")
            self.micursor = self.mibase.cursor()
            self.micursor.execute("CREATE TABLE contactos( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, apellido varchar(128) COLLATE utf8_spanish2_ci NOT NULL, edad varchar(128) COLLATE utf8_spanish2_ci NOT NULL, cel VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL )")
            print("Base de datos con tabla creada")
        except:
            print("Ya existe la base de datos")
    
    def conexion(self,):

        print("Conexion OK")
        self.mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="Agenda_AM")
        return self.mibase
        
    def consulta(self): #Ir a buscar to fecht
        self.micursor.execute("SELECT * FROM contactos")
        rows = self.micursor.fetchall()
        return rows

    def insertar(self, nombre, apellido, edad, cel, email):
        self.micursor.execute("INSERT INTO contactos VALUES (NULL, %s, %s, %s, %s, %s)",
                         (nombre, apellido, edad, cel, email))
        self.mibase.commit()

    def borrar(self, id):
        self.micursor.execute("DELETE FROM contactos WHERE id=%s", (id,))
        self.mibase.commit()

    def modificar(self, id, nombre, apellido, edad, cel, email):
        self.micursor.execute("UPDATE contactos SET nombre = %s, apellido = %s, edad =%s, cel = %s, email =%s WHERE id = %s",
                         (nombre, apellido, edad, cel, email, id))
        self.mibase.commit()

    def __del__(self):
        self.mibase.close()

