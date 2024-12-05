# Program for bubble sort

# Array definition
arr = [4,7,2,9,1,3,8,6,5]

# Function for printing the array
def printarr():
    fin = ""
    for k in range(len(arr)):
        fin = fin + " | " + str(arr[k])

    print(fin)

# Bubble sort
for i in range(len(arr)):
    printarr()
    for j in range(len(arr) - i - 1):
        if(arr[j] > arr[j+1]):
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
         




