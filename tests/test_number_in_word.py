import os
import sys
import pytest

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HERE, "../"))
import number_to_word

# TODO: finish testing
def test_correct_ten_unity_to_word():
    numbers = (0, 1, 10, 15, 20, 26, 40, 67, 99)
    word = ("zero", "um", "dez", "quinze", "vinte", "vinte e seis", "quarenta", "sessenta e sete", "noventa e nove")
    i = 0
    for number in numbers:
        assert number_to_word.ten_unity_to_word(number)
        i += 1

def test_correct_hundred_to_word():
    numbers = ((1, False), (1, True), (2, True), (5, True), (6, True))
    word = ("cem", "cento e ", "duzentos e ", "quinhentos e ", "seiscentos e ")
    i = 0
    for number in numbers:
        assert number_to_word.hundred_to_word(*number) == word[i]
        i += 1

def test_check_concat():
    numbers = (1, 5, 10, 14, 21, 56, 72)
    result = (False, False, False, True, True, True, True)
    i = 0
    for number in numbers:
        assert number_to_word.check_concat(number) == result[i]
        i += 1

def test_correct_thousand_to_word():
    numbers = ((1, False), (1, True), (5, True), (7, False), (10, True), (234, False), (999, True))
    word = ("mil", "mil e ", "cinco mil e ", "sete mil", "dez mil e ", "duzentos e trinta e quatro mil", "novecentos e noventa e nove mil e ")
    i = 0
    for number in numbers:
        assert number_to_word.thousand_to_word(*number) == word[i]
        i += 1
