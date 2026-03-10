import tkinter as tk
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") #Chave da API////

client = genai.Client(api_key=GEMINI_API_KEY)

def user(question): #Função para "chamar" a IA////
        response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= question)

        return response.text

def open_two_page(): #Segunda página////
    global windows_two, camp

    windows_one.withdraw()

    windows_two = tk.Toplevel()
    windows_two.title("CHATBOT")
    windows_two.geometry("400x200")

    tk.Label(windows_two, text= "Faça seu questionamento:").pack()

    camp = tk.Entry(windows_two, width=40)
    camp.pack()

    tk.Button(windows_two, text="Enviar", command=open_three_page).pack(padx=10, pady=10)

def open_three_page(): #Terceira página////
      global windows_three

      question = camp.get()
      resposta = user(question)

      windows_two.withdraw()

      windows_three = tk.Toplevel()
      windows_three.title("CHATBOT")
      windows_three.geometry("800x400")

      tk.Label(windows_three, text=resposta, wraplength=700).pack(pady=20)

#PROGRAMA////
    
windows_one = tk.Tk()

windows_one.title("Cadastro")
windows_one.geometry("300x200")

tk.Label(windows_one, text= "Nome").pack()
one_campo = tk.Entry(windows_one).pack()

tk.Label(windows_one, text= "Senha").pack()
two_campo = tk.Entry(windows_one, show= "*").pack()

button = tk.Button(windows_one,  text="Enviar", command=open_two_page).pack(padx=10, pady=10)

windows_one.mainloop()