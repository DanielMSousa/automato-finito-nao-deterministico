import copy
mortas = []
class Automato:
    def __init__(self, estados):
        self.estados = estados
        self.estado_atual = estados['q0']
        self.caminhos = ['q0']
        #depois checar se o estado inicial é estado final
        self.aceito = False

    def clonar(self, simbolo):
        caminhos = []
        if simbolo in self.estado_atual['proximos']:
            for e in self.estado_atual['proximos'][simbolo]:
                a = copy.deepcopy(self)
                a.caminhos.append(e)
                a.estado_atual = a.estados[e]
                if(a.estado_atual['final']):
                    a.aceito = True
                else:
                    a.aceito = False
                caminhos.append(a)
                continue
        else:
            print('morreu')
            self.caminhos.append(None)
            #caminhos.append(self)
            mortas.append(self.caminhos)
            self.aceito = False

        return caminhos

class Estado:
  def init(self, inicial, final, proximos):
    self.inicial = inicial
    self.final = final
    self.proximos = proximos

  def asdict(self):
    return {
        'inicial': self.inicial,
        'final': self.final,
        'proximos': self.proximos
    }