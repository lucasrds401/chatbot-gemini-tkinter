import customtkinter as ctk
import os
from dotenv import load_dotenv
from google import genai

windows_two, camp, windows_three = None, None, None #criação das variáveis

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key=GEMINI_API_KEY)#"Chamar" a chave da API

ctk.set_appearance_mode("dark") #Tema das janelas

def user(question):
    response = client.models.generate_content(model="models/gemini-2.5-flash",contents=question )
    return response.text

def open_two_page(): #Segunda Janela
    global windows_two, camp

    windows_one.withdraw()

    windows_two = ctk.CTkToplevel()
    windows_two.title("CHATBOT")
    windows_two.geometry("400x200")

    ctk.CTkLabel(windows_two, text="Faça seu questionamento:").pack(pady=10)

    camp = ctk.CTkEntry(windows_two, width=250)
    camp.pack(pady=10)

    ctk.CTkButton(windows_two, text="Enviar",command=open_three_page).pack(pady=10) #Botão "Enviar"
    camp.bind("<Return>", lambda event: open_three_page())


def open_three_page(): #Terceira Janela
    global camp

    question = camp.get()
    resposta = user(question)

    windows_two.withdraw()

    windows_three = ctk.CTkToplevel()
    windows_three.title("CHATBOT")
    windows_three.geometry("800x400")

    ctk.CTkLabel(windows_three,text=resposta,wraplength=700).pack(pady=20)

# PROGRAMA

windows_one = ctk.CTk() #primeira janela
windows_one.title("Cadastro")
windows_one.geometry("300x200")

ctk.CTkLabel(windows_one, text="Nome").pack(pady=5)
one_campo = ctk.CTkEntry(windows_one)
one_campo.pack()

ctk.CTkLabel(windows_one, text="Senha").pack(pady=5)
two_campo = ctk.CTkEntry(windows_one, show="*")
two_campo.pack()

ctk.CTkButton(windows_one,text="Enviar",command=open_two_page).pack(pady=10)
one_campo.bind("<Return>", lambda event: open_two_page())
two_campo.bind("<Return>", lambda event: open_two_page())

windows_one.mainloop()