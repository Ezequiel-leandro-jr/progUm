# placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status
def funcao_exibir(paciente):
    print(f'''
PACIENTE:
----------------------------------------------------------------------------------------------------------------------
PRONTUÁRIO: {paciente.prontuario}
NOME COMPLETO: {paciente.nome_paciente}
CPF: {paciente.cpf_paciente} | IDADE: {paciente.idade_paciente} | CONTATO: {paciente.contato_paciente}
DATA DA CONSULTA: {paciente.data_consulta} | HORÁRIO: {paciente.hora_consulta} | ESPECIALIDADE: {paciente.especialidade}
MÉDICO(A): Dr.{paciente.medico} | TIPO: {paciente.tipo_consulta} | ACOMPANHANTE: {paciente.acompanhante}
PLANO: {paciente.plano}
______________________________________________________________________________________________________________________

''')