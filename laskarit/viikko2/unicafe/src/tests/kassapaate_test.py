import unittest
from kassapaate import Kassapaate

from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate=Kassapaate()
        self.kortti=Maksukortti(400)
        self.kortti1=Maksukortti(200)
        

    def test_kassassa_rahaa_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kassassa_myytyjen_lounaiden_maara_oikein(self):
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)
    
    #käteisosto edulliset lounaat

    def test_edullisesti_kateisella_rahaa_oikein(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+240)
    
    def test_edullisesti_kateisella_vaihtorahaa_oikein(self):
        s=self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(s, 500-240)

    def test_edullisesti_kateisella_maara_oikein(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.edulliset, 1)

    def test_edullisesti_kateisella_rahaa_vaarin(self):
        self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_edullisesti_kateisella_vaihtorahaa_oikein_maksu_vaarin(self):
        s=self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(s, 200)

    def test_edullisesti_kateisella_maara_oikein_maksu_vaarin(self):
        self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.paate.edulliset, 0)
    
    #käseisellä maksu maukkat
    def test_maukkaasti_kateisella_rahaa_oikein(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+400)
    
    def test_maukkaasti_kateisella_vaihtorahaa_oikein(self):
        s=self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(s, 500-400)

    def test_maukkaasti_kateisella_maara_oikein(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_maukkaasti_kateisella_rahaa_vaarin(self):
        self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_maukkaasti_kateisella_vaihtorahaa_oikein_maksu_vaarin(self):
        s=self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(s, 200)

    def test_maukkaasti_kateisella_maara_oikein_maksu_vaarin(self):
        self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.paate.maukkaat, 0)

    #korttiosto käteisellä
    #rahaa on tarpeeksi

    def test_edullinen_lounas_kortti_veloitettu(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), 'saldo: 1.6')
    
    def test_edullinen_lounas_kortti_booli_arvo_oikein(self):
        s=self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(s, True)

    def test_edullinen_lounas_kortti_myytyjen_lounaiden_maara_oikein_rahaa_tarpeeksi(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 1)

    def test_edullinen_lounas_kortti_rahaa_vaarin_kortti_saldo_oikein(self):
        self.paate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), 'saldo: 2.0')
    
    #rahaa ei ole tarpeeksi
    def test_edullinen_lounas_kortti_booli_arvo_oikein_rahaa_vaarin(self):
        s=self.paate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(s, False)

    def test_edullinen_lounas_kortti_myytyjen_lounaiden_maara_oikein_rahaa_ei_tarpeeksi(self):
        self.paate.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.paate.edulliset, 0)
    
    def test_kassassa_rahaa_ei_muutu_edullinen_lounas_kortti(self):
        self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    #syö maukkaasti maukas lounas kortilla maksu
    #rahaa on tarpeeksi
    def test_maukas_lounas_kortti_veloitettu(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), 'saldo: 0.0')
    
    def test_maukas_lounas_kortti_booli_arvo_oikein(self):
        s=self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(s, True)

    def test_maukas_lounas_kortti_myytyjen_lounaiden_maara_oikein_rahaa_tarpeeksi(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_maukas_lounas_kortti_rahaa_vaarin_kortti_saldo_oikein(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), 'saldo: 2.0')
    
    #rahaa ei ole tarpeeksi

    def test_maukas_lounas_kortti_booli_arvo_oikein_rahaa_vaarin(self):
        s=self.paate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(s, False)

    def test_maukas_lounas_kortti_myytyjen_lounaiden_maara_oikein_rahaa_ei_tarpeeksi(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.paate.maukkaat, 0)
    
    def test_kassassa_rahaa_ei_muutu_maukas_lounas_kortti(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    #kortille rahan lataaminen yli 0 euroa
    def test_kortti_saldo_muuttuu(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(str(self.kortti), 'saldo: 5.0')
    
    def test_kassassa_rahamaara_kasvaa(self):
        self.paate.lataa_rahaa_kortille(self.kortti,100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)
    
    ##kortille rahan lataaminen alle 0 euroa
    def test_kortti_saldo_ei_muutu(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -5)
        self.assertEqual(str(self.kortti), 'saldo: 4.0')
    
    def test_kassassa_rahamaara_ei_kasva(self):
        self.paate.lataa_rahaa_kortille(self.kortti,-5)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)