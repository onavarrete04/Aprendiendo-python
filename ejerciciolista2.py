if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sub = 0
    for i in range(len(arr)-1):
        for x in range(len(arr)-1):
            if arr[x] < arr[x+1]:
                auxiliar = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = auxiliar
    i = 0
    while True:
        if  arr[0]>arr[i]:
            sub = arr[i]
            
            break       
        i += 1
   
    print(sub)

# solucion 2
n = int(input())
arr = set(map(int, input().split()))  
ordenado = sorted(arr)
sub = ordenado[-2]
print(sub)
print(ordenado)