# -*- coding: utf-8 -*-

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
    def test_is_valid_postcode(self):
        """Tests for is_valid on valid format postcodes"""
        self.assertTrue(is_valid("EC1A 1BB"))  # Standard format UK postcode
        self.assertTrue(is_valid("ai2640"))  # Special case UK postcode
        self.assertTrue(is_valid("bfpo57"))  # BFPO postcode
        self.assertTrue(is_valid("ky1-1234"))  # Numeric overseas postcode
        self.assertTrue(is_valid("bx1 1lt"))  # Non-geographic postcode

    def test_is_valid_invalid_postcodes(self):
        """Tests for is_valid on invalid format postcodes"""
        self.assertFalse(is_valid("Y35 E5W4"))  # Non UK format
        self.assertFalse(is_valid("12345"))  # Random string
        self.assertFalse(is_valid("abcd efg"))  # Incorrect characters
        self.assertFalse(is_valid("sw1a1a"))  # Too short
        self.assertFalse(is_valid("z1z 1zz"))  # Invalid area code

    def test_is_valid_non_string(self):
        """Test invalid postcode types"""
        invalid_postcode_types = {None, 12345, 1.1}
        for postcode in invalid_postcode_types:
            with self.assertRaises(ValueError, msg=f"Type {type(postcode)} should raise ValueError"):
                is_valid(postcode)

    def test_is_valid_empty_postcode(self):
        """Test empty or white-space only postcodes"""
        empty_postcodes = {"", " ", "\t", "\n"}
        for postcode in empty_postcodes:
            with self.assertRaises(ValueError, msg=f"Empty postcode should raise ValueError"):
                is_valid(postcode)

    # Tests for format_postcode

    def test_format_postcode_valid(self):
        """Tests for format_postcode on valid postcodes"""
        self.assertEqual(format_postcode("ec1a1bb"), "EC1A 1BB")  # Standard format UK postcode
        self.assertEqual(format_postcode("ai2640"), "AI-2640")  # Special case UK postcode
        self.assertEqual(format_postcode("bfp o57"), "BFPO 57")  # BFPO postcode
        self.assertEqual(format_postcode("bfp o1234"), "BFPO 1234")  # BFPO postcode
        self.assertEqual(format_postcode("kY1 1234"), "KY1-1234")  # Numeric overseas postcode
        self.assertEqual(format_postcode("bx 11lt"), "BX1 1LT")  # Non-geographic postcode

    def test_format_postcode_invalid(self):
        """Tests for format_postcode on invalid postcodes"""
        invalid_postcodes = {
            "y35 E5W4",  # Non Uk format
            "12345",  # Random string
            "abcd efg",  # Invalid characters
            "sw1a1a",  # Too short
            "z1z 1zz"  # Invalid area code
        }

        for postcode in invalid_postcodes:
            with self.assertRaises(ValueError, msg=f"Invalid postcode {postcode} should raise ValueError"):
                format_postcode(postcode)

    # Tests for extracting components from postcodes

    def test_component_extraction_valid(self):
        test_cases = [
            ('SW1W 0NY', {'area': 'SW', 'district': '1W', 'sector': '0', 'unit': 'NY', 'inward': '0NY', 'outward': 'SW1W'}),
            ('BF1 0AB', {'area': 'BF', 'district': '1', 'sector': '0', 'unit': 'AB', 'inward': '0AB', 'outward': 'BF1'}),
        ]

        for postcode, expected_output in test_cases:
            self.assertEqual(get_postcode_area(postcode), expected_output['area'])
            self.assertEqual(get_postcode_district(postcode), expected_output['district'])
            self.assertEqual(get_postcode_sector(postcode), expected_output['sector'])
            self.assertEqual(get_postcode_unit(postcode), expected_output['unit'])
            self.assertEqual(get_inward_code(postcode), expected_output['inward'])
            self.assertEqual(get_outward_code(postcode), expected_output['outward'])


if __name__ == "__main__":
    unittest.main()
