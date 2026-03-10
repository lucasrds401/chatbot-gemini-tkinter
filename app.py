import customtkinter as ctk
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key=GEMINI_API_KEY) #API KEY

ctk.set_appearance_mode("dark") #Configuração de tema(dark)

def user(question): #Função para "Chamar a API"
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=question)
    
    return response.text


def open_two_page(): #Página de pergunta do ChatBot
    global windows_two, camp

    windows_one.withdraw()

    windows_two = ctk.CTkToplevel()
    windows_two.title("CHATBOT")
    windows_two.geometry("400x200")

    ctk.CTkLabel(windows_two, text="Faça seu questionamento:").pack(pady=10)

    camp = ctk.CTkEntry(windows_two, width=250)
    camp.pack(pady=10)

    ctk.CTkButton(windows_two,text="Enviar",command=open_three_page).pack(pady=10) #Botão de enviar


def open_three_page(): #Página do ChatBot
    global windows_three

    question = camp.get()
    resposta = user(question)

    windows_two.withdraw()

    windows_three = ctk.CTkToplevel()
    windows_three.title("CHATBOT")
    windows_three.geometry("800x400")

    ctk.CTkLabel(
        windows_three,
        text=resposta,
        wraplength=700
    ).pack(pady=20)


# PROGRAMA

windows_one = ctk.CTk()
windows_one.title("Cadastro")
windows_one.geometry("300x200")

ctk.CTkLabel(windows_one, text="Nome").pack(pady=5)
one_campo = ctk.CTkEntry(windows_one)
one_campo.pack()

ctk.CTkLabel(windows_one, text="Senha").pack(pady=5)
two_campo = ctk.CTkEntry(windows_one, show="*")
two_campo.pack()

ctk.CTkButton(
    windows_one,
    text="Enviar",
    command=open_two_page
).pack(pady=10)

windows_one.mainloop()