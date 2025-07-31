import tkinter as tk
import random
from tkinter import messagebox
import winsound

def responder_sim():
    messagebox.showinfo("Resposta", "Eu sabia que você me ama! ❤️😘")

def fugir(event=None):
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()

    nova_x = random.randint(0, largura_janela - 100)
    nova_y = random.randint(0, altura_janela - 50)

    botao_nao.place(x=nova_x, y=nova_y)

    # Muda a cor
    cor_random = random.choice(["red", "blue", "green", "purple", "orange"])
    botao_nao.config(bg=cor_random, activebackground=cor_random)

    # Toca som
    winsound.Beep(800, 100)

# Janela
janela = tk.Tk()
janela.title("Pergunta do Amor 💘")
janela.geometry("450x450")
janela.config(bg="#ffe6f0")
janela.resizable(False, False)

# Pergunta
pergunta = tk.Label(
    janela,
    text="Você me ama?",
    font=("Comic Sans MS", 20, "bold"),
    bg="#ffe6f0",
    fg="#ff007f"
)
pergunta.pack(pady=30)

# Botão SIM
botao_sim = tk.Button(
    janela,
    text="Sim ❤️",
    font=("Arial", 14, "bold"),
    bg="#90ee90",
    activebackground="#32cd32",
    command=responder_sim
)
botao_sim.place(x=120, y=180)

# Botão NÃO — sem função de clique!
botao_nao = tk.Button(
    janela,
    text="Não 💔",
    font=("Arial", 14, "bold"),
    bg="#ff9999",
    activebackground="#ff4d4d"
)
botao_nao.place(x=250, y=180)

# Botão "Não" foge ao tentar clicar OU passar o mouse
botao_nao.bind("<Enter>", fugir)
botao_nao.bind("<ButtonPress>", fugir)

# Rodar app
janela.mainloop()
