#A biblioteca tkinter é a responsável por criar elementos gráficos - tela, labels, botoes. Nós iremos utilizar as
#classes e outros elementos existentes nessa biblioteca para contruirmos nossa interface com o usuario

import tkinter as tk
from tkinter import ttk
#Criando a janela

janela = tk.Tk()

#Configurando o titulo da janela
janela.title("Cadastro de Cliente - Supermercado")
#Configurando as dimensoes da janela
janela.geometry("600x400")
#Adicionando um label na janela
labelCliente = tk.Label(janela, text="Clientes: ")
labelCliente.place(x=110, y=10)
#Adicionando um combo no cliente
vetorOpcoes = ["Masculino", "Feminino"]
comboCliente = ttk.Combobox(janela, values=vetorOpcoes)
comboCliente.current()
comboCliente.place(x=110, y=10)
textoNome = tk.Text(janela, width=50, height=1)
textoNome.place(x=110, y=50)
#Adicionando as informações referentes ao CPF do Cliente
labelCPF = tk.Label(janela, text="CPF: ")
labelCPF.place(x=10, y=80)
textoCPF = tk.Text(janela, width=50, height=1)
textoCPF.place(x=110, y=80)
#Adicionando as informações referentes ao endereço do Cliente
labelEndereco = tk.Label(janela, text="Endereço: ")
labelEndereco.place(x=10, y=110)
textoEndereco = tk.Text(janela, width=50, height=1)
textoEndereco.place(x=110, y=110)
#Adicionando as informações referentes ao telefone do Cliente
labelTelefone = tk.Label(janela, text="Telefone: ")
labelTelefone.place(x=10, y=140)
textoTelefone = tk.Text(janela, width=50, height=1)
textoTelefone.place(x=110, y=140)
#Adicionando um botão a nossa tela
botaoInserir = tk.Button(janela, text="Inserir")
botaoInserir.place(x=50, y=170)
botaoApagar = tk.Button(janela, text="Apagar")
botaoApagar.place(x=150, y=170)
botaoAlterar = tk.Button(janela, text="Alterar")
botaoAlterar.place(x=250, y=170)
#Executando o loop principal da janela
janela.mainloop