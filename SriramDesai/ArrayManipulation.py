# Write a function add(arr, x) that takes an array arr and add x to every element in that array

def add(arr,x):
    for i in range(len(arr)):
        arr[i]+=x

# Write a function equal(arr, x) that takes an array arr and returns all the elements in that array that are equal to x
def equal(arr, x):
    count = 0
    for i in arr:
        if(i == x):
            count+=1
    return count

arr = [2,3,5,2]
x = 2   

add(arr,x)
for i in arr:
    print(i)
print(equal(arr,x))