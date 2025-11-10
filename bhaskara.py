import tkinter as tk
from tkinter import messagebox
import math

def abrir_bhaskara():
    
    bhaskara_win = tk.Toplevel()
    bhaskara_win.title("Calculadora de Bhaskara")
    bhaskara_win.geometry("400x300")

    
    tk.Label(bhaskara_win, text="Coeficiente a:").pack()
    entry_a = tk.Entry(bhaskara_win)
    entry_a.pack()

    tk.Label(bhaskara_win, text="Coeficiente b:").pack()
    entry_b = tk.Entry(bhaskara_win)
    entry_b.pack()

    tk.Label(bhaskara_win, text="Coeficiente c:").pack()
    entry_c = tk.Entry(bhaskara_win)
    entry_c.pack()

    resultado_label = tk.Label(bhaskara_win, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=10)

    def calcular():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            delta = b**2 - 4*a*c

            if delta < 0:
                resultado_label.config(text="Não existem raízes reais")
            elif delta == 0:
                x = -b / (2*a)
                resultado_label.config(text=f"Uma raiz real: x = {x:.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                resultado_label.config(text=f"Duas raízes reais:\nx1 = {x1:.2f}, x2 = {x2:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos!")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero!")
    
    
    tk.Button(bhaskara_win, text="Calcular", command=calcular).pack(pady=10)