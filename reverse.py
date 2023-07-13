arr = list(map(int, input("Enter elements separated by spaces: ").split()))
s = int(input("Enter the index to start reversing from: "))
j = int(input("Enter the index to end reversing at: "))
k = arr[:s] + arr[s:j+1][::-1] + arr[j+1:]
print(k)
