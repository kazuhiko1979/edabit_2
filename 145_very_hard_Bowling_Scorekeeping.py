"""
Bowling Scorekeeping
Tenpin bowling scores can range from 0 (all gutter balls) to 300 (a perfect game). If you are unfamiliar with scorekeeping, please see the Resources tab for a quick description.

A complete record of a 10 frame bowling game can be given as a list of the number of pins knocked down by each ball in sequence from the beginning to the end of the game.

Create a function whose argument is such a list. The function should return the final score.

Examples
bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) ➞ 300

bowling([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) ➞ 80

bowling([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) ➞ 150

bowling([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) ➞ 200
Notes
The number of balls thrown for a complete game can vary from 12 to 21 depending on the number of strikes and spares thrown.
"""


def calculate_bowling_score(rolls):
    total_score = 0
    roll_index = 0
    frame = 1
    while frame <= 10:  # 10フレームまで繰り返す
        if rolls[roll_index] == 10:  # ストライクの場合
            total_score += 10
            total_score += sum(rolls[roll_index + 1:roll_index + 3])
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # スペアの場合
            total_score += 10
            total_score += rolls[roll_index + 2]
            roll_index += 2
        else:  # それ以外（オープンフレーム）
            total_score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2

        frame += 1

    return total_score


# テストケースの実行
print(calculate_bowling_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # ➞ 300
print(calculate_bowling_score([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))  # ➞ 80
print(calculate_bowling_score([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))  # ➞ 150
print(calculate_bowling_score([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]))  # ➞ 200
print(calculate_bowling_score([10, 0, 10, 7, 2, 10, 10, 10, 8, 2, 9, 1, 7, 2, 10, 10, 5]))  # ➞ 194
print(calculate_bowling_score([8, 0, 8, 2, 10, 10, 7, 3, 9, 1, 7, 2, 10, 10, 9, 0]))  # ➞ 177
