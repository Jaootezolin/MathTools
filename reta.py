import tkinter as tk
from tkinter import messagebox
def abrir_reta():
    win = tk.Toplevel()
    win.title("Reta no Plano Cartesiano")
    win.geometry("400x300")
    tk.Label(win, text="Coeficiente angular (a):").pack()
    entry_a = tk.Entry(win)
    entry_a.pack()
    tk.Label(win, text="Coeficiente linear (b):").pack()
    entry_b = tk.Entry(win)
    entry_b.pack()
    tk.Label(win, text="Valor de x:").pack()
    entry_x = tk.Entry(win)
    entry_x.pack()
    resultado_label = tk.Label(win, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=10)
    def calcular():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            x = float(entry_x.get())
            y = a*x + b
            resultado_label.config(text=f"y = {y:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")
    tk.Button(win, text="Calcular", command=calcular).pack(pady=10)
