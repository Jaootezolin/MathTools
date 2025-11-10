import tkinter as tk
from bhaskara import abrir_bhaskara
from pitagoras import abrir_pitagoras
from trigonometria import abrir_trigonometria
from reta import abrir_reta
from parabola import abrir_parabola
from megasena import abrir_megasena
root = tk.Tk()
root.title("Projeto de Calculadoras")
root.geometry("400x500")
titulo = tk.Label(root, text="Menu Principal", font=("Arial", 18, "bold"))
titulo.pack(pady=20)
botoes = [
    ("Calculadora de Bhaskara", abrir_bhaskara),
    ("Teorema de Pitágoras", abrir_pitagoras),
    ("Trigonometria", abrir_trigonometria),
    ("Reta no Plano Cartesiano", abrir_reta),
    ("Parábola", abrir_parabola),
    ("Simulador da Mega-Sena", abrir_megasena)
]
for texto, comando in botoes:
    btn = tk.Button(root, text=texto, width=35, height=2, command=comando)
    btn.pack(pady=5)
root.mainloop()