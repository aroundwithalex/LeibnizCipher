"""
Unit tests for the scrambling method

This module contains unit tests for the scrambling method. It first
tests the lookup table, to ensure that it is correctly returned. It
then tests the scrambler, to ensure text is encrypted as expected.

Typical Usage:
    $ unittest discover
"""

import unittest

from src.lookup_table import LOOKUP_TABLE
from src.leibniz_cipher import scramble
from src.leibniz_cipher import unscramble

class TestScrambler(unittest.TestCase):
    """
    Class for testing the scrambler.

    This class tests the generation of the lookup table and the scrambling
    of text using the Leibniz cipher. The first test ensures that the lookup
    table is correctly returned, whereas the second ensures text is correctly
    scrambled. 

    Attributes:
        None
    """

    def test_lookup_table(self):
        """
        Tests the lookup table is correctly returned

        This method ensures that the lookup table is correctly returned
        from the relevant function. This enables the scrambling.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
        """

        self.assertIsInstance(LOOKUP_TABLE, dict)
    

    def test_scrambler(self):
        """
        Tests the scrambling method works correctly

        This method tests the scrambling method, to ensure it is working
        as expected.  It should take a string "hello world" and return
        a scrambled version of the string.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
        """

        self.assertEqual(scramble("hello world"), "ioaat xtean")

    def test_unscrambler(self):
        """
        Tests the unscrambling works correctly

        This method tests the unscrambling method works correctly, by
        ensuring that the expected string is returned and unscrambled
        correctly.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
        """

        self.assertEqual(unscramble("ioaat xtean"), "hello world")
