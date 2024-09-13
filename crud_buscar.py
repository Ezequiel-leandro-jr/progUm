from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from crud_editar import editar
from crud_deletar import deletar
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def buscar(portfolio, prontuario):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_buscar()
        paciente = funcao_busca(portfolio, prontuario)
        if paciente:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_buscar()
            funcao_exibir(paciente)
            op = input('EDITAR [1]\nDELETAR [2]\nNOVA BUSCA [3]\nVOLTAR AO MENU [4]\n>>> ')
            match op:
                case '1':
                    editar(portfolio, prontuario)
                    break
                case '2':
                    deletar(portfolio, prontuario)
                    break
                case '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_buscar()
                    prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                    continue
                case '4':
                    return
                case _:
                    print('\nERRO: opção inválida!')
                    time.sleep(1)
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_buscar()
                print('ERRO: Paciente não encontrado!')
                n = input('NOVA BUSCA [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_buscar()
                    prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
                    break  
                elif n == '2':
                    return 
                else:
                    print('\nERRO: Opção inválida!')
                    time.sleep(1)