import sqlite3

conexao = sqlite3.connect("cadastros.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    placaVeiculo TEXT,
    numVaga TEXT,
    horarioEntrada TEXT,
    horarioSaida TEXT
)
""")
conexao.commit()

def cadastrar(nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida):
    try:
        cursor.execute("""
        INSERT INTO cadastros (nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
        return False


def listar():
    try:
        cursor.execute("SELECT * FROM cadastros")
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar: {e}")
        return []


def atualizar(nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida):
    try:
        cursor.execute("UPDATE cadastros SET cpf = ?, placaVeiculo = ?, numVaga = ?, horarioEntrada = ?, horarioSaida = ? WHERE nome = ?", 
                       (cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida, nome))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
        return False


def excluir(id):
    try:
        cursor.execute("DELETE FROM cadastros WHERE id = ?", (id,))
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao excluir: {e}")
        return False
