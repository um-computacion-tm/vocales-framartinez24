import unittest


def vocal_counter(word: str) -> dict:
    vocales = {}
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            vocales[letter] = 1 + vocales.get(letter, 0)
    return vocales

def vocal_counter_des(word: str):
    result = vocal_counter(word)
    return \
        result.get('a', 0), \
        result.get('e', 0), \
        result.get('i', 0), \
        result.get('o', 0), \
        result.get('u', 0)


class TestVowels(unittest.TestCase):

    def test_case_1(self):
        expected = {
            'a': 5,
            'e': 1,
            'u': 1,
        }
        result = vocal_counter("aca hay una frase")
        self.assertDictEqual(result, expected)
    
    def test_case_1_2(self):
        expected = {
            'a': 3,
            'e': 4,
            'i' : 1,
            'o' : 1


        }
        result = vocal_counter("con menem me hice la casa")
        self.assertDictEqual(result, expected)

    def test_case_2(self):
        ca, ce, ci, co, cu = vocal_counter_des("ursula")
        result = (ca, ce, ci, co, cu)
        self.assertEqual(result, (1, 0, 0, 0, 2))

    def test_case_3(self):
        ca, ce, ci, co, cu = vocal_counter_des("lamebotas")
        result = (ca, ce, ci, co, cu)
        self.assertEqual(result, (2, 1, 0, 1, 0))

if __name__ == '__main__':
    unittest.main()