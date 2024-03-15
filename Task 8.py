age_computer = 80
name_human = input('Здравствуйте! Как Вас зовут?')
print(f'Очень приятно,{name_human}! Меня зовут Марк.')
age_human = int(input('Сколько Вам лет? '))
if age_computer > age_human:
    old = age_computer - age_human
    print(f'Да,{name_human}, я старше Вас на {old} лет.')
else:
    old = age_human - age_computer
    print(f'Да,{name_human}, Вы старше меня на {old} лет.')
answer = input('Вам нравится программировать? ')
if answer.lower() == 'да':
    print(f'Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
else:
    print(f'Жаль. Я думал, Вы сможете написать интересную программу для меня.')