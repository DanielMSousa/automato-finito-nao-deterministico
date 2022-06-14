from automato import Automato
from get_txt import retorna_estados

def is_cadeia_aceita(automatos, aceito=False):
    for automato in automatos:
        aceito = aceito or (automato.aceito and automato.vivo)
    
    print()

    if aceito:
        print('Como pelo menos um dos autômatos foi aceito, a cadeia foi aceita')
    else:
        print('Nenhum dos autômatos foi aceito, logo a cadeia foi rejeitada')


def is_automato_aceito(automato):
    if automato.aceito:
        return 'automato aceitou'
    return 'automato rejeitou'

resposta = 'S'

while (resposta.upper() == 'S' and resposta.upper() != 'N'):

    #Começa rejeitando
    aceito = False

    e = retorna_estados('automato_config.txt')

    if(e == None):
        break

    cadeia = input('Insira uma cadeia para testar o automato: ')

    a = Automato(e)

    automatos = [a]
    for automato in a.clonar('epsilon', False):
        automatos.append(automato)
    
    if len(cadeia) != 0:
        for simbolo in cadeia:
            _automatos = []
            for automato in automatos:
                #Processa o símbolo
                l = [automato for automato in automato.clonar(simbolo)]
                #permite que o automato faça transicoes epsilons
                for aut in l:
                    #caso haja uma epsilons entre as próximas transições ele manda um clone realizar ela
                    if 'epsilon' in aut.estado_atual['proximos'] and aut.vivo:
                        h = aut.clonar('epsilon')[0]
                        #remove a anterior, pois ele deu um "pulo"
                        pulado = h.caminho.pop(-2)
                        h.caminho[-1] = f"{pulado}->{h.caminho[-1]}"
                        #Adiciona o clone que foi pro epsílon na lista
                        l.append(h)
                for e in l:
                    _automatos.append(e)
                automatos = _automatos

    for pos, automato in enumerate(automatos):
        print(f"[automato-{pos + 1}]:{automato.caminho} |-> {is_automato_aceito(automato)}")

    is_cadeia_aceita(automatos, aceito)

    resposta = input('Deseja processar novamente ? [S, N]: ')