import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "mehu", 2)
            if tuote_id == 3:
                return Tuote(3, "kauramaito", 6)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla(
        self,
    ):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5,
        )

    def test_ostetaan_kaksi_eri_tuotetta_ja_kutsutaan_tilisiirtoa_oikeilla_tiedoilla(
        self,
    ):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            7,
        )

    def test_ostetaan_kaksi_samaa_tuotetta_ja_kutsutaan_tilisiirtoa_oikeilla_tiedoilla(
        self,
    ):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            10,
        )

    def test_ostetaan_kaksi_eri_tuotetta_joista_toista_ei_varastossaja(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5,
        )

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            42,
            "12345",
            "33333-44455",
            5,
        )

        self.kauppa.aloita_asiointi()

        self.kauppa.lisaa_koriin(1)

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            43,
            "12345",
            "33333-44455",
            5,
        )

        self.viitegeneraattori_mock.uusi.assert_called_with()
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_viitegeneraattori_kutsutaan_uudelleen_maksussa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called_once()

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called_with()
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
