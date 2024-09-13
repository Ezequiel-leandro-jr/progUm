import time
from classe_paciente import Paciente
from funcao_exibir import funcao_exibir
from crud_listar import listar
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import os
    
def cadastrar(portfolio):
    n = '0'
    while n == '0':
        especialidade = '8'
        tipo_consulta = '8'
        acompanhante = '3'
        plano = '5'
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()    
        prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()   
        nome_paciente = input('NOME COMPLETO: ').strip().upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        cpf_paciente = input('CPF: ').strip().upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        idade_paciente = int(input('IDADE: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        data_consulta = input('DATA DA CONSULTA (ex: 23/01/2024): ').strip().upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()     
        hora_consulta = input('HORA DA CONSULTA (ex: 14:00): ').upper()
        while especialidade == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            especialidade = input('''
ESPECIALIDADE:
1. Clínica Geral
2. Pediatria
3. Geriatria
4. Cardiologia
5. Gastroenterologia
6. Endocrinologia
7. Reumatologia
----------------
OP: ''')
            match especialidade:
                case '1':
                    especialidade = 'Clínica Geral'.upper()
                case '2':
                    especialidade = 'Pediatria'.upper()
                case '3':
                    especialidade = 'Geriatria'.upper()
                case '4':
                    especialidade = 'Cardiologia'.upper()
                case '5':
                    especialidade = 'Gastroenterologia'.upper()
                case '6':
                    especialidade = 'Endocrinologia'.upper()
                case '7':
                    especialidade = 'Reumatologia'.upper()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opção inválida!')
                    especialidade = '8'
                    time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        medico = input('MÉDICO(A): ').strip().upper()
        while tipo_consulta == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            tipo_consulta = input('''
    TIPO DA CONSULTA:
    1. Primeira Vez
    2. Retorno
    3. Encaixe
    4. Urgência
    5. Acompanhamento
    6. Prioritária
    7. Reagendamento
    ----------------
    OP: ''')
            match tipo_consulta:
                case '1':
                    tipo_consulta = 'Primeira Vez'.upper()
                case '2':
                    tipo_consulta = 'Retorno'.upper()
                case '3':
                    tipo_consulta = 'Encaixe'.upper()
                case '4':
                    tipo_consulta = 'Urgência'.upper()
                case '5':
                    tipo_consulta = 'Acompanhamento'.upper()
                case '6':
                    tipo_consulta = 'Prioritária'.upper()
                case '7':
                    tipo_consulta = 'Reagendamento'.upper()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    combustivel = '8'
                    time.sleep(1) 
        while acompanhante == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            acompanhante = input('ACOMPANHANTE:\n1. Sim\n2. Não\n----------------\nOP: ')
            match acompanhante:
                case '1':
                    acompanhante = 'Sim'.upper()
                case '2':
                    acompanhante = 'Não'.upper()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    acompanhante = '3'
                    time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        contato_paciente = input('CONTATO: ').strip().upper()
        while plano == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            plano = input('PLANO:\n1. Sassepe\n2. Unimed\n3. Avulso\n4. Outro\n----------------\nOP: ')
            match plano:
                case '1':
                    plano = 'Sassepe'.upper()
                case '2':
                    plano = 'Unimed'.upper()
                case '3':
                    plano = 'Avulso'.upper()
                case '4':
                    plano = 'Outro'.upper()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opção incorreta! Tente novamente!')
                    plano = '5'
                    time.sleep(1)              
        novo_paciente = Paciente(prontuario, nome_paciente, cpf_paciente, idade_paciente, data_consulta, hora_consulta, especialidade, medico, tipo_consulta, acompanhante, contato_paciente, plano)
        portfolio.append(novo_paciente)
        
        
        n = '3'
        while n == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            print('REGISTRO REALIZADO COM SUCESSO!')
            funcao_exibir(novo_paciente)
            n = input('NOVO REGISTRO [1]\nLISTAR PACIENTES [2]\nVOLTAR AO MENU [3]\n>>> ')
            if n == '1':
                n = '0'
            elif n == '2':
                listar(portfolio)
                return
            elif n == '3':
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_registrar()
                print('ERRO: opção inválida!')
                n = '3'
                time.sleep(1)
    
