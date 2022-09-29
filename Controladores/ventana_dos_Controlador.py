from ventana_principal import *
from Modelos.ventana_dos_Modelo import *
from Vistas.ventana_dos_Vista import *
import tkinter as tk
import nlpcloud

class Ventana_Dos_Controller:

    def __init__(self, root):
        self.model = Ventana_dos_Model()
        self.view = Ventana_dos_View(root)
        self.view.btnguardar.config(command=self.guardar_texto)
        self.view.btnmostrar.config(command=self.traducir_el_texto)

    def guardar_texto(self):
        try:
            self.model.texto_traducir = self.view.txtTraducir.get()
            a = self.view.combo_idiomas.get()
            print(a)
        except:
            self.borrar_campos()
            xd = "Verifica que los campos no esten vacío"
            print(xd)
            self.view.campo_vacio(xd)

    def mostrar_texto(self):
        texto = self.model.get_texto_traducir()
        self.view.lblTextoTraducido['text'] = "Texto traducido", texto

    def borrar_campos(self):
        try:
            self.view.txtTraducir.delete(0, tk.END)
        except Exception as a:
            print(a)

    def muestra_traduccion(self):
        texto_traducido = self.model.get_texto_traducir()
        self.view.lblres['text'] = texto_traducido