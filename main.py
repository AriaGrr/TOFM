# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Matheus Ferreira de Freitas, RA: 24123080-4
# Henrique


#Arrumei Os Import :)
import tkinter as tk
import math
#import matplotlib
import os
# from math import sqrt, pi, sin
# import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Janela principal
janela = tk.Tk()
janela.title("Menu")

# Variáveis globais para os frames (para poder destruí-los depois) 
frame_entrada = None
frame_saida = None

# Constantes
hj = 6.626 * (10 ** -34)  # Constante de Planck em J.s
hev = 4.136 * (10 ** -15)  # Constante de Planck em eV.s
c = 3 * 10 ** 8  # Velocidade da luz no vácuo em m/s

# Variaveis globais

# Primeira opção
l = 0 # Largura da caixa (escolher a unidade)
ni = 0 # n inicial da partícula
nf = 0 # n final da partícula
n = 0 # 

# Dados para probabilidade 
# P (a <= X <= b) = integral de f(x)dx de a até b
# Restringir valores de entrada de forma que estejam dentro do poço
a = 0 # Escolher a unidade
b = 0 # Escolher a unidade

# Segunda opção
a = 0 # Escolher a unidade
k = 0 # Escolher a unidade
xp = 0 # Escolher a unidade

# Variaveis de controle
m = 0

# Funções

# Funções de controle
#Essa função aqui é a resposavel por Limpar os frames (destruir) pra você não ter uma função que usa o jutsu clone das sombras
def limpar_frames():
    global frame_entrada, frame_saida
    if frame_entrada:
        frame_entrada.destroy()
    if frame_saida:
        frame_saida.destroy()

# Funções de cálculo


# Funções de interface
def simulador():
    def processar_1():
        global L, Ni, Nf, a, b

        L = float(entrada_valor1.get())
        Ni = float(entrada_valor2.get())
        Nf = float(entrada_valor3.get())
        a = float(entrada_valor4.get())
        b = float(entrada_valor5.get())

        # Limpar a área de saída antes de exibir a nova saída
        text_area_saida.delete(1.0, tk.END)

        # Inserir a nova saída na área de texto
        text_area_saida.insert(tk.END, "Resultados:\n")
        # ... (Formatar e exibir os resultados dos cálculos)

    global frame_entrada, frame_saida
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)

    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    # COLOCAR UM TEXTO DE INTRODUÇÃO AQUI
    #
    # ~ Escrever a introdução ~
    #

    # COLOCAR UM OPTIONAL TEXT AQUI
    #
    # Texto: "Qual a particula que deseja analisar? "
    #
    # Próton
    # Eletron
    #

    # Criar labels e campos de entrada
    # Caixa = poço de potencial infinito
    label_valor1 = tk.Label(frame_entrada, text="Largura da caixa (L) em m:")
    label_valor1.grid(row=0, column=0)
    entrada_valor1 = tk.Entry(frame_entrada)
    entrada_valor1.grid(row=0, column=1)

    label_valor2 = tk.Label(frame_entrada, text="n inicial da particula (Ni):")
    label_valor2.grid(row=1, column=0)
    entrada_valor2 = tk.Entry(frame_entrada)
    entrada_valor2.grid(row=1, column=1)

    label_valor3 = tk.Label(frame_entrada, text="n final da particula (Nf):")
    label_valor3.grid(row=2, column=0)
    entrada_valor3 = tk.Entry(frame_entrada)
    entrada_valor3.grid(row=2, column=1)

    # COLOCAR OUTRO TEXTO AQUI
    # 
    # Dados para probabilidade
    # P (a <= X <= b) = integral de f(x)dx de a até b
    #

    # a = inicio do intervalo
    label_valor4 = tk.Label(frame_entrada, text="a:")
    label_valor4.grid(row=3, column=0)
    entrada_valor4 = tk.Entry(frame_entrada)
    entrada_valor4.grid(row=3, column=1)

    # b = fim do intervalo
    label_valor5 = tk.Label(frame_entrada, text="b:")
    label_valor5.grid(row=4, column=0)
    entrada_valor5 = tk.Entry(frame_entrada)
    entrada_valor5.grid(row=4, column=1)

    # Criar botão de submit
    botao_submit = tk.Button(frame_entrada, text="Processar", command=lambda: processar_1())
    botao_submit.grid(row=5, column=0, columnspan=2)

    # Criar frame para área de saída
    frame_saida = tk.Frame(janela)
    frame_saida.pack()

    # Criar área de texto para exibir a saída
    text_area_saida = tk.Text(frame_saida, width=50, height=10)
    text_area_saida.pack()


def caixa_1d():
    def processar_2():
            global A, k, Xp

            A = float(entrada_valor1.get())
            k = float(entrada_valor2.get())
            Xp = float(entrada_valor3.get())

            # ... (Realizar cálculos ou operações com os valores)

    global frame_entrada, frame_saida
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)
    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    # COLOCAR UM OPTIONAL TEXT AQUI
    #
    # Texto: "Qual a particula que deseja analisar? "
    #
    # Próton
    # Eletron
    #

    # Criar labels e campos de entrada
    label_valor1 = tk.Label(frame_entrada, text="A em m:")
    label_valor1.grid(row=0, column=0)
    entrada_valor1 = tk.Entry(frame_entrada)
    entrada_valor1.grid(row=0, column=1)

    label_valor2 = tk.Label(frame_entrada, text="k em m:")
    label_valor2.grid(row=1, column=0)
    entrada_valor2 = tk.Entry(frame_entrada)
    entrada_valor2.grid(row=1, column=1)

    label_valor3 = tk.Label(frame_entrada, text="Posição de x (que multiplique L):")
    label_valor3.grid(row=2, column=0)
    entrada_valor3 = tk.Entry(frame_entrada)
    entrada_valor3.grid(row=2, column=1)

    # Criar botão de submit
    botao_submit = tk.Button(frame_entrada, text="Processar", command=lambda: processar_2())
    botao_submit.grid(row=5, column=0, columnspan=2)

    # Criar frame para área de saída
    frame_saida = tk.Frame(janela)
    frame_saida.pack()

    # Criar área de texto para exibir a saída
    text_area_saida = tk.Text(frame_saida, width=50, height=10)
    text_area_saida.pack()

# Janela principal
menu = tk.Menu(janela)
menu.add_command(label="Simulador", command=simulador)
menu.add_command(label="Caixa 1D", command=caixa_1d)
menu.add_separator()  # Adiciona uma linha separadora
menu.add_command(label="Sair", command=janela.quit)

# # Janela secundária
# submenu = tk.Menu(menu, tearoff=0)
# submenu.add_command(label="Teste", command=teste3)
# submenu.add_command(label="Teste 1", command=lambda: print("Teste 1"))  # Função lambda simples
# submenu.add_command(label="Teste 2", command=lambda: print("Teste 2"))

# menu.add_cascade(label="Funções", menu=submenu)

janela.config(menu=menu)
janela.mainloop()