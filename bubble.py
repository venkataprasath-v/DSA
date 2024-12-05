print("Hi")

arr = [4,7,2,9,1,3,8,6,5]


def printarr():
    fin = ""
    for k in range(len(arr)):
        fin = fin + " | " + str(arr[k])

    print(fin)

for i in range(len(arr)):
    printarr()
    for j in range(len(arr) - i - 1):
        if(arr[j] > arr[j+1]):
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
         




