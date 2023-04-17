import os


class File_txt:

    def get_data(self):
        with open(os.path.abspath(self.name),'r') as file:
            text_file = ''
            for line in file:
                self.numb_ln += 1   
                text_file += ''.join(line)
        return text_file

    def __init__(self, name):
        self.name = name
        self.text = self.get_data()
    numb_ln = 0


def get_shop_list_by_dishes(dishes, person_count):
    '''
    Возвращает словарь согласно заданию №2
    '''

    result = {}
    estimation = {}
    for item in dishes:
        for ingridient in cook_book[item]:
            estimation['measure'] = ingridient['measure']
            estimation['quantity'] = ingridient['quantity'] * person_count
            if ingridient['ingredient_name'] not in result:
                result[ingridient['ingredient_name']] = estimation
            else:
                result[ingridient['ingredient_name']]['quantity'] += estimation['quantity']
    return result


cook_book = {}
dishes = ['Омлет', 'Фахитос']
person_count = 2

with open(os.path.abspath('file.txt'),'r') as f:
    for line in f:
        if line == '\n':
            continue
        line = line.rstrip('\n')
        cook_book[line.replace('\n', '')] = []
        num_line = f.readline()
        list = []
        for lines in range(int(num_line)):
            string = f.readline()
            string = string.rstrip('\n')
            string = string.split(sep = ' | ')
            ing_dict = {}
            ing_dict['ingredient_name'] = string[0]
            ing_dict['quantity'] = int(string[1])
            ing_dict['measure'] = string[2]
            list.append(ing_dict)
            
        cook_book[line] = list


#Тест функции get_shop_list_by_dishes()
print(get_shop_list_by_dishes(dishes, person_count))

#Задание 3
list_of_files = []
for item in range(3):
    list_of_files.append(File_txt(f"{str(item + 1) + '.txt'}"))

z = sorted(list_of_files, key=lambda files: files.numb_ln)

for item in range(len(z)):
    with open(os.path.abspath('result.txt'),'a') as f:
           f.write(z[item].name)
           f.write('\n')
           f.write(str(z[item].numb_ln))
           f.write('\n')
           f.write(z[item].text)