import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')

    def test_rahan_lataaminen_menee_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.2')
    
    def test_rahan_ottaaminen_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.05')
    
    def test_rahan_ottaaminen_ei_toimi_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')
    
    def test_ota_rahaa_metodi_palauttaa_true(self):
        s= self.maksukortti.ota_rahaa(5)
        self.assertEqual(s,True)

    def test_ota_rahaa_metodi_palauttaa_false(self):
        s= self.maksukortti.ota_rahaa(20)
        self.assertEqual(s,False)