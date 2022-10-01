import tkinter as tk
from Controladores.ventana_principal_Controlador import *
from Controladores.ventana_dos_Controlador import *
from Controladores.ventana_tres_Controlador import *
from tkinter import *

class Aplicacion:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        #Configuración de la ventana
        self.configurar_ventana()
        #Widgets de la ventana
        self.decorar_ventana_principal()
        #Inicialización de la ventana principal
        self.ventana_principal.mainloop()

    def configurar_ventana(self):
        self.ventana_principal.state('zoomed') #Inicializa la ventana maximizada
        self.ventana_principal.title("Menu principal") #Aplica un titulo a la ventana
        self.ventana_principal.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.ventana_principal.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana

    def menu_ventana_principal(self):
        self.menuppal = tk.Menu(self.ventana_principal)
        self.opciones = tk.Menu(self.menuppal)
        self.opciones.add_command(label="Ventana 1", command = self.ventana_uno)
        self.opciones.add_command(label="Ventana 2", command = self.ventana_dos)
        self.opciones.add_command(label="Ventana 3", command = self.ventana_tres)
        self.menuppal.add_cascade(label="Opciones", menu=self.opciones)
        self.ventana_principal.config(menu=self.menuppal)

    def decorar_ventana_principal(self):
        #Imagen de fondo en la ventana_principal
        self.imagen_inicio = tk.PhotoImage(file="Imagenes/logo.png")  
        self.label_python=tk.Label(self.ventana_principal,image=self.imagen_inicio)
        self.label_python.grid(row=1,column=6,padx=1.4)
        #Menú de la ventana principal
        self.menu_ventana_principal()

    #Inicializador de ventanas
    def ventana_uno(self):
        root = tk.Tk()
        Ventana_Principal_Controller(root)
        root.mainloop()

    def ventana_dos(self):
        root2 = tk.Tk()
        Ventana_Dos_Controller(root2)
        root2.mainloop()

    def ventana_tres(self):
        root3 = tk.Tk()
        Ventana_Tres_Controller(root3)
        root3.mainloop()


