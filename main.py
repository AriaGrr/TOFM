# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5;
# Matheus Ferreira de Freitas, RA: 24123080-4;
# Henrique Hodel Babler, RA: 24123079-6;

import os
import tkinter as tk
from scipy.integrate import quad
import random
from math import sqrt, pi, sin
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuração inicial: Janela principal e declaração de variáveis e constantes
janela = tk.Tk()
janela.title("Menu")

frame_entrada = None
frame_saida = None

# Variáveis Globais

# Constantes
hj = 6.626 * (10 ** -34)  # Constante de Planck em J.s
hev = 4.136 * (10 ** -15)  # Constante de Planck em eV.s
c = 3 * 10 ** 8  # Velocidade da luz no vácuo em m/s

l = 0  # Largura da caixa
ni = 0  # n inicial da partícula
nf = 0  # n final da partícula
n = 0 

# Probabilidade de encontrar a partícula entre a e b P(a <= x <= b) = 2/l * sin(n * pi * x / l) ** 2 (Integral)

a = 0  # Limite inferior para probabilidade
b = 0  # Limite superior para probabilidade
k = 0  # Número de onda em metros
xp = 0  # Posição x em metros

# Variável de controle de massa
m = 1.67 * (10 ** -27)  # Inicializando como próton

# Variaveis de controle de conversão
num = 0 # Número 
num_c = 0 # Número convertido 1
num_c2 = 0 # Número convertido 2

# Funções

# Funções para conversões
# Todos os conversores vão para uma unidade padrão e depois convertem para a unidade desejada

def eV_J(num): # Conversor de eV -> J
    num_c = num * 1.6022e-19
    return num_c

def J_eV(num): # Conversor de J -> eV
    num_c = num * 6.242e+18
    return num_c

def eV_cal(num): # Conversor de eV -> cal
    num_c = num * 2.3900573613767 * (10 ** 20)
    return num_c

def cal_eV(num): # Conversor de cal -> eV
    num_c = num / 2.3900573613767 * (10 ** 20)
    return num_c

def eV_kcal(num): # Conversor de eV -> kcal
    num_c = num * 2.3900573613767 * (10 ** 17)
    return num_c

def kcal_eV(num): # Conversor de kcal -> eV
    num_c = num / 2.3900573613767 * (10 ** 17)
    return num_c

def eV_Btu(num): # Conversor de eV -> BTU
    num_c = num * 3.826733324 * (10 ** 19)
    return num_c

def Btu_eV(num): # Conversor de BTU -> eV
    num_c = num / 3.826733324 * (10 ** 19)
    return num_c

def eV_kWh(num): # Conversor de eV -> kWh
    num_c = num * 2.7777777777778 * (10 ** -7)
    return num_c

def kWh_eV(num): # Conversor de kWh -> eV
    num_c = num / 2.7777777777778 * (10 ** -7)
    return num_c

def eV_Wh(num): # Conversor de eV -> Wh
    num_c = num * 3.6 * (10 ** -6)
    return num_c

def Wh_eV(num): # Conversor de Wh -> eV
    num_c = num / 3.6 * (10 ** -6)
    return num_c

def metros_nm(num): # Conversor de metros -> nm
    num_c = num * 1e9
    return num_c

def nm_metros(num): # Conversor de nm -> metros
    num_c = num / 1e9
    return num_c

def metros_cm(num): # Conversor de metros -> cm
    num_c = num * 100
    return num_c

def cm_metros(num): # Conversor de cm -> metros
    num_c = num / 100
    return num_c

def metros_km(num): # Conversor de metros -> km
    num_c = num / 1000
    return num_c

def km_metros(num): # Conversor de km -> metros
    num_c = num * 1000
    return num_c

def metros_mm(num): # Conversor de metros -> mm
    num_c = num * 1000
    return num_c

def mm_metros(num): # Conversor de mm -> metros
    num_c = num / 1000
    return num_c

def metros_um(num): # Conversor de metros -> um
    num_c = num * 1e6
    return num_c

def um_metros(num): # Conversor de um -> metros
    num_c = num / 1e6
    return num_c

def metros_pm(num): # Conversor de metros -> pm
    num_c = num * 1e12
    return num_c

def pm_metros(num): # Conversor de pm -> metros
    num_c = num / 1e12
    return num_c

def Hz_kHz(num): # Conversor de Hz -> kHz
    num_c = num / 1e3
    return num_c

def kHz_Hz(num): # Conversor de kHz -> Hz
    num_c = num * 1e3
    return num_c

def Hz_MHz(num): # Conversor de Hz -> MHz
    num_c = num / 1e6
    return num_c

def MHz_Hz(num): # Conversor de MHz -> Hz
    num_c = num * 1e6
    return num_c

def Hz_GHz(num): # Conversor de Hz -> GHz
    num_c = num / 1e9
    return num_c

def GHz_Hz(num): # Conversor de GHz -> Hz
    num_c = num * 1e9
    return num_c

def Hz_THz(num): # Conversor de Hz -> THz
    num_c = num / 1e12
    return num_c

def THz_Hz(num): # Conversor de THz -> Hz
    num_c = num * 1e12
    return num_c

def rad_to_deg(rad): # Conversor de radianos para graus
    return rad * 180 / pi

def deg_to_rad(deg): # Conversor de graus para radianos
    return deg * pi / 180

