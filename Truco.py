import random


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        if self.valor == "Ás":
            return "Bastião" if self.naipe == "Bastos" else self.naipe[:-2] + "ão"
        return f"{self.valor} de {self.naipe}"


class Baralho:
    def __init__(self):
        self.cartas = []

    def criarCarta(self, valor, naipe):
        self.cartas.append(Carta(valor, naipe))

    def valor_carta(self, carta):
        ordem = [4, 5, 6, 7, "Valete", "Cavalo", "Rei", "Ás", 2, 3]
        if carta.valor == 7 and carta.naipe == "Ouros": return len(ordem)
        elif carta.valor == 7 and carta.naipe == "Espadas": return len(ordem)+1
        elif carta.valor == "Ás" and carta.naipe == "Bastos": return len(ordem)+2
        elif carta.valor == "Ás" and carta.naipe == "Espadas": return len(ordem)+3
        else: return ordem.index(carta.valor)

    def menorValor(self):
        if not self.cartas: return None
        return min(self.cartas, key=self.valor_carta)

    def maiorValor(self):
        if not self.cartas: return None
        return max(self.cartas, key=self.valor_carta)

    def primeiroNaipe(self):
        if not self.cartas: return None
        return self.cartas[0].naipe

    def ultimoNaipe(self):
        if not self.cartas: return None
        return self.cartas[-1].naipe

    def numeroDeCartas(self):
        return len(self.cartas)

    def __iter__(self):
        self.itr = 0
        return self

    def __next__(self):
        if self.itr < self.numeroDeCartas():
            self.itr += 1
            return self.cartas[self.itr - 1]
        raise StopIteration

    def embaralhar(self):
        if self.cartas: random.shuffle(self.cartas)

    def pegaCarta(self):
        if not self.cartas: return None
        self.itr = max(0, self.itr - 1)
        return self.cartas.pop()

    def __str__(self):
        if not self.cartas: return None
        return ", ".join([str(carta) for carta in self.cartas])


class BaralhoTruco(Baralho):
    def __init__(self):
        super().__init__()
        for valor in ["Ás", 2, 3, 4, 5, 6, 7, "Valete", "Cavalo", "Rei"]:
            for naipe in ["Ouros", "Bastos", "Copas", "Espadas"]:
                self.criarCarta(valor, naipe)


b = BaralhoTruco()
b.embaralhar()

for carta in b:
    carta = b.pegaCarta()
    print(carta)

