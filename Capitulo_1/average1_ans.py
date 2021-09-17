values = []

while True:
    try:
        line = input('Add a number or enter to finish: ')
        if not line:
            break
        values.append(int(line))
    except ValueError as err:
        print(err)

print(f'You typed {values}')
print(f'Values count : {len(values)}')
print(f'Highest : {max(values)}')
print(f'Lowest : {min(values)}')
print(f'Sum : {sum(values)}')
print(f'Mean :{sum(values) / len(values)}')