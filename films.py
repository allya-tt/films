from collections import Counter, defaultdict
with open('input.txt', 'r',  encoding='utf-8') as fl: #получение словаря путем считывания строк из файла, ключи - фильмы, актеры - значения
    onstring = fl.readlines()
    d = {}
    for i in onstring:
        if i.find('\n')!=-1:
            i=i[:-1]
        else:
            i=i
        k, *v = i.split(' ')
        d.update({k:v})
print('Выберите один пункт из представленных ниже: \n'
      '1) по 2-м названиям фильмов вывести общий актерский состав, список актеров, снимавшихся и в первом,'
      ' и во втором фильме и список актеров, участвующих в съемках первого, но не участвующих в съемках второго \n'
      '2) по заданным актерам получить названия фильмов, в которых снимался хотя бы в одном из актеров, названия фильмов'
      ' в которых снимались оба актера и названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй' )
menu=int(input())
if menu==1:
    str1, str2=input('Введите названия двух фильмов: ').split()
    actors_for_first=(d.get(str1)) #список актеров 1-го фильма, получаемый по названию фильма
    actors_for_second=d.get(str2) #список актеров 2-го фильма, получаемый по названию фильма
    m=(actors_for_first+actors_for_second) #общий список (с повторениями)
    o = list(set(m)) #исключение повторяющихся фамилий
    z=', '.join(o)
    print('Общий актерский состав, (актеры, снявшиеся хотя бы в одном из этих двух фильмов):', z)
    conjunction=[k for k,v in Counter(m).items() if v>1] #список повторяющихся фамилий
    y=', '.join(conjunction)
    print('Актеры, снявшиеся и в первом, и во втором фильме:',y)

    for i in actors_for_first[:]:
          if i in actors_for_second:
              actors_for_first.remove(i)
    u=', '.join(actors_for_first)
    print('Актеры, участвующие в съемках первого, но не участвующие в съемках второго: ', u)
elif menu==2:
    str1, str2 = input('Введите две фамилии актеров: ').split()
    y = defaultdict(list) #получение нового словаря из старого заменой ключей значениями и наоборот, ключи - актеры, значения - фильмы
    for key, values in d.items():
        for value in values:
            y[value].append(key)
    films_for_first = (y.get(str1))  # список фильмов для 1-го актера
    films_for_second = y.get(str2)  # список фильмов для 2-го актера
    m = (films_for_first + films_for_second)  # общий список (с повторениями)
    o = list(set(m))  # исключение повторяющихся фильмов
    z = ', '.join(o)
    print('Названия фильмов, в которых снимался хотя бы в одном из актеров:', z)
    conjunction = [k for k, v in Counter(m).items() if v > 1]  # список повторяющихся фильмов
    y = ', '.join(conjunction)
    print('Названия фильмов, в которых снимались оба актера:', y)
    for i in films_for_first[:]:
        if i in films_for_second:
            films_for_first.remove(i)
    u = ', '.join(films_for_second)
    print('Названия фильмов, в которых снимался первый актер, но не участвовал в съемках второй:', u)
