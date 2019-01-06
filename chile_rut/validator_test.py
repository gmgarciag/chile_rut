import unittest
import chile_rut
import itertools

class TestValidator(unittest.TestCase):

    def test_validate_ok(self):
        correct_ruts = ["6265837-1", "23289335-4", "21777921-9", "19442199-0", "23288541-6", "12194486-3", "12870299-7",
                        "6465375-k", "17268390-8", "8755721-9", "6034070-6", "5522858-2", "14420680-0", "16409917-2",
                        "13995949-3", "14194957-8", "10800123-2", "18475855-5", "13311020-8", "11746715-5"]
        for rut in correct_ruts:
            self.assertTrue(chile_rut.validate_rut(rut))

        validator_digit = ["0","1","2","3","4","5","6","7","8","9","k"]
        validator_digit = itertools.cycle(validator_digit)
        for rut in correct_ruts:
            next_digit = next(validator_digit)
            if rut[-1:] == str(next_digit):
                next_digit = next(validator_digit)
            self.assertFalse(chile_rut.validate_rut(rut[:-1]+str(next_digit)))

    def test_random_ok(self):
      for rut in chile_rut.random_ruts(1000):
            self.assertTrue(chile_rut.validate_rut(rut))

    def test_format(self):
        correct_ruts = [("7-1","7-1"),("35-4","35-4"),("921-9","921-9"),("4199-0", "4.199-0"),
                        ("88541-6","88.541-6"),("194486-3", "194.486-3"),("1287299-7","1.287.299-7"),
                        ("1345678-9", ("1.345.678-9")),("12345678-9",("12.345.678-9")),
                        ("123456789-9",("123.456.789-9")),("1123456789-9", ("1.123.456.789-9"))]
        for rut in correct_ruts:
            self.assertTrue(chile_rut.format_rut(rut[0])==rut[1])

    def test_verification_digit_ok(self):
        correct_ruts = ["6265837-1", "23289335-4", "21777921-9", "19442199-0", "23288541-6", "12194486-3", "12870299-7",
                        "6465375-k", "17268390-8", "8755721-9", "6034070-6", "5522858-2", "14420680-0", "16409917-2",
                        "13995949-3", "14194957-8", "10800123-2", "18475855-5", "13311020-8", "11746715-5"]
        for rut in correct_ruts:
            self.assertTrue(chile_rut.verification_digit(rut[:-2]) == rut[-1:].upper())

if __name__ == '__main__':
    unittest.main()