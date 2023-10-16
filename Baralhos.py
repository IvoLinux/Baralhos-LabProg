import random
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self, values = [], suits = []):
        self.cartas = [Carta(valor, naipe) for valor in values for naipe in suits]

    def create_deck(self, values, suits):
        self.cartas = [Carta(valor, naipe) for valor in values for naipe in suits]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def criaCarta(self, valor, naipe):
        self.cartas.append(Carta(valor, naipe))

    def card_value_as_number(self, carta):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
        return values.index(carta.valor)

    def menorValor(self):
        if not self.cartas:
            return None
        return min(self.cartas, key=self.card_value_as_number)

    def maiorValor(self):
        if not self.cartas:
            return None
        return max(self.cartas, key=self.card_value_as_number)

    def primeiroNaipe(self):
        if not self.cartas:
            return None
        return self.cartas[0].suit

    def ultimoNaipe(self):
        if not self.cartas:
            return None
        return self.cartas[-1].suit

    def pegaCarta(self):
        if len(self.cartas) > 0:
            self.iterator = max(0, self.iterator - 1)
            return self.cartas.pop()
        else:
            return None
    
    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < len(self.cartas):
            carta = self.cartas[self.iterator]
            self.iterator += 1
            return carta
        raise StopIteration

class BaralhoPoker(Baralho):
    def __init__(self, values = [], suits = []):
        super().__init__()
        self.create_deck()

    def create_deck(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
        suits = ['Copas', 'Ouros', 'Paus', 'Espadas']
        super().create_deck(values, suits)

# values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei', 'As']
# suits = ['Copas', 'Ouros', 'Paus', 'Espadas']

deck = BaralhoPoker()
deck.embaralhar()

for card in deck:
    carta = deck.pegaCarta()
    if carta:
        print(f"Carta: {carta}")
    else:
        print('cabo')