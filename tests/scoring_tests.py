from gym_yahtzee.scoring import (
    score_upper_section,
    score_x_of_a_kind,
    score_full_house,
    score_small_straight,
    score_large_straight,
    score_yahtzee,
    score_chance,

)
from unittest import TestCase


class RulesScoreTestCase(TestCase):
    def test_score_upper_section(self):
        self.assertEqual(score_upper_section([1, 1, 1, 2, 3], face=1), 3)
        self.assertEqual(score_upper_section([2, 1, 2, 2, 4], face=2), 6)
        self.assertEqual(score_upper_section([1, 1, 1, 2, 3], face=6), 0)

    def test_score_three_of_a_kind(self):
        self.assertEqual(score_x_of_a_kind([1, 1, 1, 2, 2], min_same_faces=3), 3)
        self.assertEqual(score_x_of_a_kind([2, 2, 2, 3, 2], min_same_faces=3), 6)
        self.assertEqual(score_x_of_a_kind([1, 2, 2, 3, 6], min_same_faces=3), 0)
        self.assertEqual(score_x_of_a_kind([6, 6, 6, 6, 6], min_same_faces=3), 18)

    def test_score_four_of_a_kind(self):
        self.assertEqual(score_x_of_a_kind([1, 1, 1, 2, 1], 4), 4)
        self.assertEqual(score_x_of_a_kind([2, 2, 2, 3, 2], 4), 8)
        self.assertEqual(score_x_of_a_kind([1, 2, 2, 3, 6], 4), 0)
        self.assertEqual(score_x_of_a_kind([6, 6, 6, 6, 6], 4), 24)

    def test_score_full_house(self):
        self.assertEqual(score_full_house([1, 1, 1, 2, 2]), 7)
        self.assertEqual(score_full_house([1, 1, 1, 2, 3]), 0)

    def test_score_small_straight(self):
        self.assertEqual(score_small_straight([1, 3, 2, 5, 4]), 30)
        self.assertEqual(score_small_straight([6, 3, 5, 4, 1]), 30)
        self.assertEqual(score_small_straight([2, 3, 5, 4, 2]), 30)
        self.assertEqual(score_small_straight([1, 1, 1, 1, 1]), 0)
        self.assertEqual(score_small_straight([1, 2, 3, 5, 4]), 30)

    def test_score_large_straight(self):
        self.assertEqual(score_large_straight([1, 3, 2, 5, 4]), 40)
        self.assertEqual(score_large_straight([6, 3, 5, 4, 2]), 40)
        self.assertEqual(score_large_straight([2, 3, 5, 4, 2]), 0)
        self.assertEqual(score_large_straight([1, 1, 1, 1, 1]), 0)

    def test_score_yahtzee(self):
        self.assertEqual(score_yahtzee([1, 1, 1, 1, 1]), 50)
        self.assertEqual(score_yahtzee([2, 2, 2, 3, 2]), 0)
        self.assertEqual(score_yahtzee([6, 6, 6, 6, 6]), 50)

    def test_score_chance(self):
        self.assertEqual(score_chance([1, 1, 1, 1, 1]), 5)
        self.assertEqual(score_chance([6, 6, 6, 6, 6]), 30)
        self.assertEqual(score_chance([1, 2, 3, 4, 5]), 15)
