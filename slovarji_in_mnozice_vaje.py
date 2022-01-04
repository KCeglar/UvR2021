#INVENTAR
print("-----------------------------------------------INVENTAR-------------------------------------------------")
inv = {'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2, 'pašteta': 10, 'mortadela': 4, 'klobasa': 7}

print("-------------Zaloga()----------")
def zaloga(inventar, artikel):
    if artikel in inventar:
        return inventar[artikel]
    return 'Tega artikla ni!'

print(zaloga(inv, 'makovka'))

print("-------------Prodaj()----------")
def prodaj(inventar, artikel, kolicina):
    if artikel in inventar:
        inventar[artikel] = inventar[artikel]-kolicina

print("Star slovar-->",inv)
prodaj(inv, 'makovka', 3)
print("Posodobljen slovar-->",inv)

print("-------------Primankljaj()----------")
def primanjkljaj(inventar, narocilo):
    manjka = {}
    for artikel_1, kolicina_1 in narocilo.items():
        if artikel_1 not in inventar:
            manjka[artikel_1] = kolicina_1
        if artikel_1 in inventar and kolicina_1>inventar[artikel_1]:
            manjka[artikel_1] = kolicina_1-inventar[artikel_1]
    return manjka

print(primanjkljaj(inv, {"pašteta": 3, "klobasa": 9, "pivo": 1}))

print("-----------------------------------------------NAJPOGOSTEJSE-------------------------------------------------")
print("-------------freq()----------")
"""
def freq(s):
    niz = "".join(sorted(s))
    pogostost_crk = {}
    niz2 = niz
    for crka in niz:
        if crka not in pogostost_crk:
            stevec_crk = 0
            i=0
            while i<len(niz2):
                if crka!=niz2[i]:
                    break
                stevec_crk+=1
                i+=1
            niz2 = niz2.strip(crka)
            pogostost_crk[crka]=stevec_crk
    return pogostost_crk
"""
def freq(s):
    tabela_crk = list(s)
    pogostost_crk = {}
    for x in tabela_crk:
        if x not in pogostost_crk:
            pogostost_crk[x] = 0
        pogostost_crk[x]+=1
    return pogostost_crk
print(freq("abcaadaaa dd ff abcdefgha"))

print("-------------max_freq()----------")
def max_freq(f):
    max_vrednost = 0
    max_crka = ''
    for crka, vrednost in f.items():
        if max_vrednost<vrednost:
            max_vrednost=vrednost
            max_crka=crka
    return max_crka

print("--->",max_freq({'a': 3, 'b': 1, 'c': 1, 'd': 1}))


#TESTI
import unittest
import collections

class TestSlovarji(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy
        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
