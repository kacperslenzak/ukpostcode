# UK Postcode Library

A small python library for validating and formatting UK postcodes

This library uses only standard python libraries and carries no external dependencies.

The regex for the initial validation of the postcode format is the following:
`^((GIR0AA)|((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|(([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9]['
    r'ABEHMNPRV-Y])))[0-9][ABD-HJLNP-UW-Z]{2}))$`

There is also a further check against a set of special post codes that don't follow the standard format.
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases

## Usage

```python
from ukpostcode import is_valid, format_postcode, get_postcode_area

# Validate a postcode
if is_valid("W1A 1AA"):
    print("Valid postcode")

# Format a postcode
formatted = format_postcode("w1a1aa")  # Returns "W1A 1AA"

# Get postcode components
area = get_postcode_area("EC1A 1BB")  # Returns "EC"
```

## API Reference

### Validation

- `is_valid(postcode: str) -> bool`: Checks if a postcode is valid according to UK standards

### Formatting

- `format_postcode(postcode: str) -> str`: Formats a valid postcode to standard format (outward code + space + inward code)

### Postcode detail extraction

- `get_inward_code(postcode: str) -> str`: Returns the inward code (last 3 characters)
- `get_outward_code(postcode: str) -> str`: Returns the outward code (all characters except last 3)
- `get_postcode_unit(postcode: str) -> str`: Returns the postcode unit (last 2 characters)
- `get_postcode_sector(postcode: str) -> str`: Returns the postcode sector (3rd character from end)
- `get_postcode_area(postcode: str) -> str`: Returns the postcode area (first 1-2 characters)
- `get_postcode_district(postcode: str) -> str`: Returns the postcode district (characters after area but before inward code)

### Utilities

- `normalize(postcode: str) -> str`: Normalizes a postcode by removing spaces and non-alphanumeric characters and converting to uppercase

## Tests

To run the supplied tests:

```commandline
git clone https://github.com/kacperslenzak/ukpostcode.git
python -m unittest discover tests
```

Alternatively, run the test file directly

```commandline
python tests/test_ukpostcode.py
```