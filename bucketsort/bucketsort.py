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

def main():
    a = [random.randint(1, 100) for i in range(0, 100)]
    print 'Start:', a
    bucketsort(a)
    print 'End:', a

if __name__ == '__main__':
    main()
