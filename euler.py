"""Solve Project Euler problems in python."""
from multiprocessing import Queue, Process
import problems

if __name__ == "__main__":
    ANSWERS = Queue()
    COUNT = 0
    FUNCTION_LIST = [problems.problem001,
                     problems.problem002,
                     problems.problem003,
                     problems.problem004,
                     problems.problem005,
                     problems.problem006]
    for problemNO in FUNCTION_LIST:
        Process(target=problemNO, args=(ANSWERS,)).start()
        COUNT += 1
    FINALANSWERS = dict()
    I = 1
    while I <= COUNT:
        if I not in FINALANSWERS:
            PROBLEMNUMBER, ANSWER = ANSWERS.get()
            FINALANSWERS[PROBLEMNUMBER] = ANSWER
        else:
            print(I, FINALANSWERS[I])
            I += 1
