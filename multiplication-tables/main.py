# Main code
while True:
    num = float(input('\nEnter number for table: '))
    print(f'\nMultiplication table of {num}\n' + '-'*20)
    for multiplier in range(1, 11):
        print(f'{num} x {multiplier} = {num * multiplier}')
    print('-' * 20)
    
    if input("Continue? (Y/N): ").strip().upper() != 'Y':
        break

#FIXME: SOLVE ERRORS FOR MULTIPLICATION OF FLOATS
