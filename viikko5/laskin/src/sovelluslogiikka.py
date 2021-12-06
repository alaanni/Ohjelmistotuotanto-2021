class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edelliset = []
        self.edelliset.append(tulos)

    def miinus(self, arvo):
        self.edelliset.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edelliset.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edelliset.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.edelliset.pop()
