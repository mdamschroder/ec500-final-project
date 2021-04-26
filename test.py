import unittest
from get_current_members import get_senators, get_house

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

def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())