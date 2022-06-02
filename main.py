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
    automato.caminhos = ['q1']
    automatos.append(automato)

for automato in automatos:
    print(automato.estado_atual)

for simbolo in cadeia:
    _automatos = []
    for automato in automatos:
        l = [automato for automato in automato.clonar(simbolo)]
        for e in l:
            _automatos.append(e)
        automatos = _automatos

for automato in _automatos:
    print(automato.caminhos)

for automato in automatos:
    aceito = aceito or automato.aceito

print(mortas)

print(f'aceita? {aceito}')