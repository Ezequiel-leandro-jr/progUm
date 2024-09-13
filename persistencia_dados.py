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
                    idade_paciente=int(dados[3]),
                    data_consulta=dados[4],
                    hora_consulta=dados[5],
                    especialidade=dados[6],
                    medico=dados[7],
                    tipo_consulta=dados[8],
                    acompanhante=dados[9],
                    contato_paciente=dados[10],
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
            f.write(f"{paciente.prontuario};{paciente.nome_paciente};{paciente.cpf_paciente};{paciente.idade_paciente};{paciente.data_consulta};"
                    f"{paciente.hora_consulta};{paciente.especialidade};{paciente.medico};{paciente.tipo_consulta};"
                    f"{paciente.acompanhante};{paciente.contato_paciente};{paciente.plano}\n")
