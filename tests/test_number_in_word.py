import os
import sys
import pytest

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HERE, "../"))
import number_to_word

def test_support_current_limit():
    limit = 999999
    assert "999999" == number_to_word.convert_to_current_limit(limit)

def test_raise_error_with_not_supported_number():
    number = 1e6
    with pytest.raises(number_to_word.NumberNotSupported):
        number_to_word.convert_to_current_limit(number)

def test_separated_rules():
    number = "000333"
    expected = [000, 3, 33]
    assert expected == number_to_word.separate_by_conversion_rule(number)

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
    numbers = (0, 1, 5, 10)
    result = (False, True, True, True)
    i = 0
    for number in numbers:
        assert number_to_word.check_concat(number) == result[i]
        i += 1

def test_correct_thousand_to_word():
    numbers = ((1, False), (1, True), (5, True), (7, False), (10, True), (234, False), (999, True))
    word = ("mil", "mil ", "cinco mil ", "sete mil", "dez mil ", "duzentos e trinta e quatro mil", "novecentos e noventa e nove mil ")
    i = 0
    for number in numbers:
        assert number_to_word.thousand_to_word(*number) == word[i]
        i += 1

def test_correct_complete_conversion():
    numbers = (100, 101, 302, 85484, 999654)
    word = ("cem", "cento e um", "trezentos e dois",
            "oitenta e cinco mil quatrocentos e oitenta e quatro",
            "novecentos e noventa e nove mil seiscentos e cinquenta e quatro")
    i = 0
    for number in numbers:
        assert number_to_word.convert_to_word(number) == word[i]
        i += 1
