from optparse import OptionParser
import random

def seperate(v, n):
    while(v % 10 != 0): v -= 1
    if v / n < n: return v / n
    else: return n - 1

def bucketsort(a, n = 10):
    buckets = [[] for i in range(0, n)]
    for i in range(0, len(a)): buckets[seperate(a[i], n)].append(a[i])
    for i in range(0, n): buckets[i].sort()
    del a[:]
    for i in range(0, n): a.extend(buckets[i])

def main(test = False):
    a = [random.randint(1, 100) for i in range(0, 100)]
    if not test: print 'Start:', a
    bucketsort(a)
    if not test: print 'End:', a

    if test:
        b = list(a)
        b.sort()
        if b == a: exit(0) # all normal
        else: exit(1) # sort didn't work

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-t', '--test',
                      action='store_true',
                      dest='test',
                      default=False,
                      help='Test list with python sort')
    (options, args) = parser.parse_args()

    main(options.test)
