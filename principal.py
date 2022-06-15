from automato import Automato
from get_txt import retorna_estados
from detectar_inicio import procura_epsilon_cadeia

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

config_estados = retorna_estados('automato_config.txt')

def checar_inicial(estado):
        if estado['inicial']:
            return estado
    
def buscando_inicial(estados):
    for estado in estados.keys():
        inicial = checar_inicial(estados[estado])
        if inicial:
            print(estado)
            return estado

while (resposta.upper() == 'S'):
    #Começa rejeitando
    aceito = False

    #Impede o programa de executar se tiver algo errado no automato_config.txt
    if(config_estados == None):
        break
    
    #Processamento de entrada
    cadeia = input('Insira uma cadeia para testar o automato: ')

    automatos = []
    for inicial in procura_epsilon_cadeia(config_estados, [buscando_inicial(config_estados)]):
        automatos.append(Automato(config_estados, inicial))

    #Processamento da cadeia -----------------------------------------------------
    if(len(cadeia) != 0):
        for simbolo in cadeia:
            clones_automatos = []
            for automato in automatos:
                lista_automatos_processados = [clone for clone in automato.clonar(simbolo)]
                for automato_clone in lista_automatos_processados:
                    if('epsilon' in automato_clone.estado_atual['proximos'] and automato_clone.vivo):
                        epsilon_transicoes = automato_clone.clonar('epsilon')

                        for pulo in epsilon_transicoes:
                            #remove a anterior, pois ele deu um "pulo"
                            estado_anterior = pulo.caminho.pop(-2)
                            novo_estado = pulo.caminho[-1]
                            pulo.caminho[-1] = f"{estado_anterior}->{novo_estado}"
                            #Adiciona o clone que foi pro epsílon na lista
                            lista_automatos_processados.append(pulo)
                            
                for automato in lista_automatos_processados:
                    clones_automatos.append(automato)
            
                automatos = clones_automatos
    
    #Saída
    for pos, automato in enumerate(automatos):
        print(f"[automato-{pos + 1}]:{automato.caminho} |-> {is_automato_aceito(automato)}")

    is_cadeia_aceita(automatos, aceito)

    resposta = input('Deseja processar novamente ? [S, N]: ')