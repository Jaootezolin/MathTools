import tkinter as tk
from tkinter import messagebox
import math

def abrir_trigonometria():
    trig_win = tk.Toplevel()
    trig_win.title("Calculadora de Trigonometria")
    trig_win.geometry("400x350")

    tk.Label(trig_win, text="Ângulo (em graus):").pack()
    entry_angulo = tk.Entry(trig_win)
    entry_angulo.pack()

    resultado_label = tk.Label(trig_win, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=10)

    def calcular():
        try:
            angulo = float(entry_angulo.get())
            rad = math.radians(angulo)

            seno = math.sin(rad)
            cosseno = math.cos(rad)
            tangente = math.tan(rad)

            resultado_label.config(
                text=f"Seno: {seno:.3f}\nCosseno: {cosseno:.3f}\nTangente: {tangente:.3f}"
            )

        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")

    tk.Button(trig_win, text="Calcular", command=calcular).pack(pady=10)
