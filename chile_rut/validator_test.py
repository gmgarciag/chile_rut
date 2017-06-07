import unittest
import chile_rut

class TestValidator(unittest.TestCase):

    def test_ok(self):
        self.assertTrue(chile_rut.validate_rut("0-0"))
        self.assertTrue(chile_rut.validate_rut("18023503-5"))
        self.assertFalse(chile_rut.validate_rut("0-1"))
        self.assertFalse(chile_rut.validate_rut("18023503-K"))
        self.assertTrue(chile_rut.validate_rut("18711487-K"))

if __name__ == '__main__':
    unittest.main()