import unittes
from Funciones.par import es_par

class TestPar(unittest.TestCase):
	
	def test_par(self):
		self.assertTrue(es_par(4))
	
	def test_impar(self):
		self.assertFalse(es_par(5))
if __name__ == '__main__':
	unittest.main()