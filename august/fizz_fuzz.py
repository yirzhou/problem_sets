class Solution:
    """#412. Write a program that outputs the string representation of numbers from 1 to n.

    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
    For numbers which are multiples of both three and five output “FizzBuzz”.
    """
    def fizzBuzz(self, n: int):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0 and not i % 5 == 0:
                result.append('Fizz')
            elif not i % 3 == 0 and i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
        