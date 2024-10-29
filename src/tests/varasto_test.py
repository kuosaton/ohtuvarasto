import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ylimaara_hukkaan(self):
        testivarasto = Varasto(5, 10)
        self.assertAlmostEqual(testivarasto.saldo, 5) 

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_liika_tavara_dumpataan(self):
        # lisätään 10-kokoiseen varastoon 15
        self.varasto.lisaa_varastoon(15)

        # vapaata tilaa pitäisi olla 0, maksimikapasiteetti ylitetty
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_liika_ottaminen_huomioidaan(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_virheellinen_init_nollataan(self):
        virheellinen_varasto = Varasto(-1, -1)

        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)

    def test_virheellinen_lisays_sivuutetaan(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_virheellinen_otto_sivuutetaan(self):
        saatu_maara = self.varasto.ota_varastosta(-20)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_tulostus_on_oikea(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(f"{self.varasto}", f"saldo = 5, vielä tilaa 5")