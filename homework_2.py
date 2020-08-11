time = int(input('Enter time in seconds: '))

h = time // 3600
m = time // 60 % 60
s = time % 60

print(f'0{h}:0{m}:0{s}')
