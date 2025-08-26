arr = [1,14,12,9,18,3]

# print(max(arr))
max = arr[1]
for i in arr:
    if(i > max):
        max = i
print(max)