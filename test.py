import unittest
from get_current_members import get_senators, get_house
from get_bills import get_bills

class TestApp(unittest.TestCase):
    #=============================
    #===     MEMBERS TESTS     ===
    #=============================
    def test_000_GetSenate(self):
        #----- Testing the get_senators function
        res = get_senators()
        self.assertEqual(res[0]['chamber'], "Senate")
    def test_001_GetHouse(self):
        #----- Testing the get_house function
        res = get_house()
        self.assertEqual(res[0]['chamber'], "House")
    #=============================
    #====     BILLS TESTS     ====
    #=============================
    def test_002_GetSenateBills(self):
        #----- Testing the get_bills function for senate bills
        res = get_bills('senate')
        self.assertEqual(res['chamber'], "Senate")
    def test_003_GetHouseBills(self):
        #----- Testing the get_bills function for house bills
        res = get_bills('house')
        self.assertEqual(res['chamber'], "House")

def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())