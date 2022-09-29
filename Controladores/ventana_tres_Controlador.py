from ventana_principal import *
from Modelos.ventana_tres_Modelo import *
from Vistas.ventana_tres_Vista import *
import tkinter as tk
import openai
import json

class Ventana_Tres_Controller:

    def __init__(self, root):
        self.model = Ventana_Tres_Model()
        self.view = Ventana_Tres_View(root)
        self.view.btnenviar.config(command=self.chatBot)

    def devolver_respuestas(humano_respuestas, ia_respuestas):
        respuestas = {}
        respuestas = {"Humano":humano_respuestas, "IA":ia_respuestas}
        return respuestas

    def chatBot(self):
        try:
            openai.api_key =("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")
            humano_respuestas = []
            ia_respuestas = []
            conversation ="Fui creado por OpenAI. ¿Cómo te puedo ayudar hoy?"
            print(conversation)

            question = self.view.txtTexto.get()
            print(question)
            self.view.mylist.insert(END,question)
            if question == "Adios":
                print("AI: ¡Adiós!")
                
            humano_respuestas.append(question)
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
            ia_respuestas.append(response.choices[0].text)

            conversation += answer
            self.view.mylist.insert(END,answer)
            question.delete("1.0","end")
        except Exception as e:
            print(e)