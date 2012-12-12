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

def main():
    a = [random.randint(1, 100) for i in range(1, 100)]
    b = a
    print 'Start:', a
    a = mergesort(a)
    print 'End:', a

if __name__ == '__main__':
    main()
