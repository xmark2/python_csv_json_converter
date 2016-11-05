import unittest
from c2j import get_json_from_csv

class C2VTest():
    def test_valid_format():
        csv_data = "name,day,id\njohn,tuesday,0\nfred,monday,1"
        self.AssertEqual(get_json_from_csv(csv_data))

