# importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')
# ver em: https://sqliteviewer.app/#/dados.db/table/Categoria/


# criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
    
# criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")
 

#%% Valores para deletar:
    
# 2. Definir os valores que deseja deletar
valores_para_deletar = ('Abc', 'TREABDJWBJSB', 'UUUUUUUU')

# Conecta ao banco de dados
# con = lite.connect('dados.db')

with con:
    cur = con.cursor()
    
    # Cria a string de placeholders (?,?,?) com base no tamanho da lista
    placeholders = ', '.join(['?'] * len(valores_para_deletar))
    
    # Executa o DELETE usando a lista como parâmetro
    sql = f"DELETE FROM Categoria WHERE nome IN ({placeholders})"
    cur.execute(sql, valores_para_deletar)
    
    # Verifica quantas linhas foram apagadas (opcional)
    print(f"Linhas deletadas: {cur.rowcount}")

# con.commit() # Não é necessário com 'with con:', já faz commit automático

#%% Deletando todos os valores da tabela Categoria

with con:
    cur = con.cursor()
    # 1. Deleta todos os valores da tabela
    cur.execute("DELETE FROM Categoria")    
    # 2. Reseta o auto-incremento na tabela interna do SQLite
    cur.execute("DELETE FROM sqlite_sequence WHERE name='Categoria'")
    
print("Tabela 'Categoria' limpa e IDs resetados com sucesso.")






