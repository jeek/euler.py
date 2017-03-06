"""Solve Project Euler problems in python."""
from multiprocessing import Queue, Process
from problems import problem001, problem002, problem003, problem004, problem005

if __name__ == "__main__":
    ANSWERS = Queue()
    COUNT = 0
    for problemNO in [problem001, problem002, problem003, problem004, problem005]:
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
