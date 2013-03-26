from optparse import OptionParser
import random

def sift_down(a, left, right):
    root = left
    while(root * 2 + 1 <= right):
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]: swap = child
        if child + 1 <= right and a[swap] < a[child + 1]: swap = child + 1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else: return

def heapify(a, count):
    start = (count - 2) / 2
    while(start >= 0):
        sift_down(a, start, count-1)
        start -= 1

def heapsort(a, count):
    heapify(a, count)
    end = count - 1
    while(end > 0):
        a[end], a[0] = a[0], a[end]
        end = end - 1
        sift_down(a, 0, end)

def main(test = False):
    a = [random.randint(0, 100) for i in range(1, 100)]
    if not test: print 'Start:', a
    heapsort(a, len(a))
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
