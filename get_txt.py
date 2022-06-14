def checa_entrada(linha):
    return linha.split('=')[1] == ''

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
        print('Seu arquivo nao esta na ordem correta, siga essa ordem: alfabetos, inicial, finais, transicoes')
        return None

    estados_configs = {}

    for estado in linhas[1].split('=')[1].split(','):
        estados_configs[estado] = {
            'inicial': False,
            'final': False,
            'proximos': {
            }
        }

    #checa se o alfabeto está correta
    if(checa_entrada(linhas[0])):
        print('O alfabeto precisa ter pelo menos um símbolo')
        return None
    elif('epsilon' in linhas[0]):
        print('epsilon não pode ser incluso no alfabeto')
        return None

    #checa se o estado inicial está certo
    if len(linhas[2].split('=')[1].split(',')) > 1:
        print("O autômato não pode ter mais de um estado inicial.")
        return None
    elif checa_entrada(linhas[2]):
        print("O autômato deve ter um estado inicial")
        return None
    else:
        estados_configs[linhas[2].split('=')[1]]['inicial'] = True

    if linhas[3].split('=')[1] != '':
        for estado in linhas[3].split('=')[1].split(','):
            estados_configs[estado]['final'] = True

    if(len(linhas[5:]) != 0):
        for transicao in linhas[5:]:
            transicao_estados = transicao.split(',')
            if transicao_estados[2] in estados_configs[transicao_estados[0]]['proximos'].keys():
                estados_configs[transicao_estados[0]]['proximos'][transicao_estados[2]].append(transicao_estados[1])
            else:
                estados_configs[transicao_estados[0]]['proximos'][transicao_estados[2]] = [transicao_estados[1]] 
    else:
        print("O autômato deve ter pelo menos uma transição")
        return None

    return estados_configs