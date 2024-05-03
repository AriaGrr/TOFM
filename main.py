
# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5;
# Matheus Ferreira de Freitas, RA: 24123080-4;
# Henrique Hodel Babler, RA: 24123079-6

import os
import tkinter as tk
from scipy.integrate import quad
from math import sqrt, pi, sin
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
num = 0  # Número 
num_c = 0  # Número convertido 1
num_c2 = 0  # Número convertido 2

# Configuração inicial: Janela principal e declaração de variáveis e constantes
janela = tk.Tk()
janela.title("Menu")
frame_entrada = None
frame_saida = None

########################################Funções de Calculo########################################
# Reagrupamento das funções de cálculo
class QuantumCalculations:
    def __init__(self, m, l=0, ni=0, nf=0, hev=4.136e-15, hj=6.626e-34):
        self.m = m       # Massa da partícula
        self.l = l       # Largura da caixa
        self.ni = ni     # Nível quântico inicial
        self.nf = nf     # Nível quântico final
        self.hev = hev   # Constante de Planck em eV.s
        self.hj = hj     # Constante de Planck em J.s

    def update_parameters(self, l, ni, nf):
        """Atualiza os parâmetros da caixa quântica."""
        self.l = l
        self.ni = ni
        self.nf = nf

    def ei_j(self):
        """Calcular energia inicial em joules."""
        return self.ni ** 2 * (self.hj ** 2) / (8 * self.m * self.l ** 2)

    def ef_j(self):
        """Calcular energia final em joules."""
        return self.nf ** 2 * (self.hj ** 2) / (8 * self.m * self.l ** 2)

    def ei_ev(self):
        """Calcular energia inicial em eV."""
        return self.ei_j() / 1.602e-19

    def ef_ev(self):
        """Calcular energia final em eV."""
        return self.ef_j() / 1.602e-19

    def e_f(self):
        """Calcular energia do fóton em eV."""
        return abs(self.ef_ev() - self.ei_ev())

    def lamb(self):
        """Calcular comprimento de onda do fóton."""
        return (self.hev * 3e8) / self.e_f()

    def freq(self):
        """Calcular frequência do fóton."""
        return self.e_f() / self.hev

    def vi(self):
        """Calcular velocidade inicial da partícula."""
        return sqrt((2 * self.ei_j()) / self.m)

    def vf(self):
        """Calcular velocidade final da partícula."""
        return sqrt((2 * self.ef_j()) / self.m)

    def ci(self):
        """Calcular comprimento de onda inicial de De Broglie."""
        return 2 * self.l / self.ni

    def cf(self):
        """Calcular comprimento de onda final de De Broglie."""
        return 2 * self.l / self.nf

    def ki(self):
        """Calcular número de onda inicial."""
        return self.ni * pi / self.l

    def kf(self):
        """Calcular número de onda final."""
        return self.nf * pi / self.l
    def lamb(self):
        """Calcular comprimento de onda do fóton."""
        energia_foton = self.e_f()
        if energia_foton == 0:
            return "Indefinido"  # Pode retornar None ou algum valor especial que indique o problema
        return (self.hev * 3e8) / energia_foton
        

########################################Funções de Conversão########################################
#Funções de Conversão reorganizadas
# Todos os conversores vão para uma unidade padrão e depois convertem para a unidade desejada

