import unittest
from trivia import ScoreMonad

class TestScoreMonad(unittest.TestCase):

    def test_initial_score(self):
        score = ScoreMonad(0)
        self.assertEqual(score.score, 0)

    def test_add_scores(self):
        score1 = ScoreMonad(10)
        score2 = ScoreMonad(20)
        result = score1 + score2
        self.assertEqual(result.score, 30)

    def test_add_integer(self):
        score = ScoreMonad(10)
        result = score + 5
        self.assertEqual(result.score, 15)

    def test_bind_function(self):
        score = ScoreMonad(10)
        result = score.bind(lambda x: ScoreMonad(x + 5))
        self.assertEqual(result.score, 15)

    def test_unit_method(self):
        score = ScoreMonad.unit(10)
        self.assertEqual(score.score, 10)

    def test_str_method(self):
        score = ScoreMonad(10)
        self.assertEqual(str(score), "Puntaje: 10")

if __name__ == '__main__':
    unittest.main()