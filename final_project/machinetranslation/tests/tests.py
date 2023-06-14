import unittest
from machinetranslation.translator import translateToFrench, translateToEnglish

class TranslationTests(unittest.TestCase):
    def test_englishToFrench_equal(self):
        english_text = 'Hello'
        french_text = translateToFrench(english_text)
        expected_result = 'Pepitoooo'
        self.assertEqual(french_text, expected_result)

    def test_englishToFrench_not_equal(self):
        english_text = 'Hello'
        french_text = translateToFrench(english_text)
        unexpected_result = 'Bonjour'
        self.assertNotEqual(french_text, unexpected_result)
    
    def test_frenchToEnglish_equal(self):
        french_text = 'Bonjour'
        english_text = translateToEnglish(french_text)
        expected_result = 'Hello'
        self.assertEqual(english_text, expected_result)

    def test_frenchToEnglish_not_equal(self):
        french_text = 'Bonjour'
        english_text = translateToEnglish(french_text)
        unexpected_result = 'Good Morning'
        self.assertNotEqual(english_text, unexpected_result)

if __name__ == "__main__":
    unittest.main()
