start = int(input("Enter a start value: "))
stop = int(input("Enter a stop value: "))
increment = int(input("Enter a increment value: "))

while start <= stop:
    print(start)
    if start == stop:
        break
    start += increment