from get_txt import retorna_estados

lista_estados = retorna_estados('automato_config.txt')

def procura_epsilon_cadeia(lista_estados, r=[]):
    tamanho = len(r)
    for estado in r:
        if('epsilon' in lista_estados[estado]['proximos']):
            for transicao in lista_estados[estado]['proximos']['epsilon']:
                if(transicao not in r):
                    r.append(transicao)
    
    if(len(r) == tamanho):
        return r
    return procura_epsilon_cadeia(lista_estados, r)