"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
from multiprocessing import Process, Queue
import unittest
from time import time

def problem006(output, argument=100):
    """
    Solve Problem #6.
    """
    output.put((6, sum(range(1,argument+1))**2 - sum([i ** 2 for i in range(1, argument+1)])))

class TestProblem006(unittest.TestCase): #pylint: disable=R0904
    """
    Test Problem #6.
    """

    def test_isanswercorrect(self):
        """
        Make sure we have the correct answer.
        """
        answer = Queue()
        Process(target=problem006, args=(answer,)).start()
        self.assertEqual(answer.get(), (6, 25164150))

    def test_example(self):
        """
        Check the provided example.
        """
        answer = Queue()
        Process(target=problem006, args=(answer, 10)).start()
        self.assertEqual(answer.get(), (6, 2640))

    def test_sixtyseconds(self):
        """
        Ensure code runs in under 60 seconds.
        """
        starttime = time()
        answer = Queue()
        Process(target=problem006, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
