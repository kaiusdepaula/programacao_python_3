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

n = len(values)
for i in range(n):
    for j in range(0, n-i-1):
            if values[j] > values[j+1] : 
                    values[j], values[j+1] = values[j+1], values[j]

index =  round(n / 2)
if n % 2 != 0:
    median = values[index]
else:
    median = ( values[index] + values[index - 1] ) / 2

print(f'Median :{median}')