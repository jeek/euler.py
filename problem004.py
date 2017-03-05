from multiprocessing import Process, Queue
import unittest
from time import time
from palindrome import is_palindrome

def problem004(output, argument=3):
    """Solve Problem #4."""
    answer = 0
    for second_number in xrange(10 ** (argument - 1), 10 ** argument):
        for first_number in xrange(10 ** (argument - 1), second_number + 1):
            if first_number * second_number > answer and is_palindrome(first_number * second_number):
                answer = first_number * second_number
    output.put((4, answer))

class TestProblem004(unittest.TestCase):
    """Test Problem #4."""

    def test_isanswercorrect(self):
        """Make sure we have the correct answer."""
        answer = Queue()
        Process(target=problem004, args=(answer,)).start()
        self.assertEqual(answer.get(), (4, 906609))

    def test_example(self):
        """Check the provided example."""
        answer = Queue()
        Process(target=problem004, args=(answer, 2)).start()
        self.assertEqual(answer.get(), (4, 9009))

    def test_sixtyseconds(self):
        """Ensure code runs in under 60 seconds."""
        starttime = time()
        answer = Queue()
        Process(target=problem004, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
