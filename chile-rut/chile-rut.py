import re
from itertools import *

def validate_rut(rut):
    number_sum = 0
    clean_rut = re.sub("[^0-9kK-]", "", rut)
    if not validate_rut_format(rut): return 1
    splited_rut = clean_rut.split("-")
    inv_rut = splited_rut[0][::-1]
    coefficents = cycle(range(2,8))
    for number in inv_rut:
        number_sum += next(coefficents) * int(number)
    verification_digit = 11 - (number_sum % 11)
    return splited_rut[1].upper() == get_verification_digit_from_int(verification_digit)

def get_verification_digit_from_int(value):
    if value == 11: return str(0)
    elif value == 10: return "K"
    else: return str(value)

def validate_rut_format(rut):
    search_start = re.search("^[0-9]",rut)
    search_finish = re.search("-[0-9kK]$", rut)
    search_score = re.search("-{1}", rut)
    return search_start and search_score and search_finish

if __name__ == "__main__":
    print validate_rut("18.023.503-5")
