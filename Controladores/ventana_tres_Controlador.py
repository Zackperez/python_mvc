from ventana_principal import *
from Modelos.ventana_tres_Modelo import *
from Vistas.ventana_tres_Vista import *
import json
import tkinter as tk
import nlpcloud

class Ventana_Tres_Controller:

    def __init__(self, root):
        self.model = Ventana_Tres_Model()
        self.view = Ventana_Tres_View(root)
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

    def agregar_datos_generales_json(self, n1, n2, res):
        informacion_json_final = []
        if self.existe_historial() == True:
            nuevos_datos = {"numero1": n1, "numero2": n2, "resultado": res}
            with open("historial.json") as archivo_json:
                datos = json.load(archivo_json)
            datos.append(nuevos_datos)

            with open("historial.json", 'w') as archivo_json:
                json.dump(datos, archivo_json, indent=3)
                print("Se han añadido los siguientes datos al archivo " +archivo_json.name + "\n")
        else:

            informacion_usuario = {"numero1": n1,"numero2": n2,"resultado": res}
            with open("historial.json", 'w') as archivo_json:
                informacion_json_final.append(informacion_usuario)
                json.dump(informacion_json_final, archivo_json, indent=3)
                print(archivo_json.name + " creado exitosamente")

    def existe_historial(self):
        try:
            with open('historial.json') as archivo:
                return True
        except FileNotFoundError as e:
            return False

    def combo_seleccion(self):
        if self.view.combo_idiomas.get() == "Español":
            return "spa_Latn"
        if self.view.combo_idiomas.get() == "Aleman":
            return "deu_Latn"
        if self.view.combo_idiomas.get() == "Portugués":
            return "por_Latn"
        if self.view.combo_idiomas.get() == "Ruso":
            return "rus_Cyrl"
        if self.view.combo_idiomas.get() == "Coreano":
            return "kor_Hang"
        if self.view.combo_idiomas.get() == "Japones":
            return "jpn_Jpan"

    def traducir_el_texto(self):
        idioma = self.combo_seleccion()
        client = nlpcloud.Client("nllb-200-3-3b","0c763b98f814c4649754c8c6e50425f99969aa72",gpu=False)
        texto_traducido = client.translation(self.model.get_texto_traducir(),source="eng_Latn",target=idioma)
        self.view.lblres['text'] = texto_traducido
