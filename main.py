from automato import Automato, mortas
from get_txt import retorna_estados

def is_automato_aceito(automato):
    if automato.aceito:
        return 'automato aceitou'
    return 'automato rejeitou'

resposta = 'S'

while (resposta.upper() == 'S' and resposta.upper() != 'N'):

    aceito = False

    e = retorna_estados('automato_config.txt')

    cadeia = input('Insira uma cadeia para testar o automato: ')

    a = Automato(e)

    #for e in a.estados['q0']:
    automatos = [a]
    for automato in a.clonar('epsilon', False):
        automatos.append(automato)

    for simbolo in cadeia:
        _automatos = []
        for automato in automatos:
            l = [automato for automato in automato.clonar(simbolo)]
            #permite que o automato faça transicoes epsilons
            for aut in l:
                #caso haja uma epsilons entre as próximas transições ele manda um clone realizar ela
                if 'epsilon' in aut.estado_atual['proximos'] and aut.vivo:
                    h = aut.clonar('epsilon')[0]
                    #remove a anterior, pois ele deu um "pulo"
                    pulado = h.caminhos.pop(-2)
                    h.caminhos[-1] = f"{pulado}->{h.caminhos[-1]}"
                    l.append(h)
            for e in l:
                _automatos.append(e)
            automatos = _automatos

    for pos, automato in enumerate(_automatos):
        print(f"[automato-{pos + 1}]:{automato.caminhos} |-> {is_automato_aceito(automato)}")

    for automato in automatos:
        aceito = aceito or automato.aceito

    #print(mortas)

    print(f'aceita? {aceito}')
    resposta = input('Deseja processar novamente ? [S, N]: ')