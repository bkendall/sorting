from optparse import OptionParser
import random

def merge(left, right):
    result = []
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]
        elif len(left):
            result.append(left[0])
            del left[0]
        elif len(right):
            result.append(right[0])
            del right[0]
    return result

def mergesort(l):
    if len(l) <= 1: return l
    left = []
    right = []
    middle = len(l) / 2
    for i in l[:middle]: left.append(i)
    for i in l[middle:]: right.append(i)
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def main(test = False):
    a = [random.randint(1, 100) for i in range(1, 100)]
    b = a
    if not test: print 'Start:', a
    a = mergesort(a)
    if not test: print 'End:', a

    if test:
        b = list(a)
        b.sort()
        if b == a: exit(1) # all normal
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
