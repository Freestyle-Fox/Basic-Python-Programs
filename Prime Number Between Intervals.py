start = int(input("Enter Your starting Number : "))
end = int(input("Enter Your End Number : "))


for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

