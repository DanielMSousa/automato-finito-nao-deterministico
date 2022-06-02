from automato import Automato, mortas

aceito = False

e = {
    'q0' : {
        'inicial': True,
        'final': False,
        'proximos': {
            '1': ['q1', 'q0'],
            '0': ['q0'],
            'epsilon': ['q1']
        }
    },
    'q1' : {
      'inicial': False,
      'final': False,
      'proximos': { 
          '1': ['q2'],
      }
    },
    'q2' : {
      'inicial': False,
      'final': False,
      'proximos': { 
          '0': ['q3']
      }
    },
    'q3' : {
      'inicial': False,
      'final': True,
      'proximos': { 
      }
    }
}

cadeia = '10'

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
            if 'epsilon' in aut.estado_atual['proximos']:
                h = aut.clonar('epsilon')[0]
                #remove a anterior, pois ele deu um "pulo"
                pulado = h.caminhos.pop(-2)
                h.caminhos[-1] = pulado+'->'+h.caminhos[-1]
                l.append(h)
        for e in l:
            _automatos.append(e)
        automatos = _automatos

for automato in _automatos:
    print(automato.caminhos)

for automato in automatos:
    aceito = aceito or automato.aceito

print(mortas)

print(f'aceita? {aceito}')