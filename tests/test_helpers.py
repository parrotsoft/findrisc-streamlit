from helpers import imc
import unittest


class TestHelpers(unittest.TestCase):
    def test_imc(self):
        test_imc = [
            {'weight': 104, 'height': 175, 'result': 33.96},
            {'weight': 0, 'height': 0, 'result': 0}
        ]

        for case in test_imc:
            with self.subTest(weight=case['weight'], height=case['height'], result=case['result']):
                result = imc(case['weight'], case['height'])
                self.assertEqual(result, case['result'])


if __name__ == '__main__':
    unittest.main()
