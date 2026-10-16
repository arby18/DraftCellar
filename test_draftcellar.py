# test_draftcellar.py
"""
Tests for DraftCellar module.
"""

import unittest
from draftcellar import DraftCellar

class TestDraftCellar(unittest.TestCase):
    """Test cases for DraftCellar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftCellar()
        self.assertIsInstance(instance, DraftCellar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftCellar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