# Funções de cálculos

def ei_j(): # Função para calcular a energia inicial em J
    ei = ni ** 2 * (hj ** 2) / (8 * m * l ** 2)
    return ei

def ef_j(): # Função para calcular a energia final em J
    ef = nf ** 2 * (hj ** 2) / (8 * m * l ** 2)
    return ef

def e_f(): # Função para calcular energia do fóton
    efoton = abs(ef_ev() - ei_ev())
    return efoton

def ei_ev(): # Função para calcular a energia inicial em eV
    eij = ei_j() / (1.602 * (10 ** -19))
    return eij

def ef_ev(): # Função para calcular a energia final em eV
    efj = ef_j() / (1.602 * (10 ** -19))
    return efj

def lamb(): # Função para calcular o comprimento de onda
    lamb = (hev * 3 * (10 ** 8)) / e_f()
    return lamb

def freq(): # Função para calcular a frequência
    f = e_f() / hev
    return f

def calcular_vi(): # Função para calcular a velocidade inicial
    vi = sqrt((2 * ei_j()) / m)
    return vi

def calcular_vf(): # Função para calcular a velocidade final
    vf = sqrt((2 * ef_j()) / m)
    return vf

def calcular_ci(): # Função para calcular o comprimento de onda inicial
    ci = 2 * l / ni
    return ci

def calcular_cf(): # Função para calcular o comprimento de onda final
    cf = 2 * l / nf
    return cf

def calcular_ki(): # Função para calcular o número de onda inicial
    ki = ni * pi / l
    return ki

def calcular_kf(): # Função para calcular o número de onda final
    kf = nf * pi / l
    return kf

def l_func(): # Função para calcular a largura da caixa
    l = 2 / a ** 2
    return l

def n_func(): # Função para calcular o número de onda
    n = round((k * l) / pi)
    return n

def probabilidade(a, b, ni, l): # Função para calcular a probabilidade
    integrand = lambda x: 2 / l * sin((ni * pi * x) / l) ** 2
    result, _ = quad(integrand, a, b)
    return result

def probalidade_2(): # Função para calcular a probabilidade
    prob = 2 / l * (sin(n * pi * xp) ** 2)
    return prob

# Função para limpar frames
def limpar_frames():
    global frame_entrada, frame_saida
    if frame_entrada:
        frame_entrada.destroy()
    if frame_saida:
        frame_saida.destroy()

def m_option(opcao):
    global m
    if opcao == "1":
        m = 1.67 * (10 ** -27)  # massa do próton
    elif opcao == "2":
        m = 9.11 * (10 ** -31)  # massa do elétron
    else:
        print("Opção inválida. Tente novamente.")

def labels_and_entries(parent):
    global entrada_l, entrada_ni, entrada_nf, entrada_a, entrada_b
    entrada_l = tk.Entry(parent)

    tk.Label(parent, text="Largura da caixa (L) em m:").grid(row=3, column=0)
    entrada_l.grid(row=3, column=1)

    entrada_ni = tk.Entry(parent)
    tk.Label(parent, text="n inicial da particula (Ni):").grid(row=4, column=0)
    entrada_ni.grid(row=4, column=1)

    entrada_nf = tk.Entry(parent)
    tk.Label(parent, text="n final da particula (Nf):").grid(row=5, column=0)
    entrada_nf.grid(row=5, column=1)

    tk.Label(parent, text="Dados para probabilidade:\n P(a <= x <= b)").grid(row=6, column=1)

    entrada_a = tk.Entry(parent)
    tk.Label(parent, text="a:").grid(row=7, column=0)
    entrada_a.grid(row=7, column=1)

    entrada_b = tk.Entry(parent)
    tk.Label(parent, text="b:").grid(row=8, column=0)
    entrada_b.grid(row=8, column=1)

# Funções de interface

