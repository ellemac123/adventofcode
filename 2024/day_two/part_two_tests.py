import unittest
from part_two import isIncrementingOrDecrementing, inc_allowed, dec_allowed, isSafe, isSafeWithOneRemoved

class TestIsDecrementing(unittest.TestCase): 
    """
        Test cases for decrementing values 
    """
    def test_decrementing_series(self):
        decRow = [46, 45, 44, 43, 41]
        result = isIncrementingOrDecrementing(decRow, dec_allowed)
        self.assertEqual(result, True)
    
    def test_safety_decrementing_series(self):
        decRow = [46, 45, 44, 43, 41]
        result = isSafe(decRow)
        self.assertEqual(result, True)

    def test_decrementing_with_three_vales(self): 
        decRow = [50, 47, 45, 44, 41, 38]
        result = isIncrementingOrDecrementing(decRow, dec_allowed)
        self.assertEqual(result, True)
    
    def test_safety_decrementing_with_three_vales(self):
        decRow = [46, 45, 44, 43, 41]
        result = isSafe(decRow)
        self.assertEqual(result, True)

    def test_unremovable_unsafe(self): 
        decRow = [50, 47, 45, 40, 41, 38]
        result = isSafe(decRow)
        self.assertEqual(result, False)
    
    def test_dec_with_one_unsafe(self): 
        """
            should be able to have one removable unsafe
        """
        decRow = [50, 47, 45, 44, 44, 41]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)
    
    def test_dec_2_unsafe(self): 
        decRow = [50, 47, 45, 44, 44, 41, 37]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, False)
    
    def test_first_same(self): 
        decRow = [47, 47, 45, 44, 41]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)

    def test_last_same(self): 
        decRow = [47, 46, 45, 44, 44]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)

    def test_first_negative(self): 
        decRow = [50, 46, 45, 44, 43]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)

    def test_last_negative(self): 
        decRow = [47, 46, 45, 44, 40]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)
    
    def test_second_last_negative(self): 
        decRow = [47, 46, 45, 48, 44]
        result = isSafeWithOneRemoved(decRow)
        self.assertEqual(result, True)

class TestIsIncrementing(unittest.TestCase): 
    """
        Test cases for incrementing values 
    """

    def test_incrementing_series(self):
        incRow = [33, 34, 37, 39, 40, 43]
        result = isIncrementingOrDecrementing(incRow, inc_allowed)
        self.assertEqual(result, True)
    
    def test_incrementing_with_three_vales(self): 
        incRow = [31, 34, 37, 39, 40, 43]
        result = isIncrementingOrDecrementing(incRow, inc_allowed)
        self.assertEqual(result, True)
    
    def test_unremovable_unsafe(self): 
        incRow = [38, 41, 40, 45, 47, 50]
        result = isSafe(incRow)
        self.assertEqual(result, False)
    
    def test_inc_with_one_unsafe(self): 
        # should be able to have one removable unsafe
        incRow = [31, 34, 37, 40, 40, 43]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)
    
    def test_inc_with_two_unsafe(self): 
        # should be able to have one removable unsafe
        incRow = [31, 34, 34, 37, 40, 40, 43]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, False)

    def test_first_same(self): 
        incRow = [34, 34, 37, 40, 41, 43]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)
    
    def test_last_same(self): 
        incRow = [32, 34, 37, 40, 41, 41]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)
    
    def test_first_negative(self): 
        incRow = [28, 34, 37, 40, 41, 42]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)

    def test_last_negative(self): 
        incRow = [32, 34, 37, 40, 41, 47]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)

    def test_second_last_negative(self): 
        incRow = [35, 36, 37, 40, 47, 41]
        result = isSafeWithOneRemoved(incRow)
        self.assertEqual(result, True)



if __name__ == "__main__":
    unittest.main()
