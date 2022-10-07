import tkinter as tk

from setuptools import Command
from Controladores.ventana_uno_Controlador import *
from Controladores.ventana_dos_Controlador import *
from Controladores.ventana_tres_Controlador import *
from tkinter import *

class Ventana_Principal:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        #Configuración de la ventana
        self.configurar_ventana()
        #Widgets de la ventana
        self.decorar_ventana_principal()
        #Inicialización de la ventana principal

        self.ventana_principal.mainloop()


    def configurar_ventana(self):
        self.ventana_principal.config(bg="#0D1216")
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
        #Simple label que indica la descripcion del programa
        self.lblTituloDescripcion = tk.Label(self.ventana_principal, text="Descripción del programa: ")
        self.lblTituloDescripcion.config(bg="#0D1216", fg = "#FFBD59", font=('Roboto', '25', 'bold'))
        self.lblTituloDescripcion.grid(row=3, column=0,pady=30)
        self.lblDescripcion = tk.Label(self.ventana_principal, text="¡Bienvenido!, te encuentras en la ventana principal. \n\nEn esta ventana encontrarás un menú de opciones en la parte superior izquierda en el que podrás acceder a tres ventanas más. \n\n1. En la primera ventana podrás encontrar un traductor el cuál te permitirá traducir a los siguientes idiomas: Español, Alemán, Portugués, Ruso, Coreano, Japones, e Inglés.\n\n2. En la segunda venta podrás encontrar un analizador de emociones, que te permite saber cual es el estado en el que te encuentras dependiendo de lo que le escribas, además de poder encontrar un generador de listas y preguntas en la misma ventana según el tema que le especifiques.\n\n3. En la tercera (y última ventana) encontrarás un Chatbot con el que te podrás comunicar haciendole preguntas y así recibir una respuesta por parte del bot.")
        self.lblDescripcion.config(bg="#0D1216", fg = "white", font=('Roboto Mono Regular', '17', 'bold'),wraplength=900, justify="left")
        self.lblDescripcion.grid(row=4, column=0, pady=20, padx = 20)

        #Imagen de fondo en la ventana_principal
        self.imagen_inicio = tk.PhotoImage(file="Imagenes/toad.png")  
        self.label_python=tk.Label(self.ventana_principal,image=self.imagen_inicio)
        self.label_python.grid(row=4,column=1, padx=30)
        #Menú de la ventana principal
        self.menu_ventana_principal()

    #Inicializador de ventanas
    def ventana_uno(self):
        root = tk.Tk()
        Ventana_Uno_Controller(root)
        root.mainloop()

    def ventana_dos(self):
        root2 = tk.Tk()
        Ventana_Dos_Controller(root2)
        root2.mainloop()

    def ventana_tres(self):
        root3 = tk.Tk()
        Ventana_Tres_Controller(root3)
        root3.mainloop()


