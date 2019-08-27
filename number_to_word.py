import sys
from numbers_dict import numbers

class NumberNotSupported(Exception):
    pass


def convert_to_current_limit(num):
    number = str(num)
    if len(number) > 6:
        raise NumberNotSupported(f"{num} out of current suported range (0 - 999999)")
    return number.zfill(6)

def separate_by_conversion_rule(str_num):
    return [int(str_num[:3]), int(str_num[3]), int(str_num[4:])]

def correct_determiner(word, concat, determiner=" e "):
    return word + determiner if (concat and word != numbers[0]) else word

def ten_unity_to_word(ten_unity_number, concat=False):
    if ten_unity_number <= 20:
        return numbers[ten_unity_number]

    ten_unity_str = str(ten_unity_number)
    ten = int(ten_unity_str[0]) * 10
    unity = int(ten_unity_str[1])
    return correct_determiner(numbers[ten], unity>0, f" e {numbers[unity]}")

def hundred_to_word(hundred_number, concat):
    if hundred_number == 1 and concat:
        return "cento e "

    return correct_determiner(numbers[hundred_number * 100], concat)

def thousand_to_word(thousand_number, concat):
    if thousand_number > 1:
        thousand_str = convert_to_word(thousand_number)
        return correct_determiner(thousand_str + " mil", concat, " ")

    else:
        return correct_determiner(numbers[thousand_number * 1000], concat, " ")

def check_concat(number):
    return number > 0

def remove_zeros(word_list):
    if len(word_list) > 1:
        if "zero" in word_list[0]:
            return remove_zeros(word_list[1:])

        if "zero" in word_list[-1]:
            return remove_zeros(word_list[:-1])

    return word_list

def convert_to_word(number):
    converted_number = convert_to_current_limit(number)
    thousand, hundred, ten_unity = separate_by_conversion_rule(converted_number)
    thousand_word = thousand_to_word(thousand, check_concat(hundred + ten_unity))
    hundred_word = hundred_to_word(hundred, check_concat(ten_unity))
    ten_unity_word = ten_unity_to_word(ten_unity)
    word_no_extra_zeros = remove_zeros([thousand_word, hundred_word, ten_unity_word])
    return "".join(word_no_extra_zeros)

def main():
    if len(sys.argv) != 2:
        print("Usage: number_in_word.py number")
        sys.exit(-1)
    
    else:
        number = sys.argv[1]
        print(convert_to_word(number))
        sys.exit(0)

if __name__ == "__main__":
    main()