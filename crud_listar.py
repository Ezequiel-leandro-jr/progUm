from crud_editar import editar
from crud_deletar import deletar
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os


def listar(portfolio):
    while True:
        i = 1
        soma = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_listar()
        for paciente in portfolio:
            print(f'''
    PACIENTE {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PRONTUÁRIO: {paciente.prontuario}
    NOME COMPLETO: {paciente.nome_paciente}
    CPF: {paciente.cpf_paciente} | IDADE: {paciente.idade_paciente} anos | CONTATO: {paciente.contato_paciente}
    DATA DA CONSULTA: {paciente.data_consulta} | HORÁRIO: {paciente.hora_consulta} | ESPECIALIDADE: {paciente.especialidade}
    MÉDICO(A): Dr.{paciente.medico} | TIPO: {paciente.tipo_consulta} | ACOMPANHANTE: {paciente.acompanhante}
    PLANO: {paciente.plano}
    ----------------------------------------------------------------------------------------------------------------------
    ''')
            i += 1
            soma += 1
            
        print(f'\nTOTAL DE PACIENTES: {soma}\n ______________________________________________________________________________________________________________________')
            
        n = input('\nEDITAR PACIENTE [1]\nDELETAR PACIENTE [2]\nVOLTAR AO MENU [3]\n>>> ')
        if n == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            prontuario = input('PRONTUÁRIO: ').split()
            editar(portfolio, prontuario)
            return
        elif n == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            prontuario = input('PRONTUÁRIO: ').split()
            deletar(portfolio, prontuario)
            return
                
        elif n == '3':
            return
        else:
            print('\nERRO: opção inválida!')
            time.sleep(1)
