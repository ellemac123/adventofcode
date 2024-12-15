import unittest
from part_two import isDecrementing, isIncrementing

class TestIsDecrementing(unittest.TestCase): 
    def test_decrementing_series(self):
        decRow = [46, 47, 45, 44, 43]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)

    def test_decrementing_with_three_vales(self): 
        decRow = [50, 47, 45, 44, 41, 38]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)
    
    def test_unremovable_unsafe(self): 
        decRow = [50, 47, 45, 40, 41, 38]
        result = isDecrementing(decRow)
        self.assertEqual(result, False)

    def test_dec_with_one_unsafe(self): 
        # should be able to have one removable unsafe
        decRow = [50, 47, 45, 44, 44, 41]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)
    
    def test_dec_2_unsafe(self): 
        decRow = [50, 47, 45, 44, 44, 41, 37]
        result = isDecrementing(decRow)
        self.assertEqual(result, False)
    
    def test_first_same(self): 
        decRow = [47, 47, 45, 44, 41]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)

    def test_last_same(self): 
        decRow = [47, 46, 45, 44, 44]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)

    def test_first_negative(self): 
        decRow = [50, 46, 45, 44, 43]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)

    def test_last_negative(self): 
        decRow = [47, 46, 45, 44, 40]
        result = isDecrementing(decRow)
        self.assertEqual(result, True)
    
    # def test_second_last_negative(self): 
    #     decRow = [47, 46, 45, 48, 44]
    #     result = isDecrementing(decRow)
    #     self.assertEqual(result, True)



class TestIsIncrementing(unittest.TestCase): 
    def test_incrementing_series(self):
        incRow = [33, 34, 37, 39, 40, 43]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)
    
    def test_incrementing_with_three_vales(self): 
        incRow = [31, 34, 37, 39, 40, 43]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)
    
    def test_unremovable_unsafe(self): 
        incRow = [38, 41, 40, 45, 47, 50]
        result = isIncrementing(incRow)
        self.assertEqual(result, False)
    
    def test_inc_with_one_unsafe(self): 
        # should be able to have one removable unsafe
        incRow = [31, 34, 37, 40, 40, 43]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)
    
    def test_inc_with_two_unsafe(self): 
        # should be able to have one removable unsafe
        incRow = [31, 34, 34, 37, 40, 40, 43]
        result = isIncrementing(incRow)
        self.assertEqual(result, False)

    def test_first_same(self): 
        incRow = [34, 34, 37, 40, 41, 43]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)
    
    def test_last_same(self): 
        incRow = [32, 34, 37, 40, 41, 41]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)
    
    def test_first_negative(self): 
        incRow = [28, 34, 37, 40, 41, 42]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)

    def test_last_negative(self): 
        incRow = [32, 34, 37, 40, 41, 47]
        result = isIncrementing(incRow)
        self.assertEqual(result, True)

    # def test_second_last_negative(self): 
    #     incRow = [35, 36, 37, 40, 47, 41]
    #     result = isIncrementing(incRow)
    #     self.assertEqual(result, True)



if __name__ == "__main__":
    unittest.main()
