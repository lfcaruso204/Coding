# importando SQLite
import sqlite3 as lite
import pandas as pd


# criando conexão
con = lite.connect('dados.db')


#%% -------- Funções de Inserção -----------


# inserir categoria


def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i) # Alimentacao
    
# inserir receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)
        
# inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)


#%% -------- Funções para Deletar -----------


# deletar receitas
def deletar_receita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query,i)

# deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query,i)

def resetar_banco():
    with con:
        cur = con.cursor()
        # Deleta todos os dados das três tabelas
        cur.execute("DELETE FROM Receitas")
        cur.execute("DELETE FROM Gastos")
        cur.execute("DELETE FROM Categoria") # Certifique-se que o nome é 'Categoria'
        
        # Reseta os contadores de ID (AUTOINCREMENT) para começarem do 1 novamente
        cur.execute("DELETE FROM sqlite_sequence WHERE name='Receitas'")
        cur.execute("DELETE FROM sqlite_sequence WHERE name='Gastos'")
        cur.execute("DELETE FROM sqlite_sequence WHERE name='Categoria'")

# tentei incluir o botão "Refresh", porém ainda não consegui

#%% -------- Funções para Ver Dados -----------


# ver categoria
def ver_categoria():
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

# ver receitas
def ver_receita():
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

# ver gastos
def ver_gastos():
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens


#%% -------- Funções para Dados da Tabela-----------


def tabela():
    gastos = ver_gastos()
    receitas = ver_receita()
    
    tabela_lista = []
    
    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)        
        
    return tabela_lista


#%% -------- Funções para Dados do Grafico de Barra -----------
    
def bar_valores():
    # Receita Total
    receitas = ver_receita()
    receitas_lista = []
    
    for i in receitas:
        receitas_lista.append(i[3])
    
    receita_total = sum(receitas_lista)    
    
    # Despesas Total
    gastos = ver_gastos()
    gastos_lista = []
    
    for i in gastos:
        gastos_lista.append(i[3])
    
    gastos_total = sum(gastos_lista)
    
    # Saldo Total
    saldo_total = receita_total - gastos_total
    
    return [receita_total, gastos_total, saldo_total]




#%% -------- Funções para Dados do Grafico Pie -----------


# função grafico pie
def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []
    
    for i in gastos:
        tabela_lista.append(i)
        
    dataframe = pd.DataFrame(tabela_lista, columns=['id', 'categoria', 'Data', 'valor'])
    dataframe = dataframe.groupby('categoria')['valor'].sum()
    
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []
    
    for i in dataframe.index:
        lista_categorias.append(i)
    
    return([lista_categorias, lista_quantias])


def percentagem_valor():
    # Receita Total
    receitas = ver_receita()
    receita_total = sum(i[3] for i in receitas)
    
    # Despesas Total
    gastos = ver_gastos()
    gasto_total = sum(i[3] for i in gastos)
    
    # Verificação para evitar divisão por zero
    if receita_total == 0:
        return [0]  # Retorna 0% se não houver receita
        
    # Percentagem Total
    total = ((receita_total - gasto_total) / receita_total) * 100 

    return [total]