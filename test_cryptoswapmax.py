# test_cryptoswapmax.py
"""
Tests for CryptoSwapMax module.
"""

import unittest
from cryptoswapmax import CryptoSwapMax

class TestCryptoSwapMax(unittest.TestCase):
    """Test cases for CryptoSwapMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSwapMax()
        self.assertIsInstance(instance, CryptoSwapMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSwapMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
