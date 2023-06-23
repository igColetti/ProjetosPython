#importando SQLite

import sqlite3 as lite

#criando conexao

con = lite.connect('banco.db')

# criando tabela

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE PESSOA(NOME TEXT, CPF TEXT, ENDERECO TEXT, CIDADE TEXT, ESTADO TEXT, SEXO TEXT, EMAIL TEXT, DATA_NASCIMENTO TEXT, OBS TEXT)")
    con.commit()
    
    def adicionarPessoa(nome,cpf,endereco,cidade,estado,sexo,email,data_nascimento,obs):
        cur.execute("INSERT INTO PESSOA(CPF,NOME, ENDERECO, CIDADE, ESTADO, SEXO, EMAIL, DATA_NASCIMENTO, OBS) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome,cpf,endereco,cidade,estado,sexo,email,data_nascimento,obs))
        con.commit()
        
    def excluirPessoa(cpf):
        cur.execute("DELETE FROM PESSOA WHERE CPF = ?", (cpf,))
        con.commit()
        
    def listaPessoas():
        cur.execute("SELECT * FROM PESSOA")
        data = cur.fetchall()
        con.commit()

        # Criar array principal
        pessoas = []

        # Percorrer os resultados da query e adicionar cada pessoa como um array ao array principal
        for pessoa in data:
            pessoa_array = list(pessoa)  # Converter a tupla em um array
            pessoas.append(pessoa_array)

        return pessoas
        
        
    
