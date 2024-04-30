# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Matheus Ferreira de Freitas, RA: 24123080-4
# Henrique


#Arrumei Os Import :)
import tkinter as tk
import math
#import matplotlib

# Janela principal
janela = tk.Tk()
janela.title("Menu")

# Variáveis globais para os frames (para poder destruí-los depois) 
frame_entrada = None
frame_saida = None

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


#Essa função aqui é a resposavel por Limpar os frames (destruir) pra você não ter uma função que usao o jutsu clone das sombras
def limpar_frames():
    global frame_entrada, frame_saida
    if frame_entrada:
        frame_entrada.destroy()
    if frame_saida:
        frame_saida.destroy()


#Por favor muda deixa eu Mudar o nome dessas funções de uma maneira que fiquedescrito a funcionalidade delas tipo
def funcao_1():
    global frame_entrada, frame_saida
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)

    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    # Criar labels e campos de entrada
    label_valor1 = tk.Label(frame_entrada, text="Largura da caixa (L) em un:")
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

    label_valor4 = tk.Label(frame_entrada, text="a:")
    label_valor4.grid(row=3, column=0)
    entrada_valor4 = tk.Entry(frame_entrada)
    entrada_valor4.grid(row=3, column=1)

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


def funcao_2():
    global frame_entrada, frame_saida
    limpar_frames()  # Limpa os frames existentes(pra não gerar varios clones)

    frame_entrada = tk.Frame(janela)
    frame_entrada.pack()

    # Criar labels e campos de entrada
    label_valor1 = tk.Label(frame_entrada, text="A em un:")
    label_valor1.grid(row=0, column=0)
    entrada_valor1 = tk.Entry(frame_entrada)
    entrada_valor1.grid(row=0, column=1)

    label_valor2 = tk.Label(frame_entrada, text="k em un:")
    label_valor2.grid(row=1, column=0)
    entrada_valor2 = tk.Entry(frame_entrada)
    entrada_valor2.grid(row=1, column=1)

    label_valor3 = tk.Label(frame_entrada, text="Xp em un:")
    label_valor3.grid(row=2, column=0)
    entrada_valor3 = tk.Entry(frame_entrada)
    entrada_valor3.grid(row=2, column=1)

    # Criar botão de submit
    botao_submit = tk.Button(frame_entrada, text="Processar", command=lambda: processar_2())
    botao_submit.grid(row=5, column=0, columnspan=2)

    def processar_2():
        global A, k, Xp

        A = float(entrada_valor1.get())
        k = float(entrada_valor2.get())
        Xp = float(entrada_valor3.get())

        # ... (Realizar cálculos ou operações com os valores)

#Janelas

#Janela principal
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