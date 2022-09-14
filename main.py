import csv

f = open('output.txt', 'w')
with open ('books.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    c = -1
    counter = 0
    author = input('Введите желаемого автора: ')
    state = input('Введите 1, если хотите ввести 20 id книг для карточек, иначе 0 на рандом: ')
    cards = 20  # 20
    id_array = []
    tags_array = []
    flag = 0
    if state == '1':
        for i in range(cards):
            id_array.append(input('Введите id нужной книги: '))
    else:
        flag = 1
    for row in reader:
        c += 1  # условие 1

        # условие 5
        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]
        last_name = row[3].split()
        last_name = last_name[-1:]

        # доп на тэги
        tags = row[12].split('#')
        for tag in tags:
            if not(tag in tags_array):
                tags_array.append(tag)

        if flag == 0:
            if row[0] in id_array:
                f.write('<'+str(*last_name)+'>. <'+str(row[1])+'> - <'+str(year)+'>'+'\n')
        elif (flag == 1) and (c < 22) and (c > 1):
            f.write('<' + str(*last_name) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')

        # условие 3 вариант 4
        if len(last_name) > 0:
            if (author == str(last_name[0])) and (int(row[7]) < 200):
                print(row[1])
        # условие 2
        if len(row[1]) > 30:
            counter += 1

    print('количество записей в таблице: ', c)
    print('количество записей названий > 30: ', counter)

    # доп на тэги
    tags_array.pop(0)
    tags_array.pop(0)
    print(tags_array)

f.close()