class UnitConverter:
    def __init__(self):
        pass  

    def eV_J(self, num):
        """Converter electron-volt para joules."""
        return num * 1.6022e-19

    def J_eV(self, num):
        """Converter joules para electron-volt."""
        return num * 6.242e+18

    def eV_cal(self, num):
        """Converter electron-volt para calorias."""
        return num * 2.3900573613767 * 10**20

    def cal_eV(self, num):
        """Converter calorias para electron-volt."""
        return num / 2.3900573613767 * 10**20

    def eV_kcal(self, num):
        """Converter electron-volt para quilocalorias."""
        return num * 2.3900573613767 * 10**17

    def kcal_eV(self, num):
        """Converter quilocalorias para electron-volt."""
        return num / 2.3900573613767 * 10**17

    def eV_Btu(self, num):
        """Converter electron-volt para British Thermal Units."""
        return num * 3.826733324 * 10**19

    def Btu_eV(self, num):
        """Converter British Thermal Units para electron-volt."""
        return num / 3.826733324 * 10**19

    def eV_kWh(self, num):
        """Converter electron-volt para kilowatt-hours."""
        return num * 2.7777777777778 * 10**-7

    def kWh_eV(self, num):
        """Converter kilowatt-hours para electron-volt."""
        return num / 2.7777777777778 * 10**-7

    def eV_Wh(self, num):
        """Converter electron-volt para watt-hours."""
        return num * 3.6 * 10**-6

    def Wh_eV(self, num):
        """Converter watt-hours para electron-volt."""
        return num / 3.6 * 10**-6

    def metros_nm(self, num):
        """Converter metros para nanômetros."""
        return num * 1e9

    def nm_metros(self, num):
        """Converter nanômetros para metros."""
        return num / 1e9

    def metros_cm(self, num):
        """Converter metros para centímetros."""
        return num * 100

    def cm_metros(self, num):
        """Converter centímetros para metros."""
        return num / 100

    def metros_km(self, num):
        """Converter metros para quilômetros."""
        return num / 1000

    def km_metros(self, num):
        """Converter quilômetros para metros."""
        return num * 1000

    def metros_mm(self, num):
        """Converter metros para milímetros."""
        return num * 1000

    def mm_metros(self, num):
        """Converter milímetros para metros."""
        return num / 1000

    def metros_um(self, num):
        """Converter metros para micrômetros."""
        return num * 1e6

    def um_metros(self, num):
        """Converter micrômetros para metros."""
        return num / 1e6

    def metros_pm(self, num):
        """Converter metros para picômetros."""
        return num * 1e12

    def pm_metros(self, num):
        """Converter picômetros para metros."""
        return num / 1e12

    def Hz_kHz(self, num):
        """Converter Hertz para kilohertz."""
        return num / 1e3

    def kHz_Hz(self, num):
        """Converter kilohertz para Hertz."""
        return num * 1e3

    def Hz_MHz(self, num):
        """Converter Hertz para megahertz."""
        return num / 1e6

    def MHz_Hz(self, num):
        """Converter megahertz para Hertz."""
        return num * 1e6

    def Hz_GHz(self, num):
        """Converter Hertz para gigahertz."""
        return num / 1e9

    def GHz_Hz(self, num):
        """Converter gigahertz para Hertz."""
        return num * 1e9

    def Hz_THz(self, num):
        """Converter Hertz para terahertz."""
        return num / 1e12

    def THz_Hz(self, num):
        """Converter terahertz para Hertz."""
        return num * 1e12
    
########################################Funções Gerais########################################

#Agrupamento de Utilidades:

