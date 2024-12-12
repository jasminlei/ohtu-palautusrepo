from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class PeliFactory:
    @staticmethod
    def luo_peli(valinta):
        if valinta == "a":
            return KPSPelaajaVsPelaaja()
        elif valinta == "b":
            return KPSTekoaly()
        elif valinta == "c":
            return KPSParempiTekoaly()
        else:
            raise ValueError("Tuntematon pelivalinta")
