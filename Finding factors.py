conditions = ['yes','no','y','n']
while True:
    try:
        input_num = int(input('Enter a number: '))
        break
    except:
        print('Not a Valid Input!!')
while True:
    prime_condition = str(input('Do you want to know if the number is a prime or composite?'))
    prime_condition.lstrip().lower()
    if prime_condition in conditions:
        break
    else:
        print('Invalid Input!!')
        continue
initial = int(1)
num = list()
while initial <= input_num:
    x = input_num % initial
    if x == 0:
        print(initial)
        num.append(initial)
    initial = initial + 1
prime = [1, input_num]
if prime_condition == 'yes':
    if not num == prime:
        print('The number is not  prime')
    else:
        print('The number is prime')
