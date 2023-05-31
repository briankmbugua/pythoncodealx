#!/usr/bin/python3.9
def get_formatted_name(first, last, middle=''):
    """Generate a fully formatted name"""

    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
