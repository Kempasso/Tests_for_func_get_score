import math
import random

TIMESTAMPS_COUNT = 20

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()
print(len(game_stamps))


# Вариант 1
def get_score(game_stamps, offset):
    if not isinstance(game_stamps, (list, tuple)) or not isinstance(offset, int):
        return 'Неверный тип данных'
    elif not len(game_stamps):
        return 'Массив не содержит данных'
    elif offset < 0:
        return 'Offset меньше 0'
    for index, stamp in enumerate(game_stamps):
        try:
            if stamp['offset'] == offset:
                result = game_stamps[index]['score']
                return f'{result["away"]} : {result["home"]}'
            else:
                return 'Offset не обнаружен'
        except KeyError:
            return 'Неправильная структура массива'


print(get_score(game_stamps, 9))
