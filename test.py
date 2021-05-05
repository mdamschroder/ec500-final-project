import unittest
from get_current_members import get_senators, get_house, filter_members
from get_bills import get_bills
from get_news import get_news
from get_data import party_line_data, dw_nominate, seniority_data, dw_line_data, get_all_senators

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
    #=============================
    #====     NEWS  TESTS     ====
    #=============================
    def test_005_GetSomeArticles(self):
        #----- Testing the news call to get some articles
        res = get_news('nba')
        self.assertGreater(len(res['articles']), 0)
    #=============================
    #====     DATA  TESTS     ====
    #=============================
    def test_006_PartyLineData(self):
        #----- Testing party line data
        get_senators()
        res = party_line_data(115, 'D')
        self.assertGreater(len(res), 0)
        res = party_line_data(111, 'R')
        self.assertGreater(len(res), 0)
    def test_007_DW(self):
        #----- Testing dw nominate score data retrieval
        res = dw_nominate("")
        self.assertGreater(len(res), 0)
        res = dw_nominate("House")
        self.assertGreater(len(res), 0)
        res = dw_nominate("Senate")
        self.assertGreater(len(res), 0)
    def test_008_Seniority(self):
        #----- Testing seniority data retrieval
        res = seniority_data()
        self.assertGreater(len(res), 0)
    def test_009_PartyDW(self):
        #----- Testing party line vs dw data retrieval
        res = dw_line_data()
        self.assertGreater(len(res), 0)




def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
    return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())