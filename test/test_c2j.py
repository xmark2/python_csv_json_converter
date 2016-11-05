import unittest
import sys, os
sys.path.append(os.getcwd() + "/../src")
from c2j import get_json_from_csv

class C2VTest(unittest.TestCase):
    def test_valid_format(self):
        csv_data = unicode("name,id\r\njohn,0\r\nfred,1\r\n")
        json_data = [{"name":"john", "id":"0"}, {"name":"fred", "id":"1"}]
        self.assertEqual(get_json_from_csv(csv_data), json_data)

if __name__ == "__main__":
    unittest.main()