class InterfaceUtils:
    def __init__(self, frame_entrada=None, frame_saida=None, massa=None):
        self.frame_entrada = frame_entrada
        self.frame_saida = frame_saida
        self.massa = massa

    def limpar_frames(self):
        """Destruir os frames de entrada e saída, se existirem."""
        if self.frame_entrada:
            self.frame_entrada.destroy()
            self.frame_entrada = None
        if self.frame_saida:
            self.frame_saida.destroy()
            self.frame_saida = None

    def definir_massa(self, opcao):
        """Definir a massa da partícula com base na opção escolhida."""
        if opcao == "1":
            self.massa = 1.67e-27  # massa do próton
        elif opcao == "2":
            self.massa = 9.11e-31  # massa do elétron
        else:
            print("Opção inválida. Tente novamente.")

    def labels_and_entries(self, parent):
        """Criar labels e entradas para configurar os parâmetros da partícula e probabilidade."""
        global entrada_l, entrada_ni, entrada_nf, entrada_a, entrada_b
        entrada_l = tk.Entry(parent)
        tk.Label(parent, text="Largura da caixa (L) em m:").grid(row=3, column=0)
        entrada_l.grid(row=3, column=1)

        entrada_ni = tk.Entry(parent)
        tk.Label(parent, text="n inicial da partícula (Ni):").grid(row=4, column=0)
        entrada_ni.grid(row=4, column=1)

        entrada_nf = tk.Entry(parent)
        tk.Label(parent, text="n final da partícula (Nf):").grid(row=5, column=0)
        entrada_nf.grid(row=5, column=1)

        tk.Label(parent, text="Dados para probabilidade:\n P(a <= x <= b)").grid(row=6, column=1)

        entrada_a = tk.Entry(parent)
        tk.Label(parent, text="a:").grid(row=7, column=0)
        entrada_a.grid(row=7, column=1)

        entrada_b = tk.Entry(parent)
        tk.Label(parent, text="b:").grid(row=8, column=0)
        entrada_b.grid(row=8, column=1)



########################################Funções de Interface########################################

#Reeorganização e reestruturação da função simulador
class Simulator:
    def __init__(self, massa=1.67e-27):
        self.massa = massa
        self.simulador = tk.Tk()
        self.simulador.title("Simulador")
        self.quantum_calcs = QuantumCalculations(m=massa)
        self.setup_interface()

    def setup_interface(self):
        self.frame_entrada = tk.Frame(self.simulador)
        self.frame_entrada.pack()

        tk.Label(self.frame_entrada, text="Introdução\n").grid(row=0, column=1)
        self.m_opcao = tk.StringVar(self.frame_entrada, "1")
        self.m_opcao.trace("w", lambda *args: self.definir_massa(self.m_opcao.get()))
        tk.Radiobutton(self.frame_entrada, text="Próton", variable=self.m_opcao, value="1").grid(row=2, column=0)
        tk.Radiobutton(self.frame_entrada, text="Elétron", variable=self.m_opcao, value="2").grid(row=2, column=1)
        self.labels_and_entries(self.frame_entrada)
        tk.Button(self.frame_entrada, text="Processar", command=self.processar).grid(row=9, column=0, columnspan=2)
        self.frame_saida = tk.Frame(self.simulador)
        self.frame_saida.pack()
        self.text_area_saida = tk.Text(self.frame_saida, width=50, height=10)
        self.text_area_saida.pack()

    def processar(self):
        try:
            l = float(entrada_l.get())
            ni = float(entrada_ni.get())
            nf = float(entrada_nf.get())
            if ni == nf:
                self.text_area_saida.delete(1.0, tk.END)
                self.text_area_saida.insert(tk.END, "Níveis quânticos inicial e final são iguais; sem transição de energia.")
                return
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            self.quantum_calcs.update_parameters(l, ni, nf)
            eij = self.quantum_calcs.ei_j()
            efj = self.quantum_calcs.ef_j()
            efoton = self.quantum_calcs.e_f()
            freq = self.quantum_calcs.freq()
            lambda_foton = self.quantum_calcs.lamb()
            vi = self.quantum_calcs.vi()
            vf = self.quantum_calcs.vf()
            ci = self.quantum_calcs.ci()
            cf = self.quantum_calcs.cf()
            self.text_area_saida.delete(1.0, tk.END)
            self.text_area_saida.insert(tk.END, f"Energia Inicial (J): {eij:.4e}\nEnergia Final (J): {efj:.4e}\nEnergia do Fóton (eV): {efoton:.4e}\nFrequência do Fóton (Hz): {freq:.4e}\nComprimento de Onda do Fóton (m): {lambda_foton}\nVelocidade Inicial (m/s): {vi:.4e}\nVelocidade Final (m/s): {vf:.4e}\nComprimento de Onda de De Broglie Inicial (m): {ci:.4e}\nComprimento de Onda de De Broglie Final (m): {cf:.4e}")

        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.")

    def definir_massa(self, opcao):
        if opcao == "1":
            self.massa = 1.67e-27  # massa do próton
        elif opcao == "2":
            self.massa = 9.11e-31  # massa do elétron
        else:
            messagebox.showerror("Erro", "Opção inválida. Tente novamente.")

    def labels_and_entries(self, parent):
        global entrada_l, entrada_ni, entrada_nf, entrada_a, entrada_b
        entrada_l = tk.Entry(parent)
        entrada_ni = tk.Entry(parent)
        entrada_nf = tk.Entry(parent)
        entrada_a = tk.Entry(parent)
        entrada_b = tk.Entry(parent)
        tk.Label(parent, text="Largura da caixa (L) em m:").grid(row=3, column=0)
        entrada_l.grid(row=3, column=1)
        tk.Label(parent, text="n inicial da partícula (Ni):").grid(row=4, column=0)
        entrada_ni.grid(row=4, column=1)
        tk.Label(parent, text="n final da partícula (Nf):").grid(row=5, column=0)
        entrada_nf.grid(row=5, column=1)
        tk.Label(parent, text="a:").grid(row=6, column=0)
        entrada_a.grid(row=6, column=1)
        tk.Label(parent, text="b:").grid(row=7, column=0)
        entrada_b.grid(row=7, column=1)

    def run(self):
        self.simulador.mainloop()

