proceeds = int(input('Enter proceeds: '))
costs = int(input('Enter costs: '))

if proceeds >= costs:
    profit_1 = proceeds - costs
    print(f'Profit {profit_1}')
    rentable = profit_1 / proceeds
    print(f'rentable {rentable}')
elif proceeds <= costs:
    lesion = costs - proceeds
    print(f'Lesion {lesion}')

peoples = int(input('How many peoples u have in your company: '))

while profit_1 or lesion:
    print(f'Firm profit per employee {profit_1 / peoples}')
    break
else:
    print(f'costs per employee {lesion / peoples}')

