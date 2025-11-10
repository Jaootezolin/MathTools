import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def abrir_parabola():
    parabola_win = tk.Toplevel()
    parabola_win.title("Parábola")
    parabola_win.geometry("400x300")

    tk.Label(parabola_win, text="Coeficiente a:").pack()
    entry_a = tk.Entry(parabola_win)
    entry_a.pack()

    tk.Label(parabola_win, text="Coeficiente b:").pack()
    entry_b = tk.Entry(parabola_win)
    entry_b.pack()

    tk.Label(parabola_win, text="Coeficiente c:").pack()
    entry_c = tk.Entry(parabola_win)
    entry_c.pack()

    def gerar_grafico():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            x = np.linspace(-10, 10, 400)
            y = a*x**2 + b*x + c

            plt.axhline(0, color='black', linewidth=0.5)  # eixo x
            plt.axvline(0, color='black', linewidth=0.5)  # eixo y
            plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
            plt.title("Gráfico da Parábola")
            plt.legend()
            plt.grid(True)
            plt.show()
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    tk.Button(parabola_win, text="Gerar Gráfico", command=gerar_grafico).pack(pady=10)