def simulador():
    global m
    def processar_1():
        global l, ni, nf, a, b, m
        try:
            l = float(entrada_l.get())
            ni = float(entrada_ni.get())
            nf = float(entrada_nf.get())
            a = float(entrada_a.get())
            b = float(entrada_b.get())

            eij = ei_j()
            eiev = ei_ev()
            efj = ef_j()
            efev = ef_ev()
            E = e_f()
            lam = lamb()
            f = freq()
            vi = calcular_vi()
            vf = calcular_vf()
            ci = calcular_ci()
            cf = calcular_cf()
            ki = calcular_ki()
            kf = calcular_kf()
            area = sqrt(2/l)
            i = probabilidade(a, b, ni, l)
            f = probabilidade(a, b, nf, l)

            text_area_saida.delete(1.0, tk.END)
            text_area_saida.insert(tk.END,
                                  f"Resultados:\n----------------\n"
                                  f"ψ{nf} (x) = {area:.4e} . sen({(kf):.4e}.x)\n"
                                  f"E{ni} = {eij:.4e} J ou {eiev:.4e} eV\n"
                                  f"E{nf} = {efj:.4e} J ou {efev:.4e} eV\n"
                                  f"Efoton = {E:.4e} eV\n"
                                  f"Comprimento de onda do fóton = {lam:.4e} m\n"
                                  f"Frequência do fóton = {f:.4e} Hz\n"
                                  f"Velocidade da partícula:\nn = {ni}: v = {vi:.4e} m/s\tn = {nf}: v = {vf:.4e} m/s\n"
                                  f"Comprimento de onda de De Broglie:\nn = {ni}: ƛ = {ci:.4e} m\tn = {nf}: ƛ = {cf:.4e} m\n"
                                  f"A probabilidade da partícula estar entre {a:.4e} e {b:.4e} no nível {ni} é de {i*100:.3f} %\n"
                                  f"A probabilidade da partícula estar entre {a:.4e} e {b:.4e} no nível {nf} é de {f*100:.3f} %\n")
            
            if m == 1.67 * (10 ** -27):
                tipo = "próton"
            elif m == 9.11 * (10 ** -31):
                tipo = "elétron"
            text_area_historico.insert(tk.END,f"----------------\nEntradas:\n----------------\n"
                                           f"Massa do {tipo}: {m} kg\n"
                                           f"Largura da caixa (L): {l} m\n"
                                           f"n inicial da partícula (Ni): {ni}\n"
                                           f"n final da partícula (Nf): {nf}\n"
                                           f"a: {a}\n"
                                           f"b: {b}\n"f"ψ{ni} (x) = {area:.4e} . sen({(ki):.4e}.x)\n"
                                           f"----------------\nResultados:\n----------------\n"
                                  f"ψ{nf} (x) = {area:.4e} . sen({(kf):.4e}.x)\n"
                                  f"E{ni} = {eij:.4e} J ou {eiev:.4e} eV\n"
                                  f"E{nf} = {efj:.4e} J ou {efev:.4e} eV\n"
                                  f"Efoton = {E:.4e} eV\n"
                                  f"Comprimento de onda do fóton = {lam:.4e} m\n"
                                  f"Frequência do fóton = {f:.4e} Hz\n"
                                  f"Velocidade da partícula:\nn = {ni}: v = {vi:.4e} m/s\tn = {nf}: v = {vf:.4e} m/s\n"
                                  f"Comprimento de onda de De Broglie:\nn = {ni}: ƛ = {ci:.4e} m\tn = {nf}: ƛ = {cf:.4e} m\n"
                                  f"A probabilidade da partícula estar entre {a:.4e} e {b:.4e} no nível {ni} é de {i*100:.3f} %\n"
                                  f"A probabilidade da partícula estar entre {a:.4e} e {b:.4e} no nível {nf} é de {f*100:.3f} %\n")
                        # plot_wave_functions(a, b, ni, nf, l)
            # plot_probability_distribution(a, b, ni, nf, l)
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.")

    def graficos():
        print("Gráficos")

    def simular():
        print("Simulação")

    m = 1.67 * (10 ** -27)

    simulador = tk.Tk()
    simulador.title("Simulador")

    frame_text = tk.Frame(simulador)
    frame_text.pack()

    label_text = tk.Label(frame_text, text="Para simular a quantização de energia de uma partícula confinada em uma caixa unidimensional, demonstrando o princípio quântico de confinamento, os usuários devem definir parâmetros como a largura da caixa e os estados quânticos inicial e final. A simulação então calcula e exibe as energias, funções de onda e probabilidades, além de gerar gráficos que ilustram esses conceitos,\n facilitando o entendimento visual dos processos quânticos estudados.\n\nDados de entrada:", wraplength=460, justify="center")
    label_text.pack()

    frame_entrada = tk.Frame(simulador)
    frame_entrada.pack()

    m_opcao = tk.StringVar(frame_entrada, "1")
    m_opcao.trace("w", lambda *args: m_option(m_opcao.get()))
    tk.Radiobutton(frame_entrada, text="Próton", variable=m_opcao, value="1").grid(row=2, column=0, padx=10, pady=6)
    tk.Radiobutton(frame_entrada, text="Elétron", variable=m_opcao, value="2").grid(row=2, column=1, padx=10, pady=5)
    labels_and_entries(frame_entrada)

    tk.Button(frame_entrada, text="Processar", command=processar_1).grid(row=9, column=1)

    tk.Button(frame_entrada, text="Gerar Gráficos", command=lambda: plot_wave_and_probability_functions(float(entrada_l.get()), int(entrada_ni.get()), int(entrada_nf.get()))).grid(row=9, column=0)

    tk.Button(frame_entrada, text="Simulação de Saltos Quânticos", command=lambda: show_quantum_jumps(int(entrada_ni.get()), int(entrada_nf.get()), float(entrada_l.get()))).grid(row=9, column=2)

    frame_saida = tk.Frame(simulador)
    frame_saida.pack()
    label_saida = tk.Label(frame_saida, text="Saída:")
    label_saida.pack()
    text_area_saida = tk.Text(frame_saida, width=60, height=20)
    text_area_saida.pack()

    frame_historico = tk.Frame(simulador)
    frame_historico.pack()
    label_historico = tk.Label(frame_historico, text="Historico:")
    label_historico.pack()
    text_area_historico = tk.Text(frame_historico, width=60, height=20)
    text_area_historico.pack()

    simulador.mainloop()

# Função para a caixa 1D

