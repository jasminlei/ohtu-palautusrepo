KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        self._tarkista_kapasiteetti(self.kapasiteetti)
        self._tarkista_kapasiteetti(self.kasvatuskoko, kasvatuskoko=True)

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _tarkista_kapasiteetti(self, arvo, kasvatuskoko=False):
        if not isinstance(arvo, int) or arvo < 0:
            virheellinen_tyyppi = "kasvatuskoko" if kasvatuskoko else "kapasiteetti"
            raise ValueError(
                f"Väärä {virheellinen_tyyppi}: Arvon täytyy olla positiivinen kokonaisluku."
            )

    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        if self.mahtuu():
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        self.suurenna_listaa()
        self.ljono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True

    def suurenna_listaa(self):
        vanha_lista = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.ljono)
        return True

    def mahtuu(self):
        return self.alkioiden_lkm < len(self.ljono)

    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == luku:
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]

                self.ljono[self.alkioiden_lkm - 1] = 0
                self.alkioiden_lkm -= 1
                return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(self.alkioiden_lkm):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        a_lista = set(a.to_int_list())
        b_lista = set(b.to_int_list())

        yhdiste = a_lista.union(b_lista)

        yhdistejoukko = IntJoukko()
        for alkio in yhdiste:
            yhdistejoukko.lisaa(alkio)

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        a_lista = set(a.to_int_list())
        b_lista = set(b.to_int_list())

        yhteiset = a_lista.intersection(b_lista)

        leikkausjoukko = IntJoukko()
        for alkio in yhteiset:
            leikkausjoukko.lisaa(alkio)

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        a_lista = set(a.to_int_list())
        b_lista = set(b.to_int_list())

        ero = a_lista.difference(b_lista)

        erotusjoukko = IntJoukko()
        for alkio in ero:
            erotusjoukko.lisaa(alkio)

        return erotusjoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return (
            "{" + ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm)) + "}"
        )
