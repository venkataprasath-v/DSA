# Dutch national flag algorithm to group 3 colours together

arr = [1,1,2,0,2,2,1,1,0,0,2,2,1,2,0,0,2,1]

left, mid, right = 0, 1 , len(arr) - 1

while(mid < right):
    if(arr[mid] == 0 ):
        arr[mid], arr[left] = arr[left], arr[mid]
        left += 1
       
    elif(arr[mid] == 2):
        arr[mid], arr[right] = arr[right], arr[mid]
        right -= 1
        
    else:
        mid +=1

print(arr)

