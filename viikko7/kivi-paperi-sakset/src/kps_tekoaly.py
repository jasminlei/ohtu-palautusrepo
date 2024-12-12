from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmäisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
