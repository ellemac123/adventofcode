"""
Two pointers algorithm 

The time complexity is O(n), where n is the number of characters in the string. 
However, our algorithm will only run O(n/2) times, since 
    two pointers are traversing toward each other
"""

def is_palindrome(s):
  """
  Sample two pointer code for a palindrome solution: 
  Given a string
  Return True if palindrome
    False otherwise
  """
  s = s.lower()
  start = 0
  end = len(s) - 1
  while start < end: 
    if not s[start] == s[end]: 
      return False
    else: 
      start += 1
      end -=1

  return True


if __name__ == "__main__": 
    """
    Some test cases and run the codes
    """
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    
    for word in test_cases: 
        print(f'is {word} a palindrome?: {is_palindrome(word)}')