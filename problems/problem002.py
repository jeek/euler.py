from multiprocessing import Process, Queue
from time import time
import unittest
from itertools import islice
from utils.fibonacci import genfib

def problem002(output, argument=4000000):
    """Solve Problem #2."""
    fibonacci_generator = genfib(1, 2)
    terms = [fibonacci_generator.next()]
    while terms[-1] < argument:
        terms.append(fibonacci_generator.next())
    terms.pop()
    terms = [i for i in terms if i % 2 == 0]
    output.put((2, sum(terms)))

class TestProblem002(unittest.TestCase):
    """Test Problem #2."""

    def test_isanswercorrect(self):
        """Make sure we have the correct answer."""
        answer = Queue()
        Process(target=problem002, args=(answer,)).start()
        self.assertEqual(answer.get(), (2, 4613732))

    def test_example(self):
        """Check the provided example."""
        self.assertEqual([i for i in islice(genfib(1, 2), 10)], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_sixtyseconds(self):
        """Ensure code runs in under 60 seconds."""
        starttime = time()
        answer = Queue()
        Process(target=problem002, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
