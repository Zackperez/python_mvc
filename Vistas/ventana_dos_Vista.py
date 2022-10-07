from ventana_principal import *
from tkinter import ttk
import tkinter as tk
import openai
from tkinter import *
class Ventana_dos_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.decorar_ventana()


    def configurar_ventana(self):
        self.parent.config(bg="white")
        self.parent.iconbitmap("Imagenes/icono-twice.ico")#Icono de la ventana
        self.parent.title("Analisis de sentimientos y creación de preguntas") #Aplica un titulo a la ventana
        self.dimensiones_ventana()
        self.parent.resizable(0, 0)

    def decorar_ventana(self):
        
        
        
        self.lblFrameTitulo_servicio_sentimiento = tk.LabelFrame(self.parent, text = "Analizar Sentimiento")
        self.lblFrameTitulo_servicio_sentimiento.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '25', 'bold'))
        self.lblFrameTitulo_servicio_sentimiento.grid(row = 0, column = 0, padx = 40, pady = 10, ipady = 50, ipadx=50)
        
        self.lblInstruccionesSentimiento = tk.Label(self.lblFrameTitulo_servicio_sentimiento, text = "Ingresa acontinuación el texto para analizar el sentimiento")
        self.lblInstruccionesSentimiento.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lblInstruccionesSentimiento.grid(row = 1, column = 0, ipadx = 10)
        
        self.lblFrameAnalizar_sentimiento = tk.LabelFrame(self.parent, text = "Sentimiento")
        self.lblFrameAnalizar_sentimiento.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameAnalizar_sentimiento.grid(row = 1, column = 0, padx = 40, pady = 10, ipady = 20, ipadx = 10)        
        
        self.txtEntrada = tk.Entry(self.lblFrameAnalizar_sentimiento, relief="solid")
        self.txtEntrada.grid(row = 0,column = 0, ipadx = 140, padx = 10)
        
        self.lblresultado=tk.Label(self.lblFrameAnalizar_sentimiento,text = "Acá se mostrará el sentimiento generado",font = ('Roboto', 10),bg="white")
        self.lblresultado.grid(row = 2,column = 0, pady = 5)
        
        self.btnEnviar = tk.Button(self.lblFrameAnalizar_sentimiento, text = "Generar", width = 10,height = 1)
        self.btnEnviar.grid(row = 0, column = 1, pady = 5)
        
        
        
        
        self.lblFrameGenerar_Preguntas = tk.LabelFrame(self.parent, text = "Listas y preguntas")
        self.lblFrameGenerar_Preguntas.config(bg = "#0D1216", fg = "#FFBD59", font = ('Roboto', '30', 'bold'))
        self.lblFrameGenerar_Preguntas.grid(row = 1, column = 0, padx = 40, pady = 10, ipady = 20, ipadx = 10)        
        
        self.txtEntrada = tk.Entry(self.lblFrameGenerar_Preguntas, relief="solid")
        self.txtEntrada.grid(row = 0,column = 0, ipadx = 140, padx = 10)
        
        self.txtRespuesta = tk.Text(self.lblFrameGenerar_Preguntas, relief = "solid", width = 50, height = 15)
        self.txtRespuesta.config(wrap=WORD)
        self.txtRespuesta.grid(row = 9,column = 0,padx = 10,pady = 0, ipadx = 50, ipady = 10)
    
        
        self.btnEnviar = tk.Button(self.lblFrameGenerar_Preguntas, text = "Generar", width = 10,height = 1)
        self.btnEnviar.grid(row = 0, column = 1, pady = 5)
        
        
        
        
        
        self.lblPregunta=tk.Label(self.parent,text="Escribe un tema para realizar preguntas: ",font=('Roboto', 10), bg="white")
        #self.lblPregunta.grid(row=4,column=0,pady=5)

        self.txtEntrada_pregunta = tk.Entry(self.parent, borderwidth=1, relief="solid")
        #self.txtEntrada_pregunta.grid(row=5,column=0,padx=10,pady=5,ipadx=180,ipady=40)

        self.lblCantidad_preguntas=tk.Label(self.parent,text="Escoge la cantidad de preguntas que quieres generar: ",font=('Roboto', 10), bg="white")
        #self.lblCantidad_preguntas.grid(row=6,column=0,pady=5)
        
        current_value = tk.StringVar(value=2)
        self.spin_box = ttk.Spinbox(self.parent, from_ = 2 , to = 10, textvariable = current_value, wrap=True)
        #self.spin_box.grid(row=7,column=0,pady=5)
        
        self.txtRespuesta = tk.Text(self.parent, borderwidth=1, relief="solid",width=50,height=15)
        #self.txtRespuesta.grid(row=9,column=0,padx=10,pady=0,ipadx=50,ipady=10)
        self.txtRespuesta.config(wrap=WORD)

        #self.botones_widget()
        #self.botones_spinbox()
        
    def dimensiones_ventana(self): #Funcion que va dentro de configurar_ventana()
        wventana = 610
        hventana = 600
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def botones_widget(self):      #Funcion que va dentro de configurar_ventana()
        pass

    def botones_spinbox(self):      #Funcion que va dentro de configurar_ventana()
        self.btnspin = tk.Button(self.parent,text="Guardar", width=10,height=1)
        self.btnspin.grid(row=8, column=0,pady=5)
