all: results.txt

results.txt: euler.py
	python euler.py | tee results.txt

check:	test

test:	euler.py
	python -m unittest -v fibonacci palindrome primes sumsteplist \
	                      problem001 problem002 problem003 problem004 \
	                      euler

clean:
	rm -rf *~ *.pyc
