from ventana_principal import *
from Modelos.ventana_tres_Modelo import *
from Vistas.ventana_tres_Vista import *
import openai

class Ventana_Tres_Controller:

    def __init__(self, root):
        self.model = Ventana_Tres_Model()
        self.view = Ventana_Tres_View(root)

        self.view.btnEnviar_texto_hacia_IA.config(command=self.chatBot)

    def devolver_respuestas(humano_preguntas, ia_respuestas): #Usado para el JSON
        conversacion = {}
        conversacion = {"Humano":humano_preguntas, "IA":ia_respuestas}
        return conversacion

    def chatBot(self):
        try:
            openai.api_key =("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")
            humano_preguntas = []
            ia_respuestas = []
            conversation ="Fui creado por OpenAI. ¿Cómo te puedo ayudar hoy?"
            print(conversation)
            #self.view.historial_de_conversacion.insert(END,conversation)
            pregunta_usuario = self.view.txtEntrada_texto_usuario.get()
        
            self.view.historial_de_conversacion.insert(END,"Humano: "+pregunta_usuario)
            if pregunta_usuario == "Adios":
                print("AI: ¡Adiós!")
                self.view.parent.destroy()

            humano_preguntas.append(pregunta_usuario)
            
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
            ia_respuestas.append(response.choices[0].text)

            conversation += respuesta_ia

            self.view.historial_de_conversacion.insert(END,"IA: "+respuesta_ia)

        except Exception as e:
            print(e)
