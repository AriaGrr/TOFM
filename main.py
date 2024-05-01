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
frame_option = None

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
A = 0 # em m
k = 0 # em m
xp = 0 # em m

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
    if frame_option:
        frame_option.destroy()

def m_option(opcao):
    global m
    if opcao == "1":
        m = 1.67 * (10 ** -27)  
    elif opcao == "2":
        m = 9.11 * (10 ** -31)

    # else:
    #     print("Opção inválida. Tente novamente.")


# def option():
#     global m
#     opcao_var = tk.StringVar(frame_option)
#     opcao_var.set("1")  # Valor padrão

#     opcoes = [("Próton", "1"),
#               ("Eletron", "2"),]

#     for texto, valor in opcoes:
#         radio_button = tk.Radiobutton(frame_entrada, text=texto, variable=opcao_var, value=valor)
#         radio_button.pack(anchor=tk.W)
    
#     button = tk.Button(frame_entrada, text="Selecionar", command=selecionar_opcao(opcao_var.get()))
#     button.pack()
#     print(m)

# Funções de cálculo


# Funções de interface
def simulador():
    global m
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
        text_area_saida.insert(tk.END, "Resultados:\n"
                                        "----------------\n" + str(m) + "\n"
                                        "Largura da caixa (L): " + str(L) + " m\n"
                                        "n inicial da partícula (Ni): " + str(Ni) + "\n"
                                        "n final da partícula (Nf): " + str(Nf) + "\n"
                                        "a: " + str(a) + "\n"
                                        "b: " + str(b) + "\n\n")
        # ... (Formatar e exibir os resultados dos cálculos)

    global frame_entrada, frame_saida, frame_option
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)
    # frame_option = tk.Frame(janela)
    # frame_option.pack()
    # opcao_var = tk.StringVar(frame_option)
    # opcoes = [("Próton", "1"),
    #            ("Eletron", "2")]
    # for texto, valor in opcoes:
    #      entrada_m = tk.Radiobutton(frame_option, text=texto, variable=opcao_var, value=valor)
    #      entrada_m.pack(anchor=tk.W)
    
    # opcao_var = tk.StringVar(frame_option)
    # opcao_var.set("1")  # Valor padrão

    # opcoes = [("Próton", "1"),
    #           ("Eletron", "2"),]

    # for texto, valor in opcoes:
    #     radio_button = tk.Radiobutton(frame_entrada, text=texto, variable=opcao_var, value=valor)
    #     radio_button.pack(anchor=tk.W)
    
    # button = tk.Button(frame_entrada, text="Selecionar", command=selecionar_opcao(opcao_var.get()))
    # button.pack()
    # print(m)

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

    # ARRUMAR AQUI
    # frame_option = tk.Frame(janela)
    # frame_option.pack()
    # opcao_var = tk.StringVar(frame_option)
    # rb_proton = tk.Radiobutton(frame_option, text="Próton", variable=opcao_var, value="1")
    # rb_eletron = tk.Radiobutton(frame_option, text="Eletron", variable=opcao_var, value="2")
    # rb_proton.grid(row=0, column=0, padx=10, pady=5)
    # rb_eletron.grid(row=1, column=0, padx=10, pady=5)

    # frame_entrada = tk.Frame(janela)
    # frame_entrada.pack()
    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    m_opcao = tk.StringVar(frame_entrada)
    m_opcao.set("1")

    rb_proton = tk.Radiobutton(frame_entrada, text="Próton", variable=m_opcao, value="1")

    rb_eletron = tk.Radiobutton(frame_entrada, text="Eletron", variable=m_opcao, value="2")

    rb_proton.grid(row=0, column=0, padx=10, pady=5)
    rb_eletron.grid(row=0, column=1, padx=10, pady=5)
    #

    # Criar labels e campos de entrada
    # Caixa = poço de potencial infinito
    label_l = tk.Label(frame_entrada, text="Largura da caixa (L) em m:")
    label_l.grid(row=0, column=0)
    entrada_l = tk.Entry(frame_entrada)
    entrada_l.grid(row=0, column=1)

    label_ni = tk.Label(frame_entrada, text="n inicial da particula (Ni):")
    label_ni.grid(row=1, column=0)
    entrada_ni = tk.Entry(frame_entrada)
    entrada_ni.grid(row=1, column=1)

    label_nf = tk.Label(frame_entrada, text="n final da particula (Nf):")
    label_nf.grid(row=2, column=0)
    entrada_nf = tk.Entry(frame_entrada)
    entrada_nf.grid(row=2, column=1)

    # COLOCAR OUTRO TEXTO AQUI
    # 
    # Dados para probabilidade
    # P (a <= X <= b) = integral de f(x)dx de a até b
    #

    # a = inicio do intervalo
    label_a = tk.Label(frame_entrada, text="a:")
    label_a.grid(row=3, column=0)
    entrada_a = tk.Entry(frame_entrada)
    entrada_a.grid(row=3, column=1)

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


    global frame_entrada, frame_saida, frame_option
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)
    # option()
    # opcao_var = tk.StringVar(frame_option)
    # opcao_var.set("1")  # Valor padrão

    # opcoes = [("Próton", "1"),
    #           ("Eletron", "2"),]

    # for texto, valor in opcoes:
    #     radio_button = tk.Radiobutton(frame_entrada, text=texto, variable=opcao_var, value=valor)
    #     radio_button.pack(anchor=tk.W)
    
    # button = tk.Button(frame_entrada, text="Selecionar", command=selecionar_opcao(opcao_var.get()))
    # button.pack()

    # frame_option = tk.Frame(janela)
    # frame_option.pack()

    # COLOCAR UM OPTIONAL TEXT AQUI
    #
    # Texto: "Qual a particula que deseja analisar? "
    #
    # Próton
    # Eletron
    #

    # ARRUMAR AQUI
    # frame_option = tk.Frame(janela)
    # frame_option.pack()

    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    m_opcao = tk.StringVar(frame_entrada)
    m_opcao.set("1")

    rb_proton = tk.Radiobutton(frame_entrada, text="Próton", variable=m_opcao, value="1")

    rb_eletron = tk.Radiobutton(frame_entrada, text="Eletron", variable=m_opcao, value="2")

    rb_proton.grid(row=0, column=0, padx=10, pady=5)
    rb_eletron.grid(row=0, column=1, padx=10, pady=5)

    #

    # for texto, valor in opcoes:
    #      entrada_m = tk.Radiobutton(frame_option, text=texto, variable=opcao_var, value=valor)
    #      entrada_m.pack(anchor=tk.W)
    # opcao_var.set("1")  # Valor padrão

    # entrada_m = tk.Radiobutton(frame_option, text="Próton", variable=opcao_var, value="1")
    # entrada_m.pack(anchor=tk.W)
    # entrada_m = tk.Radiobutton(frame_option, text="Elétron", variable=opcao_var, value="2")
    # entrada_m.pack(anchor=tk.W)


    label_a = tk.Label(frame_entrada, text="A em m:")
    label_a.grid(row=2, column=0)
    entrada_a = tk.Entry(frame_entrada)
    entrada_a.grid(row=2, column=1)

    label_k = tk.Label(frame_entrada, text="k em m:")
    label_k.grid(row=3, column=0)
    entrada_k = tk.Entry(frame_entrada)
    entrada_k.grid(row=3, column=1)

    label_xp = tk.Label(frame_entrada, text="Posição de x (que multiplique L):")
    label_xp.grid(row=4, column=0)
    entrada_xp = tk.Entry(frame_entrada)
    entrada_xp.grid(row=4, column=1)

    # Criar botão de submit
    botao_submit = tk.Button(frame_entrada, text="Processar", command=lambda: processar_2())
    botao_submit.grid(row=5, column=0, columnspan=2)

    # Criar frame para área de saída
    frame_saida = tk.Frame(janela)
    frame_saida.pack()

    # Criar área de texto para exibir a saída
    text_area_saida = tk.Text(frame_saida, width=50, height=10)
    text_area_saida.pack()
    def processar_2():
        global a, k, xp, l, m, n

        # Arrumar isso aqui
        print(m)
        x = m_opcao.get
        m = m_option(x)
        print(m)
        #
        a = float(entrada_a.get())
        k = float(entrada_k.get())
        xp = float(entrada_xp.get())

        # Limpar a área de saída antes de exibir a nova saída
        text_area_saida.delete(1.0, tk.END)

        # Inserir a nova saída na área de texto
        text_area_saida.insert(tk.END, "Entradas:\n"
                                        "----------------\n" + str(m) + "\n"
                                        "A: " + str(a) + "\n"
                                        "k: " + str(k) + "\n"
                                        "Posição de x (que multiplique L): " + str(xp) + "\n\n"
                                        "----------------\n"
                                        "Resultados:\n"
                                        "----------------\n")
        # ... (Realizar cálculos ou operações com os valores)

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