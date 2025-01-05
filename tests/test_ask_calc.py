from core import AskCalc
import unittest


class TestAskCalc(unittest.TestCase):
    def test_by_age(self):
        test_ages = [
            {'age': 44, 'result': 0},
            {'age': 45, 'result': 2},
            {'age': 53, 'result': 2},
            {'age': 55, 'result': 3},
            {'age': 64, 'result': 3},
            {'age': 65, 'result': 4},
        ]

        for case in test_ages:
            with self.subTest(age=case['age'], result=case['result']):
                result = AskCalc.by_age(case['age'])
                self.assertEqual(result, case['result'])

    def test_by_imc(self):
        test_imcs = [
            {'imc': 24, 'result': 0},
            {'imc': 26, 'result': 1},
            {'imc': 30, 'result': 1},
            {'imc': 31, 'result': 3},
        ]

        for case in test_imcs:
            with self.subTest(imc=case['imc'], result=case['result']):
                result = AskCalc.by_imc(case['imc'])
                self.assertEqual(result, case['result'])

    def test_by_abdominal_perimeter(self):
        test_abdominal_perimeters = [
            {'sex': 'Masculino', 'abdominal_perimeter': 93, 'result': 0},
            {'sex': 'Masculino', 'abdominal_perimeter': 94, 'result': 3},
            {'sex': 'Masculino', 'abdominal_perimeter': 102, 'result': 3},
            {'sex': 'Masculino', 'abdominal_perimeter': 103, 'result': 4},
            {'sex': 'Femenino', 'abdominal_perimeter': 79, 'result': 0},
            {'sex': 'Femenino', 'abdominal_perimeter': 80, 'result': 3},
            {'sex': 'Femenino', 'abdominal_perimeter': 88, 'result': 3},
            {'sex': 'Femenino', 'abdominal_perimeter': 89, 'result': 4}
        ]

        for case in test_abdominal_perimeters:
            with self.subTest(sex=case['sex'], abdominal_perimeter=case['abdominal_perimeter'], result=case['result']):
                result = AskCalc.by_abdominal_perimeter(case['abdominal_perimeter'], case['sex'])
                self.assertEqual(result, case['result'])

    def test_by_ask_one(self):
        test_ask_one = [
            {'ask': 'Si', 'result': 0},
            {'ask': 'No', 'result': 2}
        ]

        for case in test_ask_one:
            with self.subTest(ask=case['ask'], result=case['result']):
                result = AskCalc.by_ask_one(case['ask'])
                self.assertEqual(result, case['result'])

    def test_by_ask_two(self):
        test_ask_two = [
            {'ask': 'A diario', 'result': 0},
            {'ask': 'No a diario', 'result': 1}
        ]

        for case in test_ask_two:
            with self.subTest(ask=case['ask'], result=case['result']):
                result = AskCalc.by_ask_two(case['ask'])
                self.assertEqual(result, case['result'])

    def test_by_ask_three(self):
        test_ask_three = [
            {'ask': 'Si', 'result': 2},
            {'ask': 'No', 'result': 0}
        ]

        for case in test_ask_three:
            with self.subTest(ask=case['ask'], result=case['result']):
                result = AskCalc.by_ask_three(case['ask'])
                self.assertEqual(result, case['result'])

    def test_by_ask_four(self):
        test_ask_four = [
            {'ask': 'Si', 'result': 5},
            {'ask': 'No', 'result': 0}
        ]

        for case in test_ask_four:
            with self.subTest(ask=case['ask'], result=case['result']):
                result = AskCalc.by_ask_four(case['ask'])
                self.assertEqual(result, case['result'])

    def test_by_ask_five(self):
        test_ask_five = [
            {'ask': 'Si: Padres, hermano o hijos', 'result': 5},
            {'ask': 'No', 'result': 0}
        ]

        for case in test_ask_five:
            with self.subTest(ask=case['ask'], result=case['result']):
                result = AskCalc.by_ask_five(case['ask'])
                self.assertEqual(result, case['result'])
