import re
import itertools
import random

def validate_rut(rut):
    clean_rut = re.sub("[^0-9kK-]", "", rut)
    if not __validate_rut_format(rut):
        raise Exception
    splited_rut = clean_rut.split("-")
    return splited_rut[1].upper() == __get_verification_digit_from_rut(splited_rut[0])

def get_random_rut():
    rut=str(random.randint(0, 25000000))
    return rut+"-"+__get_verification_digit_from_rut(rut)

def get_random_ruts(number_of_ruts):
    ruts = []
    for i in range(0, number_of_ruts):
        ruts.append(get_random_rut())
    return ruts
    
def __get_verification_digit_from_rut(rut):
    number_sum = 0
    inv_rut = rut[::-1]
    coefficents = itertools.cycle(range(2,8))
    for number in inv_rut:
        number_sum += next(coefficents) * int(number)
    verification_digit = 11 - (number_sum % 11)
    return __get_verification_digit_from_int(verification_digit)

def __get_verification_digit_from_int(value):
    if value == 11: return str(0)
    elif value == 10: return "K"
    else: return str(value)

def __validate_rut_format(rut):
    search_start = re.search("^[0-9]",rut)
    search_finish = re.search("-[0-9kK]$", rut)
    search_score = re.search("-{1}", rut)
    return search_start and search_score and search_finish