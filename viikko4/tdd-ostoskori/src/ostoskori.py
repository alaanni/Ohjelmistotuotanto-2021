from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori = []

    def tavaroita_korissa(self):
        count = 0
        for o in self.kori:
            count += o.lukumaara()
        return count
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        count = 0
        for t in self.kori:
            count += t.hinta()
        return count
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        found = 0
        for o in self.kori:
            if o.tuotteen_nimi() == lisattava.nimi():
                o.muuta_lukumaaraa(1)
                found = 1
        if found == 0:
            ostos = Ostos(lisattava)
            self.kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for o in self.kori:
            if o.tuotteen_nimi() == poistettava.nimi():
                o.muuta_lukumaaraa(-1)
                if o.lukumaara() == 0:
                    self.kori.remove(o)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
