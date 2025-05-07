# -*- coding: utf-8 -*-

import re
from typing import Optional, Tuple

# UK Postcode validation regex. Does not include special cases.
POSTCODE_REGEX = re.compile(
    r'^((GIR0AA)|((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|(([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9]['
    r'ABEHMNPRV-Y])))[0-9][ABD-HJLNP-UW-Z]{2}))$'
)

# Using a set for special postcode verification. No need to make the regex any more complex
SPECIAL_POSTCODE_CASES = frozenset((
    'ASCN1ZZ', 'BBND1ZZ', 'BIQQ1ZZ', 'FIQQ1ZZ', 'GX111AA', 'PCRN1ZZ',
    'SIQQ1ZZ', 'STHL1ZZ', 'TDCU1ZZ', 'TKCA1ZZ', 'AI2640'
))


def _validate_input(postcode: str) -> None:
    """
    Validate that the input is a non-empty string
    """
    if not isinstance(postcode, str):
        raise ValueError("Postcode must be of type string")

    if not bool(postcode and not postcode.isspace()):
        raise ValueError("Postcode cannot be empty")


def normalize(postcode: str) -> str:
    """
    Normalize the postcode
    Strips all non-alphanumeric chars, leading and trailing whitespaces, tabs and spaces
    """
    _validate_input(postcode)
    clean_postcode = re.sub(r'[^a-zA-Z0-9]', '', postcode)
    return clean_postcode.upper()


def is_valid(postcode: str) -> bool:
    """
    Validate the postcode in accordance to the UK postcode formatting
    """
    normalized_postcode = normalize(postcode)
    if normalized_postcode in SPECIAL_POSTCODE_CASES:
        """
        Verify if postcode belongs to special cases as regex does not check for these
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases
        """
        return True

    return bool(POSTCODE_REGEX.match(normalized_postcode))


def _validate_and_normalize(postcode: str) -> Tuple[str, bool]:
    """
    Helper function to validate and normalize a postcode
    """
    normalized = normalize(postcode)
    valid = is_valid(postcode)

    if not valid:
        raise ValueError(f"Invalid postcode: {postcode}")

    return normalized, valid


def format_postcode(postcode: str) -> str:
    """
    Normalize, validate and format the postcode into standard UK postcode formatting
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    return f"{normalized_postcode[:-3]} {normalized_postcode[-3:]}"


def get_inward_code(postcode: str) -> str:
    """
    Return the inward code of the postcode
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    return normalized_postcode[-3:]


def get_outward_code(postcode: str) -> str:
    """
    Return the outward code of the postcode
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    return normalized_postcode[:-3]


def get_postcode_unit(postcode: str) -> str:
    """
    Return postcode unit of a valid postcode
    This consists of the last 2 characters of the inward portion
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    return normalized_postcode[-2:]


def get_postcode_sector(postcode: str) -> str:
    """
    Return postcode sector of a valid postcode
    This consists of the first character of the inward portion of the postcode
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    return normalized_postcode[-3]


def get_postcode_area(postcode: str) -> str:
    """
    Return the postcode area of a valid postcode
    This consists of the first 1-2 characters of the outward code.
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)

    if len(normalized_postcode) >= 2 and normalized_postcode[1].isalpha():
        return normalized_postcode[:2]

    return normalized_postcode[:1]


def get_postcode_district(postcode: str) -> str:
    """
    Return the postcode district of the postcode
    This is the last 1-3 characters of the outward code of the postcode
    """
    normalized_postcode, _ = _validate_and_normalize(postcode)
    outward = normalized_postcode[:-3]
    area = get_postcode_area(normalized_postcode)
    return outward[len(area):]