#Nova função da caixa quantica
class QuantumBoxSimulator:
    def __init__(self):
        self.massa = 1.67e-27  # Massa inicialmente definida para próton
        self.setup_gui()

    def setup_gui(self):
        self.caixa = tk.Tk()
        self.caixa.title("Simulador de Caixa Quântica")

        self.frame_entrada = tk.Frame(self.caixa)
        self.frame_entrada.pack()

        tk.Label(self.frame_entrada, text="Função de onda (no SI) de uma partícula confinada em um poço de potencial infinito unidimensional é dada por:").grid(row=0, column=0, columnspan=2)
        tk.Label(self.frame_entrada, text="ψ(x) = A sin (k * x)").grid(row=1, column=0, columnspan=2)

        self.m_opcao = tk.StringVar(value="1")
        self.m_opcao.trace("w", lambda *args: self.definir_massa(self.m_opcao.get()))
        tk.Radiobutton(self.frame_entrada, text="Próton", variable=self.m_opcao, value="1").grid(row=2, column=0, padx=10, pady=5)
        tk.Radiobutton(self.frame_entrada, text="Elétron", variable=self.m_opcao, value="2").grid(row=2, column=1, padx=10, pady=5)

        self.entrada_a = tk.Entry(self.frame_entrada)
        tk.Label(self.frame_entrada, text="A em m:").grid(row=3, column=0)
        self.entrada_a.grid(row=3, column=1)

        self.entrada_k = tk.Entry(self.frame_entrada)
        tk.Label(self.frame_entrada, text="k em m:").grid(row=4, column=0)
        self.entrada_k.grid(row=4, column=1)

        self.entrada_xp = tk.Entry(self.frame_entrada)
        tk.Label(self.frame_entrada, text="Posição de x (que multiplique L):").grid(row=5, column=0)
        self.entrada_xp.grid(row=5, column=1)

        tk.Button(self.frame_entrada, text="Processar", command=self.processar).grid(row=6, column=0, columnspan=2)

        self.frame_saida = tk.Frame(self.caixa)
        self.frame_saida.pack()
        self.text_area_saida = tk.Text(self.frame_saida, width=50, height=10)
        self.text_area_saida.pack()

        self.caixa.mainloop()

    def definir_massa(self, opcao):
        if opcao == "1":
            self.massa = 1.67e-27
        elif opcao == "2":
            self.massa = 9.11e-31
        else:
            messagebox.showerror("Erro", "Opção inválida. Tente novamente.")

    def processar(self):
        try:
            a = float(self.entrada_a.get())
            k = float(self.entrada_k.get())
            xp = float(self.entrada_xp.get())

            l = self.l_func(a)  # Modifique conforme a lógica correta para calcular l
            n = self.n_func(k, l)
            p = self.probabilidade_2(n, xp, l)

            self.text_area_saida.delete(1.0, tk.END)
            self.text_area_saida.insert(tk.END, f"Entradas:\n----------------\nMassa: {self.massa} kg\nA: {a} m\nk: {k} m^-1\nPosição de x: {xp}\n----------------\nResultados:\n----------------\nLargura da caixa: {l:.4e} m\nNúmero quântico da partícula: {n}\nProbabilidade de encontrar a partícula na posição {xp}: {p:.3f}\n")
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.")

    def l_func(self, a):
       
        return a 

    def n_func(self, k, l):
        
        return int(k * l / np.pi) 

    def probabilidade_2(self, n, xp, l):
        
        return np.sin(n * np.pi * xp / l)**2  


