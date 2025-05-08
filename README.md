# UK Postcode Library

A small python library for validating and formatting UK postcodes

This library uses only standard python libraries and carries no external dependencies.

The regex for the initial validation of the postcode format is the following:
`^((GIR0AA)|((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|(([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9]['
    r'ABEHMNPRV-Y])))[0-9][ABD-HJLNP-UW-Z]{2}))$`

The regex matches the formatting rules found here:
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

There is also a further check against a set of special post codes that don't follow the standard format.
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases

## Usage

```python
from ukpostcode import is_valid, format_postcode

# Validate a postcode
if is_valid("W1A 1AA"):
    print("Valid postcode")

# Format a postcode
formatted = format_postcode("w1a1aa")  # Returns "W1A 1AA"
```

## API Reference

### Validation

- `is_valid(postcode: str) -> bool`: Checks if a postcode is valid according to UK standards

### Formatting

- `format_postcode(postcode: str) -> str`: Formats a valid postcode to standard format (outward code + space + inward code)

### Postcode detail extraction

- `get_inward_code(postcode: str) -> str`: Returns the inward code (last 3 characters)
- `get_outward_code(postcode: str) -> str`: Returns the outward code (all characters except last 3)
- `get_postcode_unit(postcode: str) -> str or None`: Returns the postcode unit (last 2 characters)
- `get_postcode_sector(postcode: str) -> str or None`: Returns the postcode sector (3rd character from end)
- `get_postcode_area(postcode: str) -> str or None`: Returns the postcode area (first 1-2 characters)
- `get_postcode_district(postcode: str) -> str or None`: Returns the postcode district (characters after area but before inward code)

## Limitations

The library validates if postcodes match the current specified format of UK postcodes.
These postcodes change everyday. This library also does not validate if postcodes match a valid address.
This would have to be crossreferenced with a valid dataset of valid postcodes in the UK.

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