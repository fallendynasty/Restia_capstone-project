import string as char
from typing import Any

valid_domain_char = char.ascii_letters + char.digits + '._-'
valid_user_char = valid_domain_char + '+'

def true(value=None) -> bool:
    # Always returns True
    return True

def false(value=None) -> bool:
    # Always returns False
    return False

def string(value: Any) -> bool:
    """
    Return
    - True if value is of type str
    - False otherwise
    """
    return type(value) == str

def number(value: Any) -> bool:
    if type(value) == int or type(value) == float:
        return True
    return False
    """
    Return
    - True if value is of type int or float
    - False otherwise
    """

def year(value: int) -> bool:
    """
    Return
    - True if value is between 1940 (exclusive) and 2040 (inclusive)
    - False otherwise
    """
    return True if value > 1940 and value <= 2040 else False

def leap_year(yyyy: int) -> bool:
    if yyyy % 4 == 0:
        return True
    return False
        
    """
    Return
    - True if yyyy is a multiple of 4 (simple leap year)
    - False otherwise
    """

def date(value: str) -> bool:
    """
    Return
    - True if value is a valid str in YYYYMMDD format
    - False otherwise
    """
    try:
        value = value.replace('-', '')
        month = int(value[4:6])
        day = int(value[6:])
    except:
        return False

    if len(value) > 8 or year(int(value[:4])) == False:
        return False
    else: #year is valid
        if 0 < month < 13 and 0 < day < 32:
            return True
        else:
            return False

def singapore_number(value: str) -> bool:
    valid = ['6','8','9']
    if value[0] in valid and len(value) == 8:
        return True
    return False
    """
    Return
    - True if value is a valid Singapore contact number
      (Eight digits starting with 6, 8, or 9)
    - False otherwise
    """


def foreign_number(value: str) -> bool:
    
    """
    Return
    - True if value is a valid foreign contact number
      consists of optional starting '+', and digits only
    - False otherwise
    """
    if '+' in value:
        if value[1:].isdigit():
            return True
        else:
            return False
    elif value.isdigit():
        return True
    else:
        return False
        
def contact_number(value: str) -> bool:
    """
    Return
    - True if value is a valid singapore or foreign number
    - False otherwise
    """
    if singapore_number(value) == True or foreign_number(value) == True:
        return True
    else:
        return False

def username(value: str) -> bool:
    if value == '':
        return False
    for letter in value:
        if letter not in valid_user_char:
            return False
    return True
    
    """
    Return
    - True if value is a valid username
      - contains only letters, numbers, or '._-+'
    - False otherwise
    """

def domain(value: str) -> bool:
    for i in value:
        if i not in valid_domain_char:
            return False
    if 1 <= value.count('.') <= 2:
        return True
    else:
        return False
    """
    Return
    - True if value is a valid domain
      - has only one or two '.'
      - contains only letters, numbers, or '.-_'
    - False otherwise
    """

def email(value: str) -> bool:
    """
    Return
    - True if value is a valid email address
      - has only one @
      - username and domain are valid
      - username contains only letters, numbers, or '._-+'
      - domain has only one or two '.'
      - domain contains only letters, numbers, or '.-_'
    - False otherwise
    """
    if value.count('@') != 1:
        return False
    try:
        username1, domain1 = value.split('@')
    except:
        return False
    return domain(domain1) and username(username1)

def nyjc_email(value: str) -> bool:
    """
    Assume value is a valid email.

    Return
    - True if value is a valid NYJC email address
      (domain: nyjc.edu.sg)
    - False otherwise
    """
    return 'nyjc.edu.sg' in value

def moe_email(value: str) -> bool:
    """
    Assume value is a valid email.

    Return
    - True if value is a valid MOE email address
      (domain: moe.edu.sg)
    - False otherwise
    """
    return 'moe.edu.sg' in value

def gov_email(value: str) -> bool:
    """
    Assume value is a valid email.

    Return
    - True if value is a valid Gov email address
      (domain: schools.gov.sg)
    - False otherwise
    """
    return 'schools.gov.sg' in value

def approved_email(value: str) -> bool:
    """
    Assume value is a valid email.

    Return
    - True if value is an approved email address
      (NYJC, MOE, or Gov)
    - False otherwise
    """
    return any([gov_email(value), nyjc_email(value), moe_email(value)])

def contains(options: list, choice: str) -> bool:
    """
    Return
    - True if choice is in options
    - False otherwise
    """
    return choice in options

