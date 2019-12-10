import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
from db import Basededatos


# Instanciamos la base de datos como objeto

db = Basededatos('store.db')

# Aplicacion principal / interfaz grafica.

class Agenda(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Agenda Corporativa')
        # Ancho y alto
        master.geometry("700x350")
        # Crear widgets
        self.crear_widgets()
        # Init selected item var
        self.item_selecionado = 0
        # Visualizar los registros de la base.
        self.populate_list()

    def crear_widgets(self):
        # Nombre
        self.nombre_text = tk.StringVar()
        self.nombre_label = tk.Label(
            self.master, text='Nombre', font=('bold', 14), pady=20)
        self.nombre_label.grid(row=0, column=0, sticky=tk.W)
        self.nombre_entry = tk.Entry(self.master, textvariable=self.nombre_text)
        self.nombre_entry.grid(row=0, column=1)
        # Apellido
        self.apellido_text = tk.StringVar()
        self.apellido_label = tk.Label(
            self.master, text='Apellido', font=('bold', 14))
        self.apellido_label.grid(row=0, column=2, sticky=tk.W)
        self.apellido_entry = tk.Entry(
            self.master, textvariable=self.apellido_text)
        self.apellido_entry.grid(row=0, column=3)
        # Edad
        self.edad_text = tk.StringVar()
        self.edad_label = tk.Label(
            self.master, text='Edad', font=('bold', 14))
        self.edad_label.grid(row=1, column=0, sticky=tk.W)
        self.edad_entry = tk.Entry(
            self.master, textvariable=self.edad_text)
        self.edad_entry.grid(row=1, column=1)
        # Cel
        self.cel_text = tk.StringVar()
        self.cel_label = tk.Label(
            self.master, text='Cel', font=('bold', 14))
        self.cel_label.grid(row=1, column=2, sticky=tk.W)
        self.cel_entry = tk.Entry(self.master, textvariable=self.cel_text)
        self.cel_entry.grid(row=1, column=3)
        # Email
        self.email_text = tk.StringVar()
        self.email_label = tk.Label(
            self.master, text='Email', font=('bold', 14))
        self.email_label.grid(row=1, column=4, sticky=tk.W)
        self.email_entry = tk.Entry(self.master, textvariable=self.email_text)
        self.email_entry.grid(row=1, column=5)

        # Lista de contactos (listbox)
        self.contactos_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.contactos_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Creo scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # Seteo la scrollbar a contactos
        self.contactos_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.contactos_list.yview)

        # Seleccion multiple
        self.contactos_list.bind('<<ListboxSelect>>', self.seleccion_item)

        # Botones
        self.btn_agregar = tk.Button(
            self.master, text="Agregar", width=12, command=self.agregar_item)
        self.btn_agregar.grid(row=2, column=0, pady=20)

        self.btn_borrar = tk.Button(
            self.master, text="Borrar", width=12, command=self.borrar_item)
        self.btn_borrar.grid(row=2, column=1)

        self.btn_modificar = tk.Button(
            self.master, text="Modificar", width=12, command=self.modificar_item)
        self.btn_modificar.grid(row=2, column=2)

        self.btn_limpiar = tk.Button(
            self.master, text="Limpiar entrada", width=12, command=self.limpiar_text)
        self.btn_limpiar.grid(row=2, column=3)

        self.btn_color = tk.Button(
            self.master, text="Color Aleatorio", width=12, command=self.cambia_color)
        self.btn_color.grid(row=2, column=4)

        #Boton con Imagen

        self.btn_img = PhotoImage(file="Random_color.gif")

        self.btn_imagen = tk.Button(
            self.master, image=self.btn_img, height=120, width=120, command=self.ver_imagen)
        self.btn_imagen.grid(row=2, column=5)

    def populate_list(self):
        """ Borra el Item antes de actualizar. De esta manera cuano se continua presionanado lo, no se sigue llenando la lista"""
        self.contactos_list.delete(0, tk.END)
        # Loop through records
        for row in db.consulta():
            # Insert into list
            self.contactos_list.insert(tk.END, row)

    # Agregamos un nuevo item
    def agregar_item(self):
        if self.nombre_text.get() == '' or self.apellido_text.get() == '' or self.edad_text.get() == '' or self.cel_text.get() == '' or self.email_text.get() == '':
            messagebox.showerror(
                "Campo obligatorio", "Por favor, complete todos los campos")
            return
        print(self.nombre_text.get())
        # Insertar en la BD
        db.insertar(self.nombre_text.get(), self.apellido_text.get(), self.edad_text.get(), self.cel_text.get(), self.email_text.get())
        # Limpiar lista
        self.contactos_list.delete(0, tk.END)
        # Insertar en la tabla
        self.contactos_list.insert(tk.END, (self.nombre_text.get(), self.apellido_text.get(
        ), self.edad_text.get(), self.cel_text.get(), self.email_text.get()))
        self.limpiar_text()
        self.populate_list()

    # Se ejecuta cuando el item es seleccionado
    def seleccion_item(self, event):
        """ Crea el item global seleccionado para usar en otras funciones """
        # global self.selected_item
        try:
            # Obtiene el indice
            index = self.contactos_list.curselection()[0]
            # Obtiene el item_selecionado
            self.item_selecionado = self.contactos_list.get(index)
            # print(item_selecionado) # Imprime tupla

            # agregar texto a las entradas
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(tk.END, self.item_selecionado[1])
            self.apellido_entry.delete(0, tk.END)
            self.apellido_entry.insert(tk.END, self.item_selecionado[2])
            self.edad_entry.delete(0, tk.END)
            self.edad_entry.insert(tk.END, self.item_selecionado[3])
            self.cel_entry.delete(0, tk.END)
            self.cel_entry.insert(tk.END, self.item_selecionado[4])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.item_selecionado[5])
        except IndexError:
            pass

    # Borra el item
    def borrar_item(self):
        db.borrar(self.item_selecionado[0])
        self.limpiar_text()
        self.populate_list()

    # actualiza el item
    def modificar_item(self):
        db.modificar(self.item_selecionado[0], self.nombre_text.get(
        ), self.apellido_text.get(), self.edad_text.get(), self.cel_text.get(), self.email_text.get())
        self.populate_list()

    # Limpia todos el texto de los campos
    def limpiar_text(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.cel_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
    
    def cambia_color(self):
        """Cambia color aleatoriamente, basado en la generacion random de un numero en base Hexa"""

        r = lambda: random.randint(0,255)

        self.color = ('#%02X%02X%02X' % (r(),r(),r()))

        root.configure(background=self.color)

        print(self.color)

    def ver_imagen(self):
        """Muestra una imagen determinada"""

        r = lambda: random.randint(0,255)

        self.color = ('#%02X%02X%02X' % (r(),r(),r()))

        root.configure(background=self.color)

        print(self.color)

        messagebox.showinfo("Color aleatorio", message="Cambiamos de forma aleatoria el color del fondo")

root = tk.Tk()
app = Agenda(master=root)
app.mainloop()