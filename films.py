collections import Counter
with open('input.txt', 'r',  encoding='utf-8') as fl:
    onstring = fl.readlines()
    d = {}
    for i in onstring:
        if i.find('\n')!=-1:
            i=i[:-1]
        else:
            i=i
        k, *v = i.split(' ')
        d.update({k:v})
print(d)
str1, str2=input('Введите названия двух фильмов: ').split()
actors_for_first=(d.get(str1))
actors_for_second=d.get(str2)
m=(actors_for_first+actors_for_second) #общий список (с повторениями)
o = list(set(m)) #исключение повторяющихся фамилий
z=', '.join(o)
print('Общий актерский состав, (актеры, снявшиеся хотя бы в одном из этих двух фильмов):', z)
conjunction=[k for k,v in Counter(m).items() if v>1] #список повторяющихся фамилий
y=', '.join(conjunction)
print('Актеры, снявшиеся и в первом, и во втором фильме: ',y)

for i in actors_for_first[:]:
      if i in actors_for_second:
          actors_for_first.remove(i)
u=', '.join(actors_for_first)

print('Актеры, участвующие в съемках первого, но не участвующие в съемках второго: ', u)
