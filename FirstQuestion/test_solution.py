import unittest
from letter_distribution import solution  # Updated import statement

class TestSolution(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(solution(1), 'a')
        self.assertEqual(solution(3), 'abc')
        self.assertEqual(solution(5), 'abcde')

    def test_large_values(self):
        self.assertEqual(solution(26), 'abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(solution(30), 'abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz')

    def test_divisible_values(self):
        self.assertEqual(solution(52), 'abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy')
        self.assertEqual(solution(60), 'abcdefghijklmnopqrstuvwxyzaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz')

if __name__ == '__main__':
    unittest.main()
