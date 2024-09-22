print('Welcome to the Palindrome Detector')
user_list = ['word', 'number']
while True:
    user_choices = input('Do you want to use a word or a number:')
    user_choices = user_choices.lower()
    user_choices = user_choices.lstrip()
    if user_choices in user_list:
        break
    else:
        print('Invalid Input!!')
        continue
if user_choices == 'number':
    input_num = str(input('Enter a number'))
    og_list = list(map(int, input_num))
    control = list()
    control = control + og_list
    og_list.reverse()
    if og_list == control:
        print('The number is a Palindrome')
    else:
        print('The number is not a Palindrome')
#FIND A WAY TO REPLECATE NUMBERS WITHOUST LISTS OR WITH LISTS
elif user_choices == 'word':
    input_word = input("Enter a Word:")
    input_word.strip(' ')
    word_lst = list(input_word)
    word_control = word_lst
    word_lst.reverse()
    print(word_lst)
    print(word_control)
    if word_lst == word_control:
        print('The word is a palindrome')
    else:
        print('The word is not a palindrome')
