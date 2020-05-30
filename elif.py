a = int(input("Enter a number "))

for i  in range(a+1):
    if i % 5 == 0:
        continue
    elif i % 2 == 0:
        print(i)
