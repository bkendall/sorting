default: test

test:
	python bucketsort/bucketsort.py --test
	python heapsort/heapsort.py --test
	python mergesort/mergesort.py --test

# vim: noexpandtab
