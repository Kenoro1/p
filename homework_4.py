numb = int(input('Enter number: '))

max = numb % 10
numb = numb // 10
while numb > 0:
    if numb % 10 > max:
        max = numb % 10
    numb = numb // 10
print(max)
