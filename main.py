# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Matheus Ferreira de Freitas, RA: 24123080-4
# Henrique

# Importando as bibliotecas necessárias
import tkinter as tk
import math
#import matplotlib.pyplot as plt


# Variaveis globais

# Variaveis de controle

# Funções

def funcao_1():
    # Criar labels e campos de entrada na janela principal
    label_valor1 = tk.Label(janela, text="Valor 1:")
    label_valor1.pack()
    entrada_valor1 = tk.Entry(janela)
    entrada_valor1.pack()

    label_valor2 = tk.Label(janela, text="Valor 2:")
    label_valor2.pack()
    entrada_valor2 = tk.Entry(janela)
    entrada_valor2.pack()

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
    janela_funcao_1 = tk.Tk()
    janela_funcao_1.title("Função 2")

# Janelas

# Janela principal
janela = tk.Tk()
janela.title("Menu Principal")
menu = tk.Menu(janela)
menu.add_command(label="Função 1", command=funcao_1)
menu.add_command(label="Função 2", command=funcao_2)
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