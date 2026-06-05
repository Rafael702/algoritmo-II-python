def insertion_sort(v):
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while j >=0 and x < v[j]:
            print("[" ,j, "]", x, "<", v[j],"=", x < v[j])
            v[j+1] = v[j]
            print(v)
            j -= 1
        v[j+1] = x
    print(v)

v = [44,55,12,42,94,18,6,67]
insertion_sort(v)