#Counting in a Loop
count = 0
for num in [8,9,45,21,12]:
    count += 1
print(count)

#Summing in a loop:
total = 0
for num in [8,9,45,21,12]:
    total += num
print(total)

#Finding avg in Loop
count = 0
total = 0
for num in [8,9,45,21,12]:
    count += 1
    total += num
print(count,total,count/total)

#Flitering a Loop
for num in [8,9,45,21,12]:
    if num > 20:
        print(num)
print("Done")

#search using Boolean variable
fount = False
for num in [8,9,45,21,12]:
    if num == 45:
        fount = True
        print(num)
        break

#Finding the smallest value
smallest_no = None
for num in [8,9,45,21,12]:
    if smallest_no is None:
        smallest_no = num
    elif num < smallest_no:
        smallest_no = num
print(smallest_no)

#Finding the largest value
largest_no = None
for num in [8,9,45,21,12]:
    if largest_no is None:
        largest_no = num
    elif num > largest_no:
        largest_no = num
print(largest_no)