def caixa_1d():
    global m
    def processar_2():
        global a, k, xp, l, m, n
        try:
            a = float(entrada_a.get())
            k = float(entrada_k.get())
            xp = float(entrada_xp.get())

            l = l_func()
            n = n_func()
            p = probalidade_2()
            # prob = 2 / l * (sin(n * pi * xp) ** 2)
            text_area_saida.delete(1.0, tk.END)
            text_area_saida.insert(tk.END,"----------------\nResultados:\n----------------\n"
                                           f"Largura da caixa: {l:.4e} m\n"
                                           f"Número quântico da partícula: {n}\n"
                                           f"Probabilidade de encontrar a partícula na posição {xp}: {p:.3}\n")
            if m == 1.67 * (10 ** -27):
                tipo = "próton"
            elif m == 9.11 * (10 ** -31):
                tipo = "elétron"
            text_area_historico.insert(tk.END,f"----------------\nEntradas:\n----------------\n"
                                        f"Massa do {tipo}: {m} kg\n"
                                        f"A: {a}\n"
                                        f"K: {k}\n"
                                        f"Posição de x: {xp}\n"
                                        f"----------------\nResultados:\n----------------\n"
                                        f"Largura da caixa: {l:.4e} m\n"
                                        f"Número quântico da partícula: {n}\n"
                                        f"Probabilidade de encontrar a partícula na posição {xp}: {p:.3}\n")
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.")
    m = 1.67 * (10 ** -27)
    caixa = tk.Tk()
    caixa.title("Caixa 1D")

    frame_text = tk.Frame(caixa)
    frame_text.pack()

    label_text = tk.Label(frame_text, text="Função de onda (no SI) de uma partícula confinada em \num poço de potencial infinito unidimencional é dada por:\n\n" f"ψ(x) = A sin (k * x)\n\nDados de entrada:", wraplength=460, justify="center")
    label_text.pack()

    frame_entrada = tk.Frame(caixa)
    frame_entrada.pack()

    m_opcao = tk.StringVar(value="1")
    m_opcao.trace("w", lambda *args: m_option(m_opcao.get()))
    tk.Radiobutton(frame_entrada, text="Próton", variable=m_opcao, value="1").grid(row=1, column=0, padx=10, pady=5)
    tk.Radiobutton(frame_entrada, text="Elétron", variable=m_opcao, value="2").grid(row=1, column=1, padx=10, pady=5)
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
    botao_submit = tk.Button(frame_entrada, text="Processar", command=processar_2)
    botao_submit.grid(row=5, column=0, columnspan=2)
    frame_saida = tk.Frame(caixa)
    frame_saida.pack()
    label_saida = tk.Label(frame_saida, text="Saída:")
    label_saida.pack()
    text_area_saida = tk.Text(frame_saida, width=60, height=10)
    text_area_saida.pack()

    frame_historico = tk.Frame(caixa)
    frame_historico.pack()
    label_historico = tk.Label(frame_historico, text="Historico:")
    label_historico.pack()
    text_area_historico = tk.Text(frame_historico, width=60, height=10)
    text_area_historico.pack()

    caixa.mainloop()

# Conversores

# Conversor de unidades de comprimento
def conversor_1():
  global num, num_c, num_c2
  def convert_value():
    global num, num_c, num_c2
    
    entrada = selected_1.get()
    saida = selected_2.get()

    try:
      num = float(entry.get())
    except ValueError:
      print("Valor inválido. Digite um número.")
      return

    if entrada == 'm':
        num_c = num
    elif entrada == 'cm':
        num_c = cm_metros(num)
    elif entrada == 'nm':
        num_c = nm_metros(num)
    elif entrada == 'km':
        num_c = km_metros(num)
    elif entrada == 'mm':
        num_c = mm_metros(num)
    elif entrada == 'um':
        num_c = um_metros(num)
    elif entrada == 'pm':
        num_c = pm_metros(num)

    if saida == 'm':
        num_c2 = num_c
    elif saida == 'cm':
        num_c2 = metros_cm(num_c)
    elif saida == 'nm':
        num_c2 = metros_nm(num_c)
    elif saida == 'km':
        num_c2 = metros_km(num_c)
    elif saida == 'mm':
        num_c2 = metros_mm(num_c)
    elif saida == 'um':
        num_c2 = metros_um(num_c)
    elif saida == 'pm':
        num_c2 = metros_pm(num_c)

    text_area_saida.delete(1.0, tk.END)
    text_area_saida.insert(tk.END, f"{num_c2} {saida}\n")
    text_area_historico.insert(tk.END, f"----------------\n"
                                   f"Entrada: {num} {entrada}\n"
                                      f"Saida: {num_c2} {saida}\n")

  conversor = tk.Tk()
  conversor.title("m / cm / nm / km / mm / um / pm")

  def selected_option(entrada, saida):
    pass

  option_entry = ["m", "cm", "nm", "km", "mm", "um", "pm"]
  option_out = ["m", "cm", "nm", "km", "mm", "um", "pm"]

  container = tk.Frame(conversor)
  container.pack()

  selected_1 = tk.StringVar()
  selected_1.set(option_entry[0])

  selected_2 = tk.StringVar()
  selected_2.set(option_out[0])

  description_1 = tk.Label(container, text="Entrada")
  description_1.pack(side=tk.LEFT)

  dropdown1 = tk.OptionMenu(container, selected_1, *option_entry, command=selected_option)
  dropdown1.pack(side=tk.LEFT)

  description_2 = tk.Label(container, text="Saída")
  description_2.pack(side=tk.LEFT)

  dropdown2 = tk.OptionMenu(container, selected_2, *option_out, command=selected_option)
  dropdown2.pack(side=tk.LEFT)

  entry = tk.Entry(container)
  entry.pack(side=tk.LEFT)

  convert_button = tk.Button(container, text="Converter", command=convert_value)
  convert_button.pack(side=tk.LEFT)

  frame_saida = tk.Frame(conversor)
  frame_saida.pack()
  label_saida = tk.Label(frame_saida, text="Saída:")
  label_saida.pack()
  text_area_saida = tk.Text(frame_saida, width=40, height=1)
  text_area_saida.pack()

  frame_historico = tk.Frame(conversor)
  frame_historico.pack()
  label_historico = tk.Label(frame_historico, text="Historico:")
  label_historico.pack()
  text_area_historico = tk.Text(frame_historico, width=40, height=4)
  text_area_historico.pack()

  conversor.mainloop()

