from multiprocessing import Process, Queue
from time import time
import unittest
from utils import sumsteplist

def problem001(output, argument=1000):
    """Solve Problem #1."""
    output.put((1, sumsteplist(argument, 3) + sumsteplist(argument, 5) - sumsteplist(argument, 15)))

class TestProblem001(unittest.TestCase):
    """Test Problem #1."""

    def test_isanswercorrect(self):
        """Make sure we have the correct answer."""
        answer = Queue()
        Process(target=problem001, args=(answer,)).start()
        self.assertEqual(answer.get(), (1, 233168))

    def test_example(self):
        """Check the provided example."""
        answer = Queue()
        Process(target=problem001, args=(answer, 10)).start()
        self.assertEqual(answer.get(), (1, 23))

    def test_sixtyseconds(self):
        """Ensure code runs in under 60 seconds."""
        starttime = time()
        answer = Queue()
        Process(target=problem001, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
