class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        siirrot = ["k", "p", "s"]
        siirto = siirrot[self._siirto]
        self._siirto = (self._siirto + 1) % len(siirrot)
        return siirto

    def aseta_siirto(self):
        # ei tehdä mitään
        pass
