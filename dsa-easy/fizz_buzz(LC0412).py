#STANDARD FIZZBUZZ SOLUTION O(n)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1 , n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        
#OPTIMIZED WITH LIST COMPREHENSIONS O(n)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i) for i in range(1, n + 1)]