import unittest
from ukpostcode import (
    is_valid,
    format_postcode,
    get_inward_code,
    get_outward_code,
    get_postcode_unit,
    get_postcode_sector,
    get_postcode_area,
    get_postcode_district
)


class TestUKPostcodeLibrary(unittest.TestCase):

    # Tests for is_valid

    def test_is_valid_standard_cases(self):
        """
        Test standard valid UK Postcodes
        """
        valid_postcodes = {
            "EC1A 1BB",
            "w1a0ax",
            "m11AE",
            "b33 8TH",
            "CR26XH",
            "DN551pt",
            "GIR0AA",
        }

        for postcode in valid_postcodes:
            self.assertTrue(is_valid(postcode), f"Postcode {postcode} should be valid")

    def test_is_valid_special_cases(self):
        """
        Test special postcode cases
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases
        """
        special_cases = {
            'ASCN 1ZZ',
            'BBND 1ZZ',
            'BIQQ 1ZZ',
            'FIQQ 1ZZ',
            'GX11 1AA',
            'PCRN 1ZZ',
            'SIQQ 1ZZ',
            'STHL 1ZZ',
            'TDCU 1ZZ',
            'TKCA 1ZZ',
            'AI-2640'
        }

        for postcode in special_cases:
            self.assertTrue(is_valid(postcode), f"Special postcode {postcode} should be valid")

    def test_is_valid_invalid_postcodes(self):
        """Test invalid postcode formats"""
        invalid_postcodes = {
            "Y35 E5W4",  # Non-UK format
            "12345",  # Random string
            "ABCD EFG",  # Incorrect characters
            "SW1A 1A",  # Too short
            "Z1Z 1ZZ",  # Invalid area code
            "Q1Z 1ZZ",  # Invalid area code
        }
        for postcode in invalid_postcodes:
            self.assertFalse(is_valid(postcode), f"Postcode {postcode} should be invalid")

    def test_is_valid_non_string(self):
        """Test invalid postcode types"""
        invalid_postcode_types = {
            None,
            12345,
            1.1
        }

        for postcode in invalid_postcode_types:
            with self.assertRaises(ValueError, msg=f"Type {type(postcode)} should raise ValueError"):
                is_valid(postcode)

    def test_empty_postcode(self):
        """Test empty or white-space only postcodes"""
        empty_postcodes = {"", " ", "\t", "\n"}

        for postcode in empty_postcodes:
            with self.assertRaises(ValueError, msg=f"Empty postcode should raise ValueError"):
                is_valid(postcode)

    # Test for format_postcode

    def test_format_postcode_valid(self):
        """Test if valid postcodes are formatted correctly"""
        test_postcodes = [
            ("ec1a1bb", "EC1A 1BB"),
            ("W1A0AX", "W1A 0AX"),
            ("M11AE", "M1 1AE")
        ]

        for input_postcode, expected_output in test_postcodes:
            self.assertEqual(format_postcode(input_postcode), expected_output,
                             f"Formatting {input_postcode} should result in {expected_output}")

    def test_format_postcode_invalid(self):
        """Test formatting for invalid postcodes"""
        invalid_postcodes = {
            "INVALID",
            "123",
            ""
        }

        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                format_postcode(postcode)

    # Test for get_inward_code

    def test_get_inward_code_valid(self):
        """Test retrieving inward code for valid format postcodes"""
        test_cases = [
            ("EC1A1BB", "1BB"),
            ("W1A0AX", "0AX"),
            ("M11AE", "1AE")
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_inward_code(input_postcode), expected_output,
                             f"Inward code of {input_postcode} should be {expected_output}")

    def test_get_inward_code_invalid(self):
        """Test retrieving inward code for invalid format postcodes"""
        test_postcodes = {
            "INVALID",
            "123",
            ""
        }

        for postcode in test_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_inward_code(postcode)

    # Tests for get_outward_code

    def test_get_outward_code_valid(self):
        """Test retrieving outward code on valid format postcodes"""
        test_cases = [
            ("EC1A1BB", "EC1A"),
            ("W1A0AX", "W1A"),
            ("M11AE", "M1")
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_outward_code(input_postcode), expected_output,
                             f"Outward code of {input_postcode} should be {expected_output}")

    def test_get_outward_code_invalid(self):
        """Test retrieving outward code for invalid format postcodes"""
        test_postcodes = {
            "INVALID",
            "123",
            ""
        }

        for postcode in test_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_outward_code(postcode)

    # Tests for get_postcode_unit

    def test_get_postcode_unit_standard(self):
        """Test retrieving postcode unit for valid standard postcodes"""
        test_cases = [
            ("EC1A 1BB", "BB"),
            ("W1A 0AX", "AX"),
            ("M1 1AE", "AE"),
            ("B33 8TH", "TH"),
            ("GIR0AA", "AA"),
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_unit(input_postcode), expected_output,
                             f"Postcode unit of {input_postcode} should be {expected_output}")

    def test_get_postcode_unit_special(self):
        """Test retrieving postcode unit for special postcodes"""
        test_cases = [
            ("ASCN1ZZ", "ZZ"),
            ("BBND1ZZ", "ZZ"),
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_unit(input_postcode), expected_output,
                             f"Postcode unit of {input_postcode} should be {expected_output}")

    def test_get_postcode_unit_invalid(self):
        """Test retrieving postcode unit for invalid postcodes"""
        invalid_postcodes = {
            "INVALID", "123", "Z1Z 1ZZZ", ""
        }

        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_postcode_unit(postcode)

    # Test for get_postcode_sector

    def test_get_postcode_sector_standard(self):
        """Test retrieving postcode sector for valid standard postcodes"""
        test_cases = [
            ("EC1A 1BB", "1"),
            ("W1A 0AX", "0"),
            ("M1 1AE", "1"),
            ("B33 8TH", "8"),
            ("GIR0AA", "0"),
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_sector(input_postcode), expected_output,
                             f"Postcode sector of {input_postcode} should be {expected_output}")

    def test_get_postcode_sector_special(self):
        """Test retrieving postcode sector for special postcodes"""
        test_cases = [
            ("ASCN1ZZ", "1"),
            ("BBND1ZZ", "1"),
        ]

        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_sector(input_postcode), expected_output,
                             f"Postcode sector of {input_postcode} should be {expected_output}")

    def test_get_postcode_sector_invalid(self):
        """Test retrieving postcode sector for invalid postcodes"""
        invalid_postcodes = {"INVALID", "123", "Z1Z 1ZZ", ""}
        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_postcode_sector(postcode)

    # Tests for get_postcode_area

    def test_get_postcode_area_standard(self):
        """Test retrieving postcode area for valid standard postcodes"""
        test_cases = [
            ("EC1A 1BB", "EC"),
            ("W1A 0AX", "W"),
            ("M1 1AE", "M"),
            ("B33 8TH", "B"),
            ("GIR0AA", "GI"),
        ]
        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_area(input_postcode), expected_output,
                             f"Postcode area of {input_postcode} should be {expected_output}")

    def test_get_postcode_area_special(self):
        """Test retrieving postcode area for special postcodes"""
        test_cases = [
            ("ASCN1ZZ", "AS"),
            ("BBND1ZZ", "BB"),
        ]
        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_area(input_postcode), expected_output,
                             f"Postcode area of {input_postcode} should be {expected_output}")

    def test_get_postcode_area_invalid(self):
        """Test retrieving postcode area for invalid postcodes"""
        invalid_postcodes = {"INVALID", "123", "Z1Z 1ZZ", ""}
        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_postcode_area(postcode)

    # Tests for get_postcode_district

    def test_get_postcode_district_standard(self):
        """Test retrieving postcode district for valid standard postcodes"""
        test_cases = [
            ("EC1A 1BB", "1A"),
            ("W1A 0AX", "1A"),
            ("M1 1AE", "1"),
            ("B33 8TH", "33"),
            ("GIR0AA", "R"),
        ]
        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_district(input_postcode), expected_output,
                             f"Postcode district of {input_postcode} should be {expected_output}")

    def test_get_postcode_district_special(self):
        """Test retrieving postcode district for special postcodes"""
        test_cases = [
            ("ASCN1ZZ", "CN"),
            ("BBND1ZZ", "ND"),
        ]
        for input_postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_district(input_postcode), expected_output,
                             f"Postcode district of {input_postcode} should be {expected_output}")

    def test_get_postcode_district_invalid(self):
        """Test retrieving postcode district for invalid postcodes"""
        invalid_postcodes = ["INVALID", "123", "Z1Z 1ZZ", ""]
        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                get_postcode_district(postcode)


if __name__ == "__main__":
    unittest.main()
