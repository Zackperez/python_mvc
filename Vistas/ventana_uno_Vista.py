from ventana_principal import *
from tkinter import ttk
import tkinter as tk

class Ventana_Uno_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.decorar_ventana_uno()

    def configurar_ventana(self):
        self.parent.config(bg="#0D1216")
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.title("Traductor y detecciòn de lenguaje") #Aplica un titulo a la ventana
        self.parent.resizable(0,0)
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 350
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana_uno(self):
        #Simple Label que indica que es un campo para escribir texto (que se va a traducir)
        self.lblTextoTraducir = tk.Label(self.parent,text="Texto a traducir: ")
        self.lblTextoTraducir.config(bg="#0D1216", fg = "#FFBD59", font=('Roboto', '20', 'bold'))
        self.lblTextoTraducir.grid(row=0, column=1)

        self.lblInstruccionesTraduccion = tk.Label(self.parent, text = "Ingresa un texto al que quieres traducir\nRecuerda que el traductor detectará automáticamente \nel lenguaje en el que fue escrito\nSolamente selecciona a qué idioma lo quieres traducir.")
        self.lblInstruccionesTraduccion.grid(row = 1, column= 1)
        self.lblInstruccionesTraduccion.config(bg="#0D1216", fg = "white", font=('Roboto', '10'))

        #Campo donde se escribe el texto que se va a traducir posteriormente
        self.txtTraducir = tk.Entry(self.parent, validate="key", borderwidth=1, relief="solid")
        self.txtTraducir.grid(row=2,column=1,padx=5,pady=0,ipadx=180,ipady=40)

        self.comboBox_idiomas()
    
        #Simple label que indica que se va a mostrar el texto traducido
        self.lblTextoTraducido = tk.Label(self.parent,text="Texto traducido: ")
        self.lblTextoTraducido.config(bg="white")
        self.lblTextoTraducido.grid(row=3, column=0)
        
        #Label que recibe el texto traducido
        self.lblres = tk.Label(self.parent, text="Resultado texto traducido: ",bg="white")
        self.lblres.grid(row=4, column=1)

        self.botones_widget()

    def comboBox_idiomas(self):
        self.opcion = tk.StringVar()
        idiomas = ("Español", "Aleman", "Inglés", "Portugués", "Ruso", "Coreano", "Japones")
        self.combo_idiomas = ttk.Combobox(self.parent,width=10,textvariable=self.opcion,values=idiomas)
        self.combo_idiomas.current(0)
        self.combo_idiomas.grid(row = 2, column=2)

    def botones_widget(self):
        self.btnGuardar_texto_escrito = tk.Button(self.parent,text="Guardar", width=10,height=1)
        self.btnGuardar_texto_escrito.grid(row=5, column=0,padx=10,pady=0)

        self.btnMostrar_traduccion = tk.Button(self.parent,text="Mostrar", width=10,height=1)
        self.btnMostrar_traduccion.grid(row=5, column=1,padx=0,pady=10)
