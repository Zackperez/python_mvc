import tkinter as tk
import json
import nlpcloud
from tkinter import ANCHOR, ttk
import os
import openai

class Model:

    def __init__(self):
        self.texto_traducir = tk.StringVar()

    def get_texto_traducir(self):
        return self.texto_traducir

    def set_texto_traducir(self, texto_traducir):
        self.texto_traducir = texto_traducir


class View(tk.Frame):

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
        
        def on_entry_validate(S): return S.isalpha()
        vcmd = (root.register(on_entry_validate),'%S')

        self.lblTextoTraducir = tk.Label(self.parent,text="texto a traducir: ").grid(row=0, column=0)

        self.txtTraducir = tk.Entry(self.parent, validate="key", validatecommand=vcmd)
        self.txtTraducir.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=30)

        self.lblTextoTraducido = tk.Label(self.parent,text="texto traducido: ").grid(row=0, column=2)
        self.lblTextoTraducido = tk.Label(self.parent, text="").grid(row=0, column=3)

        self.lblres = tk.Label(self.parent, text="Resultado").grid(row=3, column=0)

    def configurar_ventana(self):
        self.parent.geometry("480x300")
        self.parent.resizable(0, 0)

    def botones_widget(self):
        self.btnguardar = tk.Button(text="Guardar")
        self.btnguardar.grid(row=2, column=0)

        self.btnmostrar = tk.Button(text="Mostrar")
        self.btnmostrar.grid(row=2, column=1)

    def mostrar_resultado(self, message):
        self.lblres['text'] = message

    def mostrar_error(self,message):
        self.lblres['text'] = message

    def campo_vacio (self, message):
        self.lblres['text'] = message

class Controller:

    def __init__(self, root):
        self.model = Model()
        self.view = View(root)

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


if __name__ == "__main__":


    openai.api_key = os.getenv("OPENAI_API_KEY")
    conversation ="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:"

    i = 1
    while (i !=0):
        question = input("Human: ")
        conversation += "\nHuman:" + question + "\nAI:"
        response = openai.Completion.create(
            model="davinci",
            prompt = conversation,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n"," Human:", " AI:"]
        )

        answer = response.choices[0].text.strip()
        conversation += answer
        print("AI: "+ answer)

"""  
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
import tkinter as tk

class Vista:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Programa ")
        self.ventana1.geometry("500x300")
        self.lbln1=tk.Label(self.ventana1, text="Numero 1")
        self.lbln1.grid( row=0,column=0)
        self.txtn1=tk.Entry()
        self.txtn1.grid(row=0,column=1)

        self.lbln2=tk.Label(self.ventana1, text="Numero 2")
        self.lbln2.grid(row=1,column=0)
        self.txtn2=tk.Entry()
        self.txtn2.grid(row=1,column=1)   

        self.lblres=tk.Label(self.ventana1, text="Resultado")
        self.lblres.grid(row=3,column=0)
        self.btncalcular=tk.Button(text="Calcular",command= self.boton_guardar_clicked)
        self.btncalcular.grid(row=2,column=0)

        self.control = None
        self.ventana1.mainloop()

    def mostrar_resultado(self, message):
        self.lblres['text'] = message

    def set_control(self, control):
        self.control = control

    def boton_guardar_clicked(self):
        if self.control:
            self.control.mostrar_resultado(self.lbln1.get())
 

class Modelo:
    def __init__(self,n1):
        self.numero1 = n1

    def set_numero1(self,n1):
        self.numero1 = n1        

    def get_numero1(self):
        return self.numero1       

class Controlador:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def muestra_numero (self, n1):
        self.modelo.numero1 = n1
        self.vista.mostrar_resultado(f'El numero es {n1}')

class App:
    def __init__(self):
        super().__init__()
        modelo = Modelo(2)
        vista = Vista()
        control = Controlador(modelo,vista)
        vista.set_control(control)       

if __name__ == '__main__':
    ap = App()
"""  