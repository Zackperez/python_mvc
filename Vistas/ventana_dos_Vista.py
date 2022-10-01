from ventana_principal import *
from tkinter import ttk
import tkinter as tk

class Ventana_dos_View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()

    def configurar_ventana(self):
        self.parent.geometry("480x300")
        self.parent.resizable(0, 0)