from funcao_busca import funcao_busca
from classe_paciente import Paciente
from funcao_exibir import funcao_exibir
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def editar(portfolio, prontuario):
    while True:
        paciente = funcao_busca(portfolio, prontuario)

        if paciente:
            indice = portfolio.index(paciente)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_editar()
                funcao_exibir(paciente)
                op = input('CONTINUAR EDIÇÃO [1]\nEDITAR OUTRO PACIENTE [2]\nVOLTAR AO MENU [3]\n>>> ') 
                if op == '1':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_editar()
                        funcao_exibir(paciente)
                        alterar = input('SELECIONE O CAMPO:\n1. Prontuário\n2. Nome completo\n3. CPF\n4. Idade\n5. Data da consulta\n6. Hora da consulta\n7. Especialidade\n8. Médico(a)\n9. Tipo de consulta\n10. Acompanhante\n11. Contato\n12. Plano\n\n0. Voltar\n>> ')
                        if alterar == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.prontuario = input('PRONTUÁRIO: ').strip()
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '7':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                especialidade = input('''
ESPECIALIDADE:
1. Clínica Geral
2. Pediatria
3. Geriatria
4. Cardiologia
5. Gastroenterologia
6. Endocrinologia
7. Reumatologia

0. Cancelar
----------------
OP: ''')
                                if especialidade in ['1', '2', '3', '4', '5', '6', '7']:
                                    especialidades = ['Clínica Geral', 'Pediatria', 'Geriatria', 'Cardiologia', 'Gastroenterologia', 'Endocrinologia', 'Reumatologia']
                                    paciente.especialidade = especialidades[int(especialidade) - 1]
                                    portfolio[indice] = paciente
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif especialidade == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '2':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.nome_paciente = input('NOME COMPLETO: ').split()
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.cpf_paciente = input('CPF: ').split()
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '4':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.idade_paciente = int(input('IDADE: '))
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '5':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.data_consulta = input('DATA DA CONSULTA (ex: 23/01/2024): ').split()
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '6':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.hora_consulta = input('HORÁRIO (ex: 14:00): ')
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '9':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                tipo_consulta = input('''
TIPO DA CONSULTA:
1. Primeira Vez
2. Retorno
3. Encaixe
4. Urgência
5. Acompanhamento
6. Prioritária
7. Reagendamento

0. Cancelar
----------------
OP:  ''')
                                if tipo_consulta in ['1', '2', '3', '4', '5', '6', '7']:
                                    consultas = ['Primeira Vez', 'Retorno', 'Encaixe', 'Urgência', 'Acompanhamento', 'Prioritária', 'Reagendamento']
                                    paciente.tipo_consulta = consultas[int(tipo_consulta) - 1]
                                    portfolio[indice] = paciente
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif tipo_consulta == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '10':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                acompanhante = input('ACOMPANHANTE:\n1. Sim\n2. Não\n\n\n0. Cancelar\n----------------\nOP: ')
                                if acompanhante in ['1', '2']:
                                    paciente.acompanhante = 'Sim' if conservacao == '1' else 'Não'
                                    portfolio[indice] = paciente
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif acompanhante == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '8':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.medico = input('MÉDICO(A): ')
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '11':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            paciente.contato_paciente = input('CONTATO: ')
                            portfolio[indice] = paciente
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '12':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                plano = input('PLANO:\n1. Sassepe\n2. Unimed\n3. Avulso\n4. Outro\n\n0. Cancelar\n----------------\nOP: ')
                                if plano in ['1', '2', '3', '4']:
                                    planos = ['Sassepe', 'Unimed', 'Avulso', 'Outro']
                                    paciente.plano = status_opcoes[int(status) - 1]
                                    portfolio[indice] = paciente
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif plano == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção inválida!')
                                    time.sleep(1)
                        elif alterar == '0':
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('ERRO: Opção inválida!')
                            time.sleep(1)
                            continue           
                            
                elif op == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                    break
                elif op == '3':
                    return  
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
        else:
            
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_editar()
                print('ERRO: Paciente não encontrado!')
                n = input('EDITAR NOVO PACIENTE [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                    break  
                elif n == '2':
                    return 
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
