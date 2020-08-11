f_day = int(input('Какой ваш результат в первый день: '))
result = int(input('Какой результат вы хотите: '))

day = 1
while f_day < result:
    f_day *= 1.1
    day += 1
print(f'Спортсмен достигнет результата за {day} дней')
