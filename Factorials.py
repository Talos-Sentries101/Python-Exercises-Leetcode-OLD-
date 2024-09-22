def factorial(number):
    import math
    nums = list()
    nums.append(number)
    while number > 1:
        number = number - 1
        nums.append(number)
    print(math.prod(nums))


input_num = int(input('Enter a number'))

factorial(input_num)
#or use math libery and import .frac()