import sys

numbers = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10:"dez",
    11:"onze",
    12:"doze",
    13:"treze",
    14:"quatorze",
    15:"quinze",
    16:"dezesseis",
    17:"dezessete",
    18:"dezoito",
    19:"dezenove",
    20:"vinte",
    30:"trinta",
    40:"quarenta",
    50:"cinquenta",
    60:"sessenta",
    70:"setenta",
    80:"oitenta",
    90:"noventa",
    100:"cem",
    200:"duzentos",
    300:"trezentos",
    400:"quatrocentos",
    500:"quinhentos",
    600:"seiscentos",
    700:"setecentos",
    800:"oitocentos",
    900:"novecentos",
    1000:"mil"
}

def convert_to_suported(num):
    number = str(num)
    return number.zfill(6)

def separate_by_conversion_rule(str_num):
    return [int(str_num[:3]), int(str_num[3]), int(str_num[4:])]

def ten_unity_to_word(ten_unity_number, concat=False):
    if ten_unity_number <= 20:
        return numbers[ten_unity_number]
    ten_unity_str = str(ten_unity_number)
    ten = int(ten_unity_str[0]) * 10
    unity = int(ten_unity_str[1])
    return f"{numbers[ten]} e {numbers[unity]}" if unity > 0 else numbers[ten]

def hundred_to_word(hundred_number, concat):
    if hundred_number == 1 and concat:
        return "cento e "
    return numbers[hundred_number * 100] + " e " if concat else numbers[hundred_number * 100]

def thousand_to_word(thousand_number, concat):
    if thousand_number > 1:
        thousand_str = convert_to_word(thousand_number)
        return f"{thousand_str} mil " if concat else f"{thousand_str} mil"
    else:
        return f"{numbers[1000]} " if concat else numbers[1000]

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
    converted_number = convert_to_suported(number)
    separated_number = separate_by_conversion_rule(converted_number)
    thousand = separated_number[0]
    hundred = separated_number[1]
    ten_unity = separated_number[2]
    thousand_word = thousand_to_word(thousand, check_concat(hundred + ten_unity)) if thousand != 0 else numbers[0]
    hundred_word = hundred_to_word(hundred, check_concat(ten_unity)) if hundred != 0 else numbers[0]
    ten_unity_word = ten_unity_to_word(ten_unity) if ten_unity != 0 else numbers[0]
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