# Conversor de unidades de energia
def conversor_2():
  global num, num_c, num_c2
  def convert_2():
    global num, num_c, num_c2
    
    entrada = selected_1.get()
    saida = selected_2.get()

    try:
      num = float(entry.get())
    except ValueError:
      print("Valor inválido. Digite um número.")
      return

    if entrada == 'eV':
        num_c = num
    elif entrada == 'J':
        num_c = J_eV(num)
    elif entrada == 'cal':
        num_c = cal_eV(num)
    elif entrada == 'kcal':
        num_c = kcal_eV(num)
    elif entrada == 'BTU':
        num_c = Btu_eV(num)
    elif entrada == 'kWh':
        num_c = kWh_eV(num)
    elif entrada == 'Wh':
        num_c = Wh_eV(num)

    if saida == 'eV':
        num_c2 = num_c
    elif saida == 'J':
        num_c2 = eV_J(num_c)
    elif saida == 'cal':
        num_c2 = eV_cal(num_c)
    elif saida == 'kcal':
        num_c2 = eV_kcal(num_c)
    elif saida == 'BTU':
        num_c2 = eV_Btu(num_c)
    elif saida == 'kWh':
        num_c2 = eV_kWh(num_c)
    elif saida == 'Wh':
        num_c2 = eV_Wh(num_c)

    if num_c2:
        text_area_saida.delete(1.0, tk.END)
        text_area_saida.insert(tk.END,f"{num_c2} {saida}\n")
        text_area_historico.insert(tk.END, f"----------------\n"
                                   f"Entrada: {num} {entrada}\n"
                                      f"Saida: {num_c2} {saida}\n")

  conversor = tk.Tk()
  conversor.title("eV / J / cal / kcal / BTU / kWh / Wh")

  def selected_option(entrada, saida):
    pass

  option_entry = ["eV", "J", "cal", "kcal", "BTU", "kWh", "Wh"]
  option_out = ["eV", "J", "cal", "kcal", "BTU", "kWh", "Wh"]

  container = tk.Frame(conversor)
  container.pack()

  selected_1 = tk.StringVar()
  selected_1.set(option_entry[0])

  selected_2 = tk.StringVar()
  selected_2.set(option_out[0])

  description_1 = tk.Label(container, text="Entrada")
  description_1.pack(side=tk.LEFT)

  dropdown1 = tk.OptionMenu(container, selected_1, *option_entry, command=selected_option)
  dropdown1.pack(side=tk.LEFT)

  description_2 = tk.Label(container, text="Saída")
  description_2.pack(side=tk.LEFT)

  dropdown2 = tk.OptionMenu(container, selected_2, *option_out, command=selected_option)
  dropdown2.pack(side=tk.LEFT)

  entry = tk.Entry(container)
  entry.pack(side=tk.LEFT)

  convert_button = tk.Button(container, text="Converter", command=convert_2)
  convert_button.pack(side=tk.LEFT)

  frame_saida = tk.Frame(conversor)
  frame_saida.pack()
  label_saida = tk.Label(frame_saida, text="Saída:")
  label_saida.pack()
  text_area_saida = tk.Text(frame_saida, width=40, height=1)
  text_area_saida.pack()

  frame_historico = tk.Frame(conversor)
  frame_historico.pack()
  label_historico = tk.Label(frame_historico, text="Historico:")
  label_historico.pack()
  text_area_historico = tk.Text(frame_historico, width=40, height=4)
  text_area_historico.pack()

  conversor.mainloop()

