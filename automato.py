import copy
mortas = []
class Automato:
    def __init__(self, estados):
        inicial = self.buscando_inicial(estados)
        self.estados = estados
        self.estado_atual = estados[inicial]
        self.caminhos = [inicial]
        #depois checar se o estado inicial é estado final
        self.aceito = self.estado_atual['final']
        self.vivo = True

    def checar_inicial(self, estado):
        if estado['inicial']:
            return estado
    
    def buscando_inicial(self, estados):
        for estado in estados.keys():
            inicial = self.checar_inicial(estados[estado])
            if inicial:
                print(estado)
                return estado

    def clonar(self, simbolo, registrar=True):
        caminhos = []
        if simbolo in self.estado_atual['proximos'] and self.vivo:
            for e in self.estado_atual['proximos'][simbolo]:
                a = copy.deepcopy(self)
                if registrar:
                    a.caminhos.append(e)
                else:
                    a.caminhos = [e]

                a.estado_atual = a.estados[e]

                a.aceito = a.estado_atual['final']
                #
                #else:
                #    a.aceito = False
                caminhos.append(a)
                continue
        else:
            #print('morreu')
            if self.caminhos[-1]:
                self.caminhos.append(None)
                mortas.append(self.caminhos)

            self.aceito = False
            self.vivo = False
            a = copy.deepcopy(self)
            caminhos.append(a)

        return caminhos

class Estado:
  def init(self, estado , inicial, final, proximos):
    self.estado = estado
    self.inicial = inicial
    self.final = final
    self.proximos = proximos

  def asdict(self):
    return {
        self.estado: {
            'inicial': self.inicial,
            'final': self.final,
            'proximos': self.proximos
        }
    }