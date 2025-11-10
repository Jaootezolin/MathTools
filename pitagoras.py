import tkinter as tk
from tkinter import messagebox
import math

def abrir_pitagoras():
    pit_win = tk.Toplevel()
    pit_win.title("Calculadora de Pitágoras")
    pit_win.geometry("400x300")

    tk.Label(pit_win, text="Cateto A:").pack()
    entry_a = tk.Entry(pit_win)
    entry_a.pack()

    tk.Label(pit_win, text="Cateto B:").pack()
    entry_b = tk.Entry(pit_win)
    entry_b.pack()

    resultado_label = tk.Label(pit_win, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=10)

    def calcular():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = math.sqrt(a**2 + b**2)
            resultado_label.config(text=f"Hipotenusa: {c:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números válidos!")

    tk.Button(pit_win, text="Calcular", command=calcular).pack(pady=10)
