import random


problem_words = ['Father', 'Aeroplane', 'Green', 'Apple', 'Mother']
count = 0
list_index = 0

for word in problem_words:
    l = list(word)
    random.shuffle(l)
    result = ''.join(l) 
    print(f'Arrange the letters to form a valid word:{result}')
    your_input = input('Enter the answer: ')

    if problem_words[list_index] == your_input:
        count += 1

    else:
        count -= 1

    list_index += 1

print(count)