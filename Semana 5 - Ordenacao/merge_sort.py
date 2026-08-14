from math import inf


def merge_sort(v,ini, fim):
    if ini < fim:
        print("Inicio:",ini, " Fim:",fim) 
        meio = (ini + fim) // 2
        print("Meio:",meio) 
        merge_sort(v,ini,meio)
        merge_sort(v,meio+1,fim)
        intercala(v,ini,meio,fim)

def intercala(v,ini,meio,fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    print("Left:",L)
    print("Rigth",R)
    #sentinelas - infinito - evita que a incrementacao ultrapasse uma quantidade devida de indices
    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(ini,fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
    print(v)

v = [5,2,4,7,1,3,2,6]
ini = 0
fim = len(v)-1
merge_sort(v,ini,fim)
