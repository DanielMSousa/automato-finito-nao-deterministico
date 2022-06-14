def retorna_estados(arquivo):

    arq = open(f"{arquivo}")
    linhas = arq.readlines()

    for pos, linha in enumerate(linhas):
        linhas[pos] = linha.replace('\n', '').replace(' ', '')

    palavra_geral = 'alfabetoestadosinicialfinaistransicoes'
    verificar_palavra = ''

    for linha in range(4):
        verificar_palavra += linhas[linha].split('=')[0]
    verificar_palavra += linhas[4]

    if verificar_palavra == palavra_geral:
        pass
    else:
        print('Seu arquivo nao esta na ordem correta')
        return None

    estados_configs = {}

    for estado in linhas[1].split('=')[1].split(','):
        estados_configs[estado] = {
            'inicial': False,
            'final': False,
            'proximos': {
            }
        }

    estados_configs[linhas[2].split('=')[1]]['inicial'] = True

    for estado in linhas[3].split('=')[1].split(','):
        estados_configs[estado]['final'] = True

    for transicao in linhas[5:]:
        transicao_estados = transicao.split(',')
        if transicao_estados[2] in estados_configs[transicao_estados[0]]['proximos'].keys():
            estados_configs[transicao_estados[0]]['proximos'][transicao_estados[2]].append(transicao_estados[1])
        else:
            estados_configs[transicao_estados[0]]['proximos'][transicao_estados[2]] = [transicao_estados[1]] 

    return estados_configs