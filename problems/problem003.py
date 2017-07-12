"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from multiprocessing import Process, Queue
import unittest
from time import time
from problems.utils.primes import prime_factors


def problem003(output, argument=600851475143):
    """
    Solve Problem #3.
    """
    output.put((3, max(prime_factors(argument))))


class TestProblem003(unittest.TestCase):
    """
    Test Problem #3.
    """

    def test_isanswercorrect(self):
        """
        Make sure we have the correct answer.
        """
        answer = Queue()
        Process(target=problem003, args=(answer,)).start()
        self.assertEqual(answer.get(), (3, 6857))

    def test_example(self):
        """
        Check the provided example.
        """
        self.assertEqual([i for i in prime_factors(13195)], [5, 7, 13, 29])

    def test_sixtyseconds(self):
        """
        Ensure code runs in under 60 seconds.
        """
        starttime = time()
        answer = Queue()
        Process(target=problem003, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
