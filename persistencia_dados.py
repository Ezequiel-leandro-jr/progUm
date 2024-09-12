import os
from classe_paciente import Paciente

def cria_banco():
    file = 'banco.txt'

    if os.path.exists(file):
        lista_de_objetos = []
        with open(file, 'r') as f:
            for line in f:
                dados = line.strip().split(';')  # Split dos dados por ';'
                paciente = Paciente(
                    prontuario=dados[0],
                    nome_paciente=dados[1],
                    cpf_paciente=dados[2],
                    idade_paciente=dados[3],
                    data_consulta=dados[4],
                    hora_consulta=dados[5],
                    especialidade=int(dados[6]),
                    medico=dados[7],
                    tipo_consulta=dados[8],
                    acompanhante=float(dados[9]),
                    contato_paciente=float(dados[10]),
                    plano=dados[11]
                )
                lista_de_objetos.append(paciente)
        return lista_de_objetos
    else:
        return []

def salva_banco(portfolio):
    file = 'banco.txt'

    with open(file, 'w') as f:
        for paciente in portfolio:
            f.write(f"{veiculo.placa};{veiculo.tipo};{veiculo.marca};{veiculo.modelo};{veiculo.cor};"
                    f"{veiculo.ano_fabricacao};{veiculo.portas};{veiculo.combustivel};{veiculo.conservacao};"
                    f"{veiculo.quilometragem};{veiculo.preco};{veiculo.status}\n")
