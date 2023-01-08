"""
Basic implementation of the Leibniz Cipher

This module contains a basic implementation of the Leibniz Cipher. It
converts letters into other letters, thus scrambling the contents of
encrypted communications. It was designed to encrypt communications
between Leibniz and Claudio Grimaldi, a Jesuit missionary based in
China (see Strickland & Lewis 2022). The cipher is as follows (see
Strickland & Lewis 2022): -

L a b y r i n t h u s c d e f g k m o p q w x z

a b c d e f g h i j k l m o p q r s t u w x y z

Typical Usage:
    >>> from leibniz_cipher import scramble
    >>> scramble("hello world")
    "....."
"""

from src.lookup_table import LOOKUP_TABLE

def scramble(text: str) -> str:
    """
    Scrambles text using the Leibniz Cipher.

    This method scrambles text utilising the Leibniz cipher. This converts
    letters within a string using the following cipher (see Strickland and
    Lewis 2022):

    L a b y r i n t h u s c d e f g k m o p q w x z

    a b c d e f g h i j k l m o p q r s t u w x y z

    Args:
        Text -> Text to scramble
    
    Returns:
        Scrambled text
    
    Raises:
        None
    """

    scrambled_string = ""

    for letter in text:
        if not letter.isalpha():
            scrambled_string += letter
            continue

        scrambled_string += LOOKUP_TABLE[str(letter)]
    
    return scrambled_string


def unscramble(text: str) -> str:
    """
    Unscrambles text using the Leibniz Cipher.

    This method unscrambles text utilsing the Leibniz cipher. It looks
    values up within the provided lookup table, and re-creates the string
    as originally rendered.

    Args:
        Text -> Text to unscramble
    
    Returns:
        Unscrambled string
    
    Raises:
        None
    """

    unscrambled_string = ""

    lookup_keys = list(LOOKUP_TABLE.keys())
    lookup_values = list(LOOKUP_TABLE.values())

    for letter in text:
        if not letter.isalpha():
            unscrambled_string += letter
            continue
        
        key_letter  = lookup_keys[lookup_values.index(letter)]
        unscrambled_string += key_letter
    
    return unscrambled_string
