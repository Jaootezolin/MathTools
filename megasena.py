import tkinter as tk
import random

def abrir_megasena():
    win = tk.Toplevel()
    win.title("Simulador da Mega-Sena")
    win.geometry("400x250")

    resultado_label = tk.Label(win, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=30)

    def sortear():
        numeros = sorted(random.sample(range(1, 61), 6))
        resultado_label.config(text=f"Números sorteados:\n{numeros}")

    tk.Button(win, text="Sortear Números", command=sortear).pack(pady=10)
