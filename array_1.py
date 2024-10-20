length = int(input("Enter the length of the first array: "))
arr = []
arr2=[]
for i in range(0,length):
    number = int(input("Enter the values: "))
    arr.append(number)
    arr2.append(arr[i])

arr2.append("8")
print(arr)
print(arr2)