from turtle import width
from ventana_principal import *
from tkinter import ttk
import tkinter as tk
from tkinter import *

class Ventana_Tres_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.txt_lbl()
        self.botones_widget()
        self.configurar_ventana()

    def txt_lbl(self):

        self.lblnombrev2=tk.Label(self.parent,text="CHATBOT con OpenAI",font=('Roboto', 20))
        self.lblnombrev2.grid(row=0,column=0,padx=0,pady=5,ipadx=0,ipady=10)

        myscroll = Scrollbar(self.parent) 
        self.mylist = Listbox(self.parent, yscrollcommand = myscroll.set)  
        self.mylist.grid(row=1,column=0,padx=10,pady=0,ipadx=80,ipady=140)  

        self.lblnombrev2=tk.Label(self.parent,text="Escribe acá",font=('Roboto', 10))
        self.lblnombrev2.grid(row=2,column=0)

        self.txtTexto = tk.Entry(self.parent)
        self.txtTexto.grid(row=3,column=0,padx=10,pady=0,ipadx=80,ipady=0)

    def configurar_ventana(self):
        wventana = 300
        hventana = 600

        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        self.parent.resizable(0, 0)

    def botones_widget(self):
        self.btnenviar = tk.Button(self.parent,text="Enviar")
        self.btnenviar.grid(row=4, column=0)
