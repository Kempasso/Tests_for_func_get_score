import unittest

from score import get_score


class TestGetScore(unittest.TestCase):
    def test_offset_is_not_negative(self):
        self.assertEqual(get_score([{'offset': 9, 'score': {'away': 0, 'home': 0}}], -1), 'Offset меньше 0')

    def test_offset_is_not_int(self):
        self.assertEqual(get_score([{'offset': 9, 'score': {'away': 0, 'home': 0}}], 'string'), 'Неверный тип данных')

    def test_array_is_not_empty(self):
        for i in [[], ()]:
            self.assertEqual(get_score(i, 5), 'Массив не содержит данных')

    def test_find_true_value(self):
        self.assertEqual(get_score([{'offset': 9, 'score': {'away': 1, 'home': 2}}], 9), '1 : 2')

    def test_match_array(self):
        array_templates = [[{'offset': 9}],
                          [{'of': 9, 'score': {'away': 1, 'home': 2}}],
                          [{'offset': 9, 'score': {'home': 2}}],
                          [{'offset': 9, 's': {'away': 1, 'home': 2}}]]
        for array_template in array_templates:
            self.assertEqual(get_score(array_template, 9), 'Неправильная структура массива')




    def test_value_not_in_array(self):
        self.assertEqual(get_score([{'offset': 9, 'score': {'away': 1, 'home': 2}},
                                    {'offset': 11, 'score': {'away': 3, 'home': 2}}]), 'Offset не обнаружен')

    # @patch(score.game_stamps)
    # def test_no_value(self):
    #     self.assertEqual('Такого индекса нет', get_score(values, 5))
    #
    # @patch(score.game_stamps)
    # def test_wrong_value_type(self):
    #     self.assertEqual('Неверное значение', get_score(1, 2))
    #
    # @patch(score.game_stamps)
    # def test_wrong_list(self):
    #     self.assertEqual('Неверное значение', get_score([], 3))
