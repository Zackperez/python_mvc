from ventana_principal import *
from Modelos.ventana_principal_Modelo import *
from Vistas.ventana_principal_Vista import *
import tkinter as tk
import nlpcloud

class Ventana_Principal_Controller:

    def __init__(self, root):
        self.model = Ventana_Principal_Model()
        self.view = Ventana_Principal_View(root)

        self.view.btnGuardar_texto_escrito.config(command=self.guardar_texto_a_traducir)
        self.view.btnMostrar_traduccion.config(command=self.mostrar_texto_traducido)

    def guardar_texto_a_traducir(self):
        try:
            self.model.set_texto_traducir(self.view.txtTraducir.get())
            print(self.model.get_texto_traducir())
        except Exception as e:
            print(e)

    def comboBox_seleccion_idioma_traducir(self):
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
        if self.view.combo_idiomas.get() == "Inglés":
           return "eng_Latn"
    
    def detectar_idioma(self,texto): #Primer servicio
        token = "034df8cc6c50fb8e051d5df968c8dff4397e410e"
        client = nlpcloud.Client("python-langdetect", token)
        lang = client.langdetection(texto)

        a = lang.get('languages')
        listapy = a[0]
        listafinal = listapy.items()
        idioma = list(listafinal)[0][0]

        if idioma == "es":   return "spa_Latn"

        elif idioma == "de": return "deu_Latn"

        elif idioma == "pt": return "por_Latn"

        elif idioma == "ru": return "rus_Cyrl"

        elif idioma == "ko": return "kor_Hang"

        elif idioma == "ja": return "jpn_Jpan"

        elif idioma == "en": return "eng_Latn"

        else:                return print("No se detecta el idioma")
    
    def traducir_texto(self): #Segundo servicio
        #Se guarda el idioma al que se va a traducir el texto ingresado
        idioma_a_traducir_seleccionado = self.comboBox_seleccion_idioma_traducir()

        #Se guarda el texto para poder ser traducido
        texto_escrito = self.model.get_texto_traducir()

        #Se recibe en qué idioma fue escrito el texto anteriormente escrito (variable texto)
        idioma_escrito_detectado = self.detectar_idioma(texto_escrito)

        #Según el idioma en el que fue escrito el texto, se compara que no sea el mismo al que se quiera traducir, es decir, no se pueda traducir del español al español
        if idioma_escrito_detectado == idioma_a_traducir_seleccionado:
            print("No puedes traducir al mismo idioma")

        else:
            client = nlpcloud.Client("nllb-200-3-3b","0c763b98f814c4649754c8c6e50425f99969aa72",gpu=False)
            texto_traducido = client.translation(texto_escrito, source = idioma_escrito_detectado, target = idioma_a_traducir_seleccionado)
            return texto_traducido

    def mostrar_texto_traducido(self):
        self.view.lblres['text'] = self.traducir_texto()