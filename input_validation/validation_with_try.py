"""
Author: Brady Trenary
Program: validation_with_try.py
Date: 9/20/2020
"""

NUMBER_TESTS = 3


def average(score1, score2, score3):
    result = float((score1 + score2 + score3) / NUMBER_TESTS)
    if score1 < 0 or score2 < 0 or score3 <0:
        raise ValueError
    return result


if __name__ == '__main__':
    average_scores = average(10, 90, 100)
    last_name = input('Enter your last name: ')
    first_name = input('Enter your first name: ')
    age = input('Enter your age: ')

    print(f'{last_name}, {first_name} age:{age} average grade: {average_scores}')
