default: test

test:
	python bucketsort/bucketsort.py -t
	python mergesort/mergesort.py -t

# vim: noexpandtab
