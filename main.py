# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Matheus Ferreira de Freitas, RA: 24123080-4
# Henrique

# Importando as bibliotecas necessárias
import tkinter as tk
import math
import tkinter.constants as tkc

# Constantes

# Variaveis globais
L = 0  # Largura da caixa (escolher a unidade)
Ni = 0  # n inicial da partícula
Nf = 0  # n final da partícula
a = 0  # Escolher a unidade
b = 0  # Escolher a unidade
A = 0  # Escolher a unidade
k = 0  # Escolher a unidade
Xp = 0  # Escolher a unidade

text_area_saida_1 = None
text_area_saida_2 = None
text_area_saida_ativa = None

# Funções

def funcao_1():
    def processar_1():
        global L, Ni, Nf, a, b, text_area_saida_ativa

        L = float(entrada_valor1_1.get())
        Ni = float(entrada_valor2_1.get())
        Nf = float(entrada_valor3_1.get())
        a = float(entrada_valor4_1.get())
        b = float(entrada_valor5_1.get())

        # ... (Realizar cálculos ou operações com os valores)

        # Limpar a área de saída antes de exibir a nova saída
        text_area_saida_ativa.delete(1.0, tkc.END)

        # Inserir a nova saída na área de texto
        text_area_saida_ativa.insert(tkc.END, "Resultados:\n")
        # ... (Formatar e exibir os resultados dos cálculos)

    # Criar frame para conteúdo da função 1
    frame_funcao_1 = tk.Frame(janela)

    # Criar labels e campos de entrada
    label_valor1_1 = tk.Label(frame_funcao_1, text="Largura da caixa (L) em un:")
    label_valor1_1.grid(row=0, column=0)
    entrada_valor1_1 = tk.Entry(frame_funcao_1)
    entrada_valor1_1.grid(row=0, column=1)

    label_valor2_1 = tk.Label(frame_funcao_1, text="n inicial da particula (Ni):")
    label_valor2_1.grid(row=1, column=0)
    entrada_valor2_1 = tk.Entry(frame_funcao_1)
    entrada_valor2_1.grid(row=1, column=1)

    label_valor3_1 = tk.Label(frame_funcao_1, text="n final da particula (Nf):")
    label_valor3_1.grid(row=2, column=0)
    entrada_valor3_1 = tk.Entry(frame_funcao_1)
    entrada_valor3_1.grid(row=2, column=1)

    label_valor4_1 = tk.Label(frame_funcao_1, text="a:")
    label_valor4_1.grid(row=3, column=0)
    entrada_valor4_1 = tk.Entry(frame_funcao_1)
    entrada_valor4_1.grid(row=3, column=1)
    label_valor5_1 = tk.Label(frame_funcao_1, text="b:")
    label_valor5_1.grid(row=4, column=0)
    entrada_valor5_1 = tk.Entry(frame_funcao_1)
    entrada_valor5_1.grid(row=4, column=1)

    # Criar botão de submit
    botao_submit_1 = tk.Button(frame_funcao_1, text="Processar", command=processar_1)
    botao_submit_1.grid(row=5, column=0, columnspan=2)

    # Criar área de texto para saída
    text_area_saida_1 = tk.Text(frame_funcao_1, width=50, height=10)
    text_area_saida_1.pack()

    frame_funcao_1.pack(fill=tk.X)  # Preencher horizontalmente


def funcao_2():
    def processar_2():
        global A, k, Xp, text_area_saida_ativa

        A = float(entrada_valor1_2.get())
        k = float(entrada_valor2_2.get())
        Xp = float(entrada_valor3_2.get())

        # ... (Realizar cálculos ou operações com os valores)

        # Limpar a área de saída antes de exibir a nova saída
        text_area_saida_ativa.delete(1.0, tkc.END)

        # Inserir a nova saída na área de texto
        text_area_saida_ativa.insert(tkc.END, "Resultados:\n")
        # ... (Formatar e exibir os resultados dos cálculos)

    # Criar frame para conteúdo da função 2
    frame_funcao_2 = tk.Frame(janela)

    # Criar labels e campos de entrada
    label_valor1_2 = tk.Label(frame_funcao_2, text="A em un:")
    label_valor1_2.grid(row=0, column=0)
    entrada_valor1_2 = tk.Entry(frame_funcao_2)
    entrada_valor1_2.grid(row=0, column=1)

    label_valor2_2 = tk.Label(frame_funcao_2, text="k em un:")
    label_valor2_2.grid(row=1, column=0)
    entrada_valor2_2 = tk.Entry(frame_funcao_2)
    entrada_valor2_2.grid(row=1, column=1)

    label_valor3_2 = tk.Label(frame_funcao_2, text="Xp em un:")
    label_valor3_2.grid(row=2, column=0)
    entrada_valor3_2 = tk.Entry(frame_funcao_2)
    entrada_valor3_2.grid(row=2, column=1)

    # Criar botão de submit
    botao_submit_2 = tk.Button(frame_funcao_2, text="Processar", command=processar_2)
    botao_submit_2.grid(row=5, column=0, columnspan=2)

    # Criar área de texto para saída
    text_area_saida_2 = tk.Text(frame_funcao_2, width=50, height=10)
    text_area_saida_2.pack()

    frame_funcao_2.pack(fill=tk.X)  # Preencher horizontalmente

funcao_ativa = funcao_1  # Função ativa no início (funcao_1)

def mostrar_funcao(funcao):
    global funcao_ativa, text_area_saida_ativa

    # Limpar a área de saída da função ativa
    if text_area_saida_ativa is not None:
        text_area_saida_ativa.delete(1.0, tkc.END)

    # Ocultar o frame da função inativa
    if funcao_ativa == funcao_1:
        frame_funcao_2.pack_forget()
    else:
        frame_funcao_1.pack_forget()

    # Atualizar a variável de função ativa
    funcao_ativa = funcao

    # Mostrar o frame da função ativa
    if funcao == funcao_1:
        frame_funcao_1.pack(fill=tk.X)
        text_area_saida_ativa = text_area_saida_1
    else:
        frame_funcao_2.pack(fill=tk.X)
        text_area_saida_ativa = text_area_saida_2


# Janela principal
janela = tk.Tk()
janela.title("Menu")

# Criar menu
menu = tk.Menu(janela)

# Adicionar opções de menu
menu.add_command(label="Simulador", command=lambda: mostrar_funcao(funcao_1))
menu.add_command(label="Caixa 1D", command=lambda: mostrar_funcao(funcao_2))
menu.add_separator()
menu.add_command(label="Sair", command=janela.quit)

# Configurar menu na janela
janela.config(menu=menu)

# Mostrar a janela principal
janela.mainloop()