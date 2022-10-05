from ventana_principal import *
from Modelos.ventana_tres_Modelo import *
from Vistas.ventana_tres_Vista import *
import json
import openai

class Ventana_Tres_Controller:

    def __init__(self, root):
        self.model = Ventana_Tres_Model()
        self.view = Ventana_Tres_View(root)
        self.view.btnEnviar_texto_hacia_IA.config(command=self.chatBot)

    def existe_historial(self):
        try:
            with open('historial.json') as archivo:
                return True
        except FileNotFoundError as e:
            return False

    def devolver_respuestas(self,nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2):
        diccionario_generado = {}
        diccionario_generado = {espacio_1 : valor_espacio_1, espacio_2 : valor_espacio_2}
        respuesta_final = {nombre_servicio: diccionario_generado}
        return respuesta_final

    def crear_traduccion_json(self, nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2):

        if self.existe_historial() == True:
            nuevos_datos = self.devolver_respuestas(nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2)
            with open("historial.json",encoding="utf-8") as archivo_json:
                datos = json.load(archivo_json)
                datos.append(nuevos_datos)
            with open("historial.json", 'w',encoding="utf-8") as archivo_json:
                json.dump(datos, archivo_json, indent=3, ensure_ascii=False)
                print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")
        else:
            with open("historial.json", 'w',encoding="utf-8") as archivo_json:
                historial = []
                historial.append(self.devolver_respuestas(nombre_servicio, espacio_1, valor_espacio_1, espacio_2, valor_espacio_2))
                json.dump(historial, archivo_json, indent=3, ensure_ascii=False)
                print(archivo_json.name+" creado exitosamente")
                print("Se han añadido los siguientes datos al archivo " + archivo_json.name+"\n")

    def chatBot(self):
        try:
            openai.api_key =("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")
            humano_preguntas = []
            ia_respuestas = []
            conversation ="Fui creado por OpenAI. ¿Cómo te puedo ayudar hoy?"
            #self.view.historial_de_conversacion.insert(END,conversation)
            pregunta_usuario = self.view.txtEntrada_texto_usuario.get()
        
            self.view.historial_de_conversacion.insert(END,"Humano: "+pregunta_usuario)
            if pregunta_usuario == "Adios":
                print("AI: ¡Adiós!")
                self.crear_traduccion_json("Chat Bot", "Humano preguntas", humano_preguntas, "IA respuestas", ia_respuestas)
                self.view.parent.destroy()
            
            conversation += "\nHuman:" + pregunta_usuario + "\nAI:"
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

            respuesta_ia = response.choices[0].text.strip()
            conversation += respuesta_ia

            humano_preguntas.append(self.view.txtEntrada_texto_usuario.get())
            ia_respuestas.append(respuesta_ia)

            self.view.historial_de_conversacion.insert(END,"IA: "+respuesta_ia)
            self.view.txtEntrada_texto_usuario.delete(0,END)
            
        except Exception as e:
            print(e)
