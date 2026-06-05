
def buble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]
    print(v)

v = [24,48,92,37,12,57,86,33]
print(v)
buble_sort(v)