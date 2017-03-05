"""Solve Project Euler problems in python."""
from multiprocessing import Queue, Process
from time import time
import unittest
from itertools import islice
from problem001 import problem001
from problem002 import problem002
from problem003 import problem003
from problem004 import problem004

if __name__ == "__main__":
    ANSWERS = Queue()
    COUNT = 0
    for problemNO in [problem001, problem002, problem003, problem004]:
        Process(target=problemNO, args=(ANSWERS,)).start()
        COUNT += 1
    FINALANSWERS = dict()
    I = 1
    while I <= COUNT:
        if I not in FINALANSWERS:
            PROBLEMNUMBER, ANSWER = ANSWERS.get()
            FINALANSWERS[PROBLEMNUMBER] = ANSWER
        else:
            print I, FINALANSWERS[I]
            I += 1
