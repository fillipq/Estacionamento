import tkinter as tk
from tkinter import messagebox
import backend


def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)
    entrada_placa.delete(0, tk.END)
    entrada_numVaga.delete(0, tk.END)
    entrada_horarioEntrada.delete(0, tk.END)
    entrada_horarioSaida.delete(0, tk.END)
    entrada_id.delete(0, tk.END)


def cadastrar():
    nome = entrada_nome.get().strip()
    cpf = entrada_cpf.get().strip()
    placaVeiculo = entrada_placa.get().strip()
    numVaga = entrada_numVaga.get().strip()
    horarioEntrada = entrada_horarioEntrada.get().strip()
    horarioSaida = entrada_horarioSaida.get().strip()

    if not nome or not cpf or not placaVeiculo or not numVaga or not horarioEntrada or not horarioSaida:
        messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios!")
        return

    if len(cpf) != 11 or not cpf.isdigit():
        messagebox.showwarning("Erro", "CPF deve ter 11 dígitos!")
        return

    if len(placaVeiculo) < 7:
        messagebox.showwarning("Erro", "Placa de veículo inválida!")
        return

    try:
        backend.cadastrar(nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        limpar_campos()
        listar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")

def atualizar():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    placaVeiculo = entrada_placa.get()  
    numVaga = entrada_numVaga.get()
    horarioEntrada = entrada_horarioEntrada.get()
    horarioSaida = entrada_horarioSaida.get()

    if not nome or not cpf or not placaVeiculo or not numVaga or not horarioEntrada or not horarioSaida:
        messagebox.showwarning("Erro", "Preencha os campos obrigatórios!")
        return

    backend.atualizar(nome, cpf, placaVeiculo, numVaga, horarioEntrada, horarioSaida)
    messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
    listar()

def listar():
    registros = backend.listar()
    texto_lista.delete("1.0", tk.END)

    for r in registros:
        texto_lista.insert(tk.END, f"{r}\n")

def excluir():
    id = entrada_id.get()

    if not id:
        messagebox.showwarning("Erro", "Informe o ID!")
        return

    backend.excluir(id)
    messagebox.showinfo("Sucesso", "Registro excluído!")
    listar()

janela = tk.Tk()
janela.title("Sistema de Estacionamento")

tk.Label(janela, text="Nome:").grid(row=0, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="cpf:").grid(row=1, column=0)
entrada_cpf = tk.Entry(janela)
entrada_cpf.grid(row=1, column=1)


tk.Label(janela, text="placa do veiculo:").grid(row=2, column=0)
entrada_placa = tk.Entry(janela)
entrada_placa.grid(row=2, column=1)

tk.Label(janela, text="numero da Vaga:").grid(row=3, column=0)
entrada_numVaga = tk.Entry(janela)
entrada_numVaga.grid(row=3, column=1)

tk.Label(janela, text="horario deEntrada:").grid(row=4, column=0)
entrada_horarioEntrada = tk.Entry(janela)
entrada_horarioEntrada.grid(row=4, column=1)

tk.Label(janela, text="horario de Saida:").grid(row=5, column=0)
entrada_horarioSaida = tk.Entry(janela)
entrada_horarioSaida.grid(row=5, column=1)

tk.Label(janela, text="ID Atualizar/Excluir:").grid(row=6, column=0)
entrada_id = tk.Entry(janela)
entrada_id.grid(row=6, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=7, column=1)
tk.Button(janela, text="Atualizar Dados", command=atualizar).grid(row=7, column=0)
tk.Button(janela, text="Listar", command=listar).grid(row=8, column=1)
tk.Button(janela, text="Excluir", command=excluir).grid(row=8, column=0)

texto_lista = tk.Text(janela, height=10, width=60)
texto_lista.grid(row=9, column=0, columnspan=2)

janela.mainloop()
