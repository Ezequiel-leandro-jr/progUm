def funcao_busca(portfolio, prontuario):
    if prontuario:
        for paciente in portfolio:
            if paciente.prontuario == prontuario:
                return paciente
    else:
        return