# Conversor de unidades de frequência
def conversor_3():
  global num, num_c, num_c2
  def convert_3():
    global num, num_c, num_c2
    
    entrada = selected_1.get()
    saida = selected_2.get()

    try:
      num = float(entry.get())
    except ValueError:
      print("Valor inválido. Digite um número.")
      return

    if entrada == 'Hz':
        num_c = num
    elif entrada == 'kHz':
        num_c = kHz_Hz(num)
    elif entrada == 'MHz':
        num_c = MHz_Hz(num)
    elif entrada == 'GHz':
        num_c = GHz_Hz(num)
    elif entrada == 'THz':
        num_c = THz_Hz(num)
    # elif entrada == '':
    #     num_c = 
    # elif entrada == '':
    #     num_c = 
    # elif entrada == '':
    #     num_c = 

    if saida == 'Hz':
        num_c2 = num_c
    elif saida == 'kHz':
        num_c2 = Hz_kHz(num_c)
    elif saida == 'MHz':
        num_c2 = Hz_MHz(num_c)
    elif saida == 'GHz':
        num_c2 = Hz_GHz(num_c)
    elif saida == 'THz':
        num_c2 = Hz_THz(num_c)
    # elif saida == '':
    #     num_c2 = 
    # elif saida == '':
    #     num_c2 = 
    # elif saida == '':
    #     num_c2 = 

    # Display the converted value (if any)
    if num_c2:
        text_area_saida.delete(1.0, tk.END)
        text_area_saida.insert(tk.END, f"{num_c2} {saida}\n")
        text_area_historico.insert(tk.END, f"----------------\n"
                                   f"Entrada: {num} {entrada}\n"
                                      f"Saida: {num_c2} {saida}\n")

  conversor = tk.Tk()
  conversor.title("Hz / kHz / MHz / GHz / THzh")

  def selected_option(entrada, saida):
    pass

  option_entry = ["Hz", "kHz", "MHz", "GHz", "THz"]
  option_out = ["Hz", "kHz", "MHz", "GHz", "THz"]

  container = tk.Frame(conversor)
  container.pack()

  selected_1 = tk.StringVar()
  selected_1.set(option_entry[0])

  selected_2 = tk.StringVar()
  selected_2.set(option_out[0])

  description_1 = tk.Label(container, text="Entrada")
  description_1.pack(side=tk.LEFT)

  dropdown1 = tk.OptionMenu(container, selected_1, *option_entry, command=selected_option)
  dropdown1.pack(side=tk.LEFT)

  description_2 = tk.Label(container, text="Saída")
  description_2.pack(side=tk.LEFT)

  dropdown2 = tk.OptionMenu(container, selected_2, *option_out, command=selected_option)
  dropdown2.pack(side=tk.LEFT)

  entry = tk.Entry(container)
  entry.pack(side=tk.LEFT)

  convert_button = tk.Button(container, text="Converter", command=convert_3)
  convert_button.pack(side=tk.LEFT)

  frame_saida = tk.Frame(conversor)
  frame_saida.pack()
  label_saida = tk.Label(frame_saida, text="Saída:")
  label_saida.pack()
  text_area_saida = tk.Text(frame_saida, width=40, height=1)
  text_area_saida.pack()

  frame_historico = tk.Frame(conversor)
  frame_historico.pack()
  label_historico = tk.Label(frame_historico, text="Historico:")
  label_historico.pack()
  text_area_historico = tk.Text(frame_historico, width=40, height=4)
  text_area_historico.pack()

  conversor.mainloop()

# Conversor de unidades de ângulo
def conversor_4():
    global num, num_c, num_c2
    def convert_4():
        global num, num_c, num_c2

        num_c = 0
        num = 0

        entrada = selected_1.get()

        try:
            num = float(entry.get())
        except ValueError:
            print("Valor inválido. Digite um número.")
            return

        if entrada == 'rad':
            num_c = rad_to_deg(num)
            saida = 'deg'
        elif entrada == 'deg':
            num_c = deg_to_rad(num)
            saida = 'rad'

        if num_c:
            text_area_saida.delete(1.0, tk.END)
            text_area_saida.insert(tk.END, 
                                           f"{num_c} {saida}\n")
            text_area_historico.insert(tk.END, f"----------------\n"
                                                f"Entrada: {num} {entrada}\n"
                                                f"Saida: {num_c} {saida}\n")

    conversor = tk.Tk()
    conversor.title("rad / deg")

    def selected_option(entrada, saida):
        pass

    option_entry = ["rad", "deg"]

    container = tk.Frame(conversor)
    container.pack()

    selected_1 = tk.StringVar()
    selected_1.set(option_entry[0])

    description_1 = tk.Label(container, text="Entrada")
    description_1.pack(side=tk.LEFT)

    dropdown1 = tk.OptionMenu(container, selected_1, *option_entry, command=selected_option)
    dropdown1.pack(side=tk.LEFT)

    entry = tk.Entry(container)
    entry.pack(side=tk.LEFT)

    convert_button = tk.Button(container, text="Converter", command=convert_4)
    convert_button.pack(side=tk.LEFT)

    frame_saida = tk.Frame(conversor)
    frame_saida.pack()
    label_saida = tk.Label(frame_saida, text="Saída:")
    label_saida.pack()
    text_area_saida = tk.Text(frame_saida, width=40, height=1)
    text_area_saida.pack()

    frame_historico = tk.Frame(conversor)
    frame_historico.pack()
    label_historico = tk.Label(frame_historico, text="Historico:")
    label_historico.pack()
    text_area_historico = tk.Text(frame_historico, width=40, height=4)
    text_area_historico.pack()

    conversor.mainloop()

