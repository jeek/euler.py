all: results.txt

results.txt: euler.py
	python euler.py | tee results.txt

check:	test

test:	euler.py
	python -m unittest -v euler
	cd problems;make test

clean:
	rm -rf *~ *.pyc results.txt
	cd problems;make clean
