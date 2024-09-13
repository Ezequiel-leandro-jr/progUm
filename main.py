from classe_paciente import Paciente
from persistencia_dados import cria_banco, salva_banco
from crud_registrar import cadastrar
from crud_editar import editar
from crud_buscar import buscar
from crud_listar import listar
from crud_deletar import deletar
from titulos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os

portfolio = cria_banco()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo_automarket()
    op = input('''
         MENU
---------------------
1. REGISTRAR PACIENTE
2. BUSCAR PACIENTE
3. EDITAR PACIENTE
4. LISTAR PACIENTES
5. DELETAR PACIENTE

0. SAIR DO SISTEMA
---------------------
OP: ''')

    match op:
        case '1':
            cadastrar(portfolio)
            salva_banco(portfolio)
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_buscar()
            prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
            buscar(portfolio, prontuario)
            salva_banco(portfolio)
        case '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_editar()
            prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
            editar(portfolio, prontuario)
            salva_banco(portfolio)
        case '4':
            listar(portfolio)
            salva_banco(portfolio)
        case '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_deletar()
            prontuario = str(input('PRONTUÁRIO: ')).strip().upper()
            deletar(portfolio, prontuario)
            salva_banco(portfolio)
        case '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nSAINDO DO SISTEMA...')
            time.sleep(1)
            salva_banco(portfolio)
            break
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nERRO: OPÇÃO INVÁLIDA!')
            salva_banco(portfolio)
            time.sleep(1)