def conversor_geral():
    global num, num_c, num_c2
    def convertendo():
        print("Convertendo")
        global num, num_c, num_c2
        
        entrada = selected_1.get()
        saida = selected_2.get()

        try:
            num = float(entry.get())
        except ValueError:
            print("Valor inválido. Digite um número.")
            return
        
        if entrada == 'rad':
            num_c = rad_to_deg(num)
            saida = 'deg'
        elif entrada == 'deg':
            num_c = deg_to_rad(num)
            saida = 'rad'
        elif entrada == 'm':
            num_c = num
        elif entrada == 'cm':
            num_c = cm_metros(num)
        elif entrada == 'nm':
            num_c = nm_metros(num)
        elif entrada == 'km':
            num_c = km_metros(num)
        elif entrada == 'mm':
            num_c = mm_metros(num)
        elif entrada == 'um':
            num_c = um_metros(num)
        elif entrada == 'pm':
            num_c = pm_metros(num)
        elif entrada == 'eV':
            num_c = num
        elif entrada == 'J':
            num_c = J_eV(num)
        elif entrada == 'cal':
            num_c = cal_eV(num)
        elif entrada == 'kcal':
            num_c = kcal_eV(num)
        elif entrada == 'BTU':
            num_c = Btu_eV(num)
        elif entrada == 'kWh':
            num_c = kWh_eV(num)
        elif entrada == 'Wh':
            num_c = Wh_eV(num)
        elif entrada == 'Hz':
            num_c = num
        elif entrada == 'kHz':
            num_c = kHz_Hz(num)
        elif entrada == 'MHz':
            num_c = MHz_Hz(num)
        elif entrada == 'GHz':
            num_c = GHz_Hz(num)
        elif entrada == 'THz':
            num_c = THz_Hz(num)

        if saida == entrada:
            num_c2 = num_c

        if (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'cm':
            num_c2 = metros_cm(num_c)
        elif (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'nm':
            num_c2 = metros_nm(num_c)
        elif (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'km':
            num_c2 = metros_km(num_c)
        elif (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'mm':
            num_c2 = metros_mm(num_c)
        elif (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'um':
            num_c2 = metros_um(num_c)
        elif (entrada == 'm' or entrada == 'cm' or entrada == 'nm' or entrada == 'km' or entrada == 'mm' or entrada == 'um' or entrada == 'pm') and saida == 'pm':
            num_c2 = metros_pm(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'J':
            num_c2 = eV_J(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'cal':
            num_c2 = eV_cal(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'kcal':
            num_c2 = eV_kcal(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'BTU':
            num_c2 = eV_Btu(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'kWh':
            num_c2 = eV_kWh(num_c)
        elif (entrada == 'eV' or entrada == 'J' or entrada == 'cal' or entrada == 'kcal' or entrada == 'BTU' or entrada == 'kWh' or entrada == 'Wh') and saida == 'Wh':
            num_c2 = eV_Wh(num_c)
        elif (entrada == 'Hz' or entrada == 'kHz' or entrada == 'MHz' or entrada == 'GHz' or entrada == 'THz') and saida == 'kHz':
            num_c2 = Hz_kHz(num_c)
        elif (entrada == 'Hz' or entrada == 'kHz' or entrada == 'MHz' or entrada == 'GHz' or entrada == 'THz') and saida == 'MHz':
            num_c2 = Hz_MHz(num_c)
        elif (entrada == 'Hz' or entrada == 'kHz' or entrada == 'MHz' or entrada == 'GHz' or entrada == 'THz') and saida == 'GHz':
            num_c2 = Hz_GHz(num_c)
        elif (entrada == 'Hz' or entrada == 'kHz' or entrada == 'MHz' or entrada == 'GHz' or entrada == 'THz') and saida == 'THz':
            num_c2 = Hz_THz(num_c)
        elif entrada == 'rad' or entrada == 'deg':
            num_c2 = num_c
        else:
            num_c2 = num_c
            print("Erro de conversão")
        
        text_area_saida.delete(1.0, tk.END)
        text_area_saida.insert(tk.END, f"Entrada: {num} {entrada}\n"
                                        f"Saida: {num_c2} {saida}\n")
        text_area_historico.insert(tk.END, f"----------------\n"
                                        f"Entrada: {num} {entrada}\n"
                                        f"Saida: {num_c2} {saida}\n")

    conversor = tk.Tk()
    conversor.title("Conversores")

    def selected_option(entrada, saida):
        pass

    option_entry = ["rad", "deg", "m", "cm", "nm", "km", "mm", "um", "pm", "eV", "J", "cal", "kcal", "BTU", "kWh", "Wh", "Hz", "kHz", "MHz", "GHz", "THz"]
    option_out = ["rad", "deg", "m", "cm", "nm", "km", "mm", "um", "pm", "eV", "J", "cal", "kcal", "BTU", "kWh", "Wh", "Hz", "kHz", "MHz", "GHz", "THz"]

    container = tk.Frame(conversor)
    container.pack()

    selected_1 = tk.StringVar()
    selected_1.set(option_entry[0])

    selected_2 = tk.StringVar()
    selected_2.set(option_out[0])

    description_1 = tk.Label(container, text="Entrada")
    description_1.pack(side=tk.LEFT)

    dropdown1 = tk.OptionMenu(container, selected_1, *option_entry, command=selected_option)
    dropdown1.pack(side=tk.LEFT)

    description_2 = tk.Label(container, text="Saída")
    description_2.pack(side=tk.LEFT)

    dropdown2 = tk.OptionMenu(container, selected_2, *option_out, command=selected_option)
    dropdown2.pack(side=tk.LEFT)

    entry = tk.Entry(container)
    entry.pack(side=tk.LEFT)

    convert_button = tk.Button(container, text="Converter", command=convertendo)
    convert_button.pack(side=tk.LEFT)

    frame_saida = tk.Frame(conversor)
    frame_saida.pack()
    label_saida = tk.Label(frame_saida, text="Saída:")
    label_saida.pack()
    text_area_saida = tk.Text(frame_saida, width=40, height=1)
    text_area_saida.pack()

    frame_historico = tk.Frame(conversor)
    frame_historico.pack()
    label_historico = tk.Label(frame_historico, text="Historico:")
    label_historico.pack()
    text_area_historico = tk.Text(frame_historico, width=40, height=4)
    text_area_historico.pack()

    conversor.mainloop()

# Funções de simulação

def plot_wave_and_probability_functions(l, ni, nf):
    # Definindo o domínio x
    x = np.linspace(0, l, 400)
    
    # Funções de onda para os estados inicial e final
    psi_ni = np.sqrt(2/l) * np.sin(ni * np.pi * x / l)
    psi_nf = np.sqrt(2/l) * np.sin(nf * np.pi * x / l)
    
    # Calculando as distribuições de probabilidade
    probability_ni = psi_ni**2
    probability_nf = psi_nf**2

    # Criando uma figura com 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Plotando as funções de onda
    axes[0, 0].plot(x, psi_ni, label=f'ψ(x) para Ni = {ni}')
    axes[0, 0].set_title(f'Função de Onda para Ni = {ni}')
    axes[0, 0].set_xlabel('x (m)')
    axes[0, 0].set_ylabel('ψ(x)')
    axes[0, 0].legend()

    axes[0, 1].plot(x, psi_nf, label=f'ψ(x) para Nf = {nf}')
    axes[0, 1].set_title(f'Função de Onda para Nf = {nf}')
    axes[0, 1].set_xlabel('x (m)')
    axes[0, 1].set_ylabel('ψ(x)')
    axes[0, 1].legend()

    # Plotando e sombreando as distribuições de probabilidade
    axes[1, 0].plot(x, probability_ni, label=f'Distribuição de Probabilidade para Ni = {ni}')
    axes[1, 0].fill_between(x, probability_ni, alpha=0.3)  # Sombreamento
    axes[1, 0].set_title(f'Distribuição de Probabilidade para Ni = {ni}')
    axes[1, 0].set_xlabel('x (m)')
    axes[1, 0].set_ylabel('|\u03C8(x)|²')
    axes[1, 0].legend()

    axes[1, 1].plot(x, probability_nf, label=f'Distribuição de Probabilidade para Nf = {nf}')
    axes[1, 1].fill_between(x, probability_nf, alpha=0.3)  # Sombreamento
    axes[1, 1].set_title(f'Distribuição de Probabilidade para Nf = {nf}')
    axes[1, 1].set_xlabel('x (m)')
    axes[1, 1].set_ylabel('|\u03C8(x)|²')
    axes[1, 1].legend()

    # Organizando os gráficos e mostrando o resultado
    plt.tight_layout()
    plt.show()
    
def show_quantum_jumps(ni, nf, l):
    fig, ax = plt.subplots()
    
    energy_levels = np.array([-13.6, -3.4, -1.51, -0.85, -0.54])
    ax.set_ylim(-14, 0) 
    ax.set_xlim(0, l)
    ax.set_ylabel('Energia (eV)')
    ax.set_xlabel('x (nm)')
    ax.set_title('Simulação de Saltos Quânticos com Emissão e Absorção de Fótons')

    # Desenho das linhas representando os níveis de energia
    for level in energy_levels:
        ax.hlines(level, 0, l, colors='blue', linestyles='--')

    particle, = ax.plot([], [], 'ro', label='Partícula')
    photon, = ax.plot([], [], 'y-', linewidth=2, label='Fóton Emitido/Absorvido')
    ax.legend(loc='upper right')

    current_level = ni - 1 

    def init():
        particle.set_data([], [])
        photon.set_data([], [])
        return particle, photon,

    def update(frame):
        nonlocal current_level
        previous_level = current_level
        if frame == 1: 
            current_level = nf - 1
        elif frame > 5: 
            current_level = random.choice(range(len(energy_levels)))

        # Cálculo do valor de X para cada frame
        x_position = (frame / 60) * l

        particle.set_data(x_position, energy_levels[current_level])
        if current_level != previous_level: 
            photon.set_data([x_position, x_position], [energy_levels[previous_level], energy_levels[current_level]])
        else:
            photon.set_data([], [])
        return particle, photon,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 61), init_func=init, blit=True, interval=1000, repeat=True)

    window = tk.Toplevel()
    window.title("Animação de Saltos Quânticos")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Função principal
def main():
    menu = tk.Menu(janela)
 
    menu.add_command(label="Simulador", command=simulador)
    menu.add_command(label="Caixa 1D", command=caixa_1d)

    # Janelas de conversores
    submenu_conversores = tk.Menu(menu, tearoff=0)
    submenu_conversores.add_command(label="Conversor Geral", command=conversor_geral)
    submenu_conversores.add_command(label="m / cm / nm / km / mm / um / pm", command=conversor_1)
    submenu_conversores.add_command(label="eV / J / cal / kcal / BTU / kWh / Wh", command=conversor_2)  
    submenu_conversores.add_command(label="Hz / kHz / MHz / GHz / THz", command=conversor_3)
    submenu_conversores.add_command(label="rad / deg", command=conversor_4)
    menu.add_cascade(label="Conversores", menu=submenu_conversores)

    menu.add_separator()  # Adiciona uma linha separadora
    menu.add_command(label="Sair", command=janela.quit)
    janela.config(menu=menu)
    janela.mainloop()

main()
