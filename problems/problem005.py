from multiprocessing import Process, Queue
import unittest
from time import time
from utils.gcd import lcm

def problem005(output, argument=20):
    """Solve Problem #5."""
    answer = 0
    output.put((5, reduce(lcm, range(1, argument+1))))

class TestProblem005(unittest.TestCase):
    """Test Problem #5."""

    def test_isanswercorrect(self):
        """Make sure we have the correct answer."""
        answer = Queue()
        Process(target=problem005, args=(answer,)).start()
        self.assertEqual(answer.get(), (5, 232792560))

    def test_example(self):
        """Check the provided example."""
        answer = Queue()
        Process(target=problem005, args=(answer, 10)).start()
        self.assertEqual(answer.get(), (5, 2520))

    def test_sixtyseconds(self):
        """Ensure code runs in under 60 seconds."""
        starttime = time()
        answer = Queue()
        Process(target=problem005, args=(answer,)).start()
        self.assertLess(time() - starttime, 60)
