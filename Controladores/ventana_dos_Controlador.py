from ventana_principal import *
from Modelos.ventana_dos_Modelo import *
from Vistas.ventana_dos_Vista import *
import tkinter as tk
import nlpcloud

class Ventana_Dos_Controller:

    def __init__(self, root):
        self.model = Ventana_dos_Model()
        self.view = Ventana_dos_View(root)
