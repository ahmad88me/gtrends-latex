import unittest
import gtrends

class gtrendsTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_squeeze(self):
        d = gtrends.squeeze("tests/gtrends1.csv")
        correct_d = {
            "2004": {
                "XML: (Worldwide)": [93, 100],
                "CSV: (Worldwide)": [0.5, 11],
            },
            "2005": {
                "XML: (Worldwide)": [78],
                "CSV: (Worldwide)": [0.5],
            },
            "2006": {
                "XML: (Worldwide)": [65, 66],
                "CSV: (Worldwide)": [9, 10],
            }
        }
        self.assertListEqual(d.keys(), correct_d.keys())
        for y in d.keys():
            for h in d[y].keys():
                self.assertListEqual(d[y][h], correct_d[y][h])

    def test_aggregate(self):
        self.maxDiff = None
        d = gtrends.squeeze("tests/gtrends1.csv")
        d = gtrends.aggregate(d)
        correct_d = {
            "2004": {
                "XML: (Worldwide)": 96.5,
                "CSV: (Worldwide)": 5.75,
            },
            "2005": {
                "XML: (Worldwide)": 78,
                "CSV: (Worldwide)": 0.5,
            },
            "2006": {
                "XML: (Worldwide)": 65.5,
                "CSV: (Worldwide)": 9.5,
            }
        }
        self.assertDictEqual(d, correct_d)
