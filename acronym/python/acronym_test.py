import unittest
from acronym import acronymize

class TestAcronym(unittest.TestCase):
    def test_acronym_with_spaces(self):
        self.assertEqual(acronymize('Portable Network Graphics'), 'PNG')
        
    def test_acronym_with_hyphen(self):
        self.assertEqual(acronymize('Liquid-crystal display'), 'LCD')
        
    def test_acronym_with_other_punctuation(self):
        self.assertEqual(acronymize("Thank George It's Friday!"), 'TGIF')
        
if __name__ == '__main__':
    unittest.main()