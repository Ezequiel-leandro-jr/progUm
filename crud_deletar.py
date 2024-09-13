from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def deletar(portfolio, prontuario):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_deletar()
        paciente = funcao_busca(portfolio, prontuario)
        if paciente:
            n = '4'
            while n == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_deletar()
                funcao_exibir(paciente)
                n = input('CONFIRMAR DELEÇÃO [1]\nNOVA BUSCA [2]\nVOLTAR AO MENU [3]\n>>> ')
                match n:
                    case '1':
                        portfolio.remove(paciente)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_deletar()
                        print('PACIENTE DELETADO COM SUCESSO!')
                        time.sleep(2)
                        n = '0'
                        while n == '0':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_deletar()
                            n = input('DELETAR OUTRO PACIENTE [1]\nVOLTAR AO MENU [2]\n>>> ')
                            if n == '1':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_deletar()
                                prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                            elif n == '2':
                                return
                            else:
                                print('\nERRO: opção inválida!')
                                n = '0'
                                time.sleep(1)        
                    case '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_deletar()
                        prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                        n = '5'
                    case '3':
                        n = '5'
                        return
                    case _:
                        print('\nERRO: opção inválida!')
                        n = '4'
                        time.sleep(1)
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_deletar()
                print('\nERRO: Paciente não encontrado!')
                n = input('NOVA DELEÇÃO [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_deletar()
                    prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                    break  
                elif n == '2':
                    return 
                else:
                    print('\nERRO: Opção inválida!')
                    time.sleep(1)        
            