########################################Funções de Conversão Reestruradas########################################
#Reogranização dos conversores

class UnitConverterApp:
    def __init__(self):
        self.conversor = tk.Tk()
        self.conversor.title("Unit Converter")
        self.setup_ui()
        self.conversor.mainloop()

    def setup_ui(self):
        self.container = tk.Frame(self.conversor)
        self.container.pack()

        # Create dropdowns for unit selection
        self.selected_1 = tk.StringVar()
        self.selected_2 = tk.StringVar()
        self.setup_dropdowns()

        # Input field for number
        self.entry = tk.Entry(self.container)
        self.entry.pack(side=tk.LEFT)

        # Button to trigger conversion
        convert_button = tk.Button(self.container, text="Converter", command=self.convert_value)
        convert_button.pack(side=tk.LEFT)

        # Output text area
        self.text_area_saida = tk.Text(self.conversor, width=50, height=2)
        self.text_area_saida.pack()

    def setup_dropdowns(self):
        # Define options for different units
        self.option_entry = ["m", "cm", "nm", "km", "mm", "um", "pm", "eV", "J", "cal", "kcal", "BTU", "kWh", "Wh", "Hz", "kHz", "MHz", "GHz", "THz", "rad", "deg"]
        self.option_out = self.option_entry[:]  # Same options for output

        # Setup dropdowns for input and output unit selection
        description_1 = tk.Label(self.container, text="Unidade de Entrada")
        description_1.pack(side=tk.LEFT)
        dropdown1 = tk.OptionMenu(self.container, self.selected_1, *self.option_entry)
        dropdown1.pack(side=tk.LEFT)

        description_2 = tk.Label(self.container, text="Unidade de Saída")
        description_2.pack(side=tk.LEFT)
        dropdown2 = tk.OptionMenu(self.container, self.selected_2, *self.option_out)
        dropdown2.pack(side=tk.LEFT)

    def convert_value(self):
        # Fetch selected units and input value
        entrada = self.selected_1.get()
        saida = self.selected_2.get()
        try:
            num = float(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
            return

        # Conversion logic
        num_c = self.apply_conversion(entrada, num)
        num_c2 = self.apply_conversion(saida, num_c, reverse=True)

        # Display the result
        self.text_area_saida.delete(1.0, tk.END)
        self.text_area_saida.insert(tk.END, f"Entrada: {num} {entrada}\nSaida: {num_c2} {saida}\n")

    def apply_conversion(self, unit, value, reverse=False):
        # Conversion functions based on selected unit
        if unit in ['m', 'J', 'Hz', 'deg']:
            conversion_factor = 1
        elif unit in ['cm', 'kHz']:
            conversion_factor = 1e3
        elif unit == 'nm':
            conversion_factor = 1e9
        elif unit == 'km':
            conversion_factor = 1e-3
        elif unit == 'mm':
            conversion_factor = 1e3
        elif unit == 'um':
            conversion_factor = 1e6
        elif unit == 'pm':
            conversion_factor = 1e12
        elif unit == 'eV':
            conversion_factor = 1 / 1.60218e-19
        elif unit == 'cal':
            conversion_factor = 1 / 4.184
        elif unit == 'kcal':
            conversion_factor = 1 / 4184
        elif unit == 'BTU':
            conversion_factor = 1 / 1055
        elif unit == 'kWh':
            conversion_factor = 1 / 3600000
        elif unit == 'Wh':
            conversion_factor = 1 / 3600
        elif unit == 'MHz':
            conversion_factor = 1e6
        elif unit == 'GHz':
            conversion_factor = 1e9
        elif unit == 'THz':
            conversion_factor = 1e12
        elif unit == 'rad':
            conversion_factor = 180 / pi

        if reverse:
            return value / conversion_factor
        return value * conversion_factor

########################################Funções de Animação e Plotagem########################################

def animate_wave_function(massa, l, ni, nf):
    fig, ax = plt.subplots()
    x = np.linspace(0, l, 300)
    lines = []
    for n in range(ni, nf + 1):
        line, = ax.plot(x, np.sin(n * np.pi * x / l), label=f'n={n}')
        lines.append(line)
    ax.set_xlim(0, l)
    ax.set_ylim(-1.2, 1.2)
    ax.legend()

    def update(frame):
        for i, line in enumerate(lines):
            n = ni + i
            line.set_ydata(np.sin(n * np.pi * (x + frame / 20) / l))
        return lines

    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.show()

def show_quantum_jumps():
    fig, ax = plt.subplots()
    energy_levels = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
    ax.set_ylim(-0.05, 0.45)
    ax.set_xlim(0, 5)
    ax.set_ylabel('Energia (eV)')
    ax.set_xlabel('Tempo (s)')
    ax.set_title('Simulação de Saltos Quânticos com Emissão de Fótons')
    for level in energy_levels:
        ax.hlines(level, 0, 5, colors='blue', linestyles='--')

    particle, = ax.plot([], [], 'ro', label='Partícula')
    photon, = ax.plot([], [], 'm-', linewidth=2, label='Fóton Emitido')
    ax.legend()

    def init():
        particle.set_data([], [])
        photon.set_data([], [])
        return particle, photon,

    def update(frame):
        current_level = energy_levels[frame % len(energy_levels)]
        particle.set_data(2.5, current_level)
        if frame > 0:
            previous_level = energy_levels[(frame - 1) % len(energy_levels)]
            photon.set_data([2.5, 2.5], [previous_level, current_level])
        else:
            photon.set_data([], [])
        return particle, photon,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 10), init_func=init, blit=True, interval=1000, repeat=True)

    window = tk.Toplevel()
    window.title("Animação de Saltos Quânticos")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


########################################Função Main########################################


def main():
    janela = tk.Tk()
    janela.title("Aplicação Principal")
    menu = tk.Menu(janela)

    submenu_simulador = tk.Menu(menu, tearoff=0)
    submenu_simulador.add_command(label="Abrir Simulador", command=Simulator)
    menu.add_cascade(label="Simulador", menu=submenu_simulador)

    submenu_caixa = tk.Menu(menu, tearoff=0)
    submenu_caixa.add_command(label="Abrir Caixa 1D", command=QuantumBoxSimulator)
    menu.add_cascade(label="Caixa 1D", menu=submenu_caixa)

    submenu_conversores = tk.Menu(menu, tearoff=0)
    submenu_conversores.add_command(label="Conversores", command=UnitConverterApp)
    menu.add_cascade(label="Conversores", menu=submenu_conversores)

    menu.add_command(label="Realizar Simulação de Onda", command=lambda: animate_wave_function(massa=9.11e-31, l=1e-9, ni=1, nf=3))
    menu.add_command(label="Simulação de Saltos Quânticos", command=show_quantum_jumps)

    menu.add_separator()
    menu.add_command(label="Sair", command=janela.quit)

    janela.config(menu=menu)
    janela.mainloop()

if __name__ == "__main__":
    main()
