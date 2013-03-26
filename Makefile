default: test

test:
	python bucketsort/bucketsort.py -t
	python heapsort/heapsort.py -t
	python mergesort/mergesort.py -t

# vim: noexpandtab
