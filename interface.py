import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

df = pd.read_csv('hey.csv')
vendas = df['vendas']
vendedor = df['vendedor']

janela = tk.Tk()
janela.geometry('250x180')
janela.title('GRÁFICOS')
texto = tk.Label(janela, text =  'Escolha qual gráfico deseja visualizar')
texto.pack()

def barras():
    plt.bar(vendedor, vendas, color = 'pink')
    plt.xlabel('Vendedores')
    plt.ylabel('Vendas')
    plt.title('Vendas por Vendedor - Gráfico de Barra')
    plt.show()

def linhas():
    plt.plot(vendedor, vendas, color = 'pink')
    plt.xlabel('Vendedores')
    plt.ylabel('Vendas')
    plt.title('Vendas por Vendedor - Gráfico de Linha')
    plt.show()


def histogram():
    plt.hist(df['vendas'], bins=9, edgecolor='black', color = 'pink')
    plt.xlabel('vendas')
    plt.ylabel('vendedores')
    plt.title('histograma')
    plt.show()


def bolinha():
    plt.scatter(vendedor, vendas, color='pink')
    plt.xlabel('Vendedores')
    plt.ylabel('Vendas')
    plt.title('Vendas por Vendedor')
    plt.show()

def pizza():
    plt.pie(vendas, labels =  vendedor)
    plt.title('Vendas')
    plt.show()


btn  =  tk.Button(janela, text='Gráfico de barras', command=barras)
btn.pack()

btn  =  tk.Button(janela, text='Gráfico de linhas', command=linhas)
btn.pack()

btn  =  tk.Button(janela, text='Histograma', command=histogram)
btn.pack()

btn  =  tk.Button(janela, text='Gráfico de dispersão', command=bolinha)
btn.pack()

btn  =  tk.Button(janela, text='Gráfico de pizza', command=pizza)
btn.pack()

janela.mainloop()