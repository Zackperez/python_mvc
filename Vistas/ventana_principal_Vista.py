from ventana_principal import *
from tkinter import ttk
import tkinter as tk

class Ventana_Principal_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.opcion = tk.StringVar()
        idiomas = ("Español", "Aleman", "Portugués", "Ruso", "Coreano","Japones")
        self.combo_idiomas = ttk.Combobox(self.parent,width=10,textvariable=self.opcion,values=idiomas)
        self.combo_idiomas.current(0)
        self.combo_idiomas.grid(column=0, row=4)

        self.txt_lbl()
        self.botones_widget()
        self.configurar_ventana()

    def txt_lbl(self):
        #def on_entry_validate(S): return S.isempty()
        #vcmd = (root.register(on_entry_validate),'%S')
 
        self.lblTextoTraducir = tk.Label(self.parent,text="texto a traducir: ").grid(row=0, column=0)
        #validatecommand=vcmd    
        self.txtTraducir = tk.Entry(self.parent, validate="key")
        self.txtTraducir.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=30)

        self.lblTextoTraducido = tk.Label(self.parent,text="texto traducido: ").grid(row=0, column=2)

        self.lblres = tk.Label(self.parent, text="Resultado")
        self.lblres.grid(row=3, column=0)

    def configurar_ventana(self):
        self.parent.geometry("480x300")
        self.parent.resizable(0, 0)

    def botones_widget(self):
        self.btnguardar = tk.Button(self.parent,text="Guardar")
        self.btnguardar.grid(row=2, column=0)

        self.btnmostrar = tk.Button(self.parent,text="Mostrar")
        self.btnmostrar.grid(row=2, column=1)

    def mostrar_resultado(self, message):
        self.lblres['text'] = message

    def mostrar_error(self,message):
        self.lblres['text'] = message

    def campo_vacio (self, message):
        self.lblres['text'] = message
