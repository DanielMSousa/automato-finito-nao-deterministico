import copy


mortas = []

class Automato:
    def __init__(self, estados, inicial=None):
        self.inicial = inicial
        self.estados = estados
        self.estado_atual = estados[inicial]
        self.caminho = [inicial]
        self.aceito = self.estado_atual['final']
        self.vivo = True

    def clonar(self, simbolo, registrar=True):
        #caminho é onde os clones colocados
        automatos = []
        if simbolo in self.estado_atual['proximos'] and self.vivo:
            for estado in self.estado_atual['proximos'][simbolo]:
                a = copy.deepcopy(self)
                if registrar:
                    a.caminho.append(estado)
                else:
                    #quando tem epsilon no início vem pra cá
                    #ao invés de registrar como uma transição nova põe como estado inicial
                    a.caminho = [estado]

                #O estado atual vira o novo estado para onde ele foi
                a.estado_atual = a.estados[estado]

                a.aceito = a.estado_atual['final']

                automatos.append(a)
        else:
            #Morreu
            if self.caminho[-1]:
                self.caminho.append(None)
                mortas.append(self.caminho)

            self.aceito = False
            self.vivo = False
            a = copy.deepcopy(self)
            automatos.append(a)

        return automatos