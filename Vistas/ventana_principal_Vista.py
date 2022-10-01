from ventana_principal import *
from tkinter import ttk
import tkinter as tk

class Ventana_Principal_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configurar_ventana()
        self.decorar_ventana_uno()

    def configurar_ventana(self):
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.resizable(0,0)
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
    
        wventana = 600
        hventana = 700

        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2+500)
        pheight = round(htotal/2-hventana/2)

        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        self.parent.resizable(0, 0)

    def decorar_ventana_uno(self):
        #Simple Label que indica que es un campo para escribir texto (que se va a traducir)
        self.lblTextoTraducir = tk.Label(self.parent,text="texto a traducir: ").grid(row=0, column=0)

        #Campo donde se escribe el texto que se va a traducir posteriormente
        self.txtTraducir = tk.Entry(self.parent, validate="key")
        self.txtTraducir.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=30)

        self.comboBox_idiomas()
    
        #Simple label que indica que indica que se va a mostrar el texto traducido
        self.lblTextoTraducido = tk.Label(self.parent,text="texto traducido: ").grid(row=0, column=2)
        #Label que recibe el texto traducido
        self.lblres = tk.Label(self.parent, text="Texto traducido: ")
        self.lblres.grid(row=3, column=0)

        self.botones_widget()

    def comboBox_idiomas(self):
        self.opcion = tk.StringVar()
        idiomas = ("Español", "Aleman", "Inglés", "Portugués", "Ruso", "Coreano", "Japones")
        self.combo_idiomas = ttk.Combobox(self.parent,width=10,textvariable=self.opcion,values=idiomas)
        self.combo_idiomas.current(0)
        self.combo_idiomas.grid(column=0, row=4)

    def botones_widget(self):
        self.btnGuardar_texto_escrito = tk.Button(self.parent,text="Guardar")
        self.btnGuardar_texto_escrito.grid(row=2, column=0)

        self.btnMostrar_traduccion = tk.Button(self.parent,text="Mostrar")
        self.btnMostrar_traduccion.grid(row=2, column=1)
