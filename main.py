# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Matheus Ferreira de Freitas, RA: 24123080-4
# Henrique

# Importando as bibliotecas necessárias
import tkinter as tk
import math
#import matplotlib.pyplot as plt

# Constantes

# Variaveis globais

# Primeira opção
L = 0 # Largura da caixa (escolher a unidade)
Ni = 0 # n inicial da partícula
Nf = 0 # n final da partícula
# Dados para probabilidade 
# P (a <= X <= b) = integral de f(x)dx de a até b
# Restringir valores de entrada de forma que estejam dentro do poço
a = 0 # Escolher a unidade
b = 0 # Escolher a unidade

# Segunda opção
A = 0 # Escolher a unidade
k = 0 # Escolher a unidade
Xp = 0 # Escolher a unidade

# Variaveis de controle

# Funções

# Testes
def funcao_1():
    global L, Ni, Nf, a, b
    # Criar labels e campos de entrada na janela principal
    label_valor1 = tk.Label(janela, text="Largura da caixa (L) em un:")
    label_valor1.pack()
    entrada_valor1 = tk.Entry(janela)
    entrada_valor1.pack()
    L = float(entrada_valor1.get())

    label_valor2 = tk.Label(janela, text="n inicial da particula (Ni):")
    label_valor2.pack()
    entrada_valor2 = tk.Entry(janela)
    entrada_valor2.pack()
    Ni = float(entrada_valor2.get())

    label_valor3 = tk.Label(janela, text="n final da particula (Nf):")
    label_valor3.pack()
    entrada_valor3 = tk.Entry(janela)
    entrada_valor3.pack()
    Nf = float(entrada_valor3.get())

    tk.Label(janela, text="P (a <= X <= b)").pack()

    label_valor4 = tk.Label(janela, text="a:")
    label_valor4.pack()
    entrada_valor4 = tk.Entry(janela)
    entrada_valor4.pack()
    a = float(entrada_valor4.get())

    label_valor5 = tk.Label(janela, text="b:")
    label_valor5.pack()
    entrada_valor5 = tk.Entry(janela)
    entrada_valor5.pack()
    b = float(entrada_valor5.get())


    # ... (Adicionar outros campos de entrada se necessário)

    # Função para obter e processar os valores digitados
    def processar_valores():
        valor1 = float(entrada_valor1.get())
        valor2 = float(entrada_valor2.get())

        # ... (Realizar cálculos ou operações com os valores)

    # Criar botão para acionar a função de processamento
    botao_processar = tk.Button(janela, text="Processar", command=processar_valores)
    botao_processar.pack()

def funcao_2():
    global L, Ni, Nf, a, b, A, k, Xp
    # Criar labels e campos de entrada na janela principal
    label_valor1 = tk.Label(janela, text="A em un:")
    label_valor1.pack()
    entrada_valor1 = tk.Entry(janela)
    entrada_valor1.pack()
    A = float(entrada_valor1.get())

    label_valor2 = tk.Label(janela, text="k em un:")
    label_valor2.pack()
    entrada_valor2 = tk.Entry(janela)
    entrada_valor2.pack()
    k = float(entrada_valor2.get())

    label_valor3 = tk.Label(janela, text="Xp em un:")
    label_valor3.pack()
    entrada_valor3 = tk.Entry(janela)
    entrada_valor3.pack()
    Xp = float(entrada_valor3.get())

    # ... (Adicionar outros campos de entrada se necessário)

    # Função para obter e processar os valores digitados
    def processar_valores():
        valor1 = float(entrada_valor1.get())
        valor2 = float(entrada_valor2.get())

        # ... (Realizar cálculos ou operações com os valores)

    # Criar botão para acionar a função de processamento
    botao_processar = tk.Button(janela, text="Processar", command=processar_valores)
    botao_processar.pack()

# Janelas

# Janela principal
janela = tk.Tk()
janela.title("Menu")
menu = tk.Menu(janela)
menu.add_command(label="Simulador", command=funcao_1)
menu.add_command(label="Caixa 1D", command=funcao_2)
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