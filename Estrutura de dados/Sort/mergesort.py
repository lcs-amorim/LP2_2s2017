def mergesort(lista):
    if (len(lista) <= 1):
        return lista
    meio = int(len(lista)/2)
    metade1 = lista[:meio]
    metade2 = lista[meio:]
    metade1 = mergesort(metade1)
    #a partir daqui, metade1 está ordenada
    metade2 = mergesort(metade2)
    #a partir daqui, metade2 está ordenada
    juntas = merge(metade1,metade2)
    return juntas
'''
defina a funcao merge do mergesort como já discutido
'''
def merge(lista1,lista2):
    if not len(lista1) or not len(lista2):
        return lista1 or lista2
    result = []
    i, j = 0, 0
    while (len(result) < len(lista1) + len(lista2)):
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i+= 1
        else:
            result.append(lista2[j])
            j+= 1
        if i == len(lista1) or j == len(lista2):
            result.extend(lista1[i:] or lista2[j:])
            break
    return result

#from mergesort_resposta import *

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_merge_simple(self):
        self.assertEqual(merge([1,2,3],[4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(merge([1,3,5],[2,4,6]), [1,2,3,4,5,6])
    
    def test_02_merge_vazios(self):
        self.assertEqual(merge([1,2,3],[]), [1,2,3])
        self.assertEqual(merge([],[2,4,6]), [2,4,6])
        self.assertEqual(merge([],[]), [])
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

