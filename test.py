import unittest
from get_current_members import get_senators, get_house, filter_members
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
    def test_002_FilterMembers(self):
        result = get_house()
        res = filter_members(result, "PA", "D")
        self.assertGreater(len(res), 0)
        res = filter_members(result, None, None)
        self.assertGreater(len(res), 0)
    #=============================
    #====     BILLS TESTS     ====
    #=============================
    def test_003_GetSenateBills(self):
        #----- Testing the get_bills function for senate bills
        res = get_bills('senate')
        self.assertEqual(res['chamber'], "Senate")
    def test_004_GetHouseBills(self):
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