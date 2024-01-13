# используется для сортировки
from operator import itemgetter


class Sec:
    """Раздел"""
    def __init__(self, id, title, word, Doc_id):
        self.id = id
        self.title = title
        self.word = word
        self.Doc_id = Doc_id


class Doc:
    """Документ"""
    def __init__(self, id, titl):
        self.id = id
        self.titl = titl


class SecDoc:
    """
    'Разделы документа' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, Doc_id, Sec_id):
        self.Doc_id = Doc_id
        self.Sec_id = Sec_id


# Документы

Docs = [
    Doc(1, 'Капитанская дочка'),
    Doc(2, 'Ася'),
    Doc(3, 'Крыжовник'),


    Doc(11, 'Собачье сердце'),
    Doc(22, 'Документ Финансист'),
    Doc(33, 'Документ Лабораторная работа'),
]

# Разделы
Secs = [
    Sec(1, 'Глава 1', 250, 1),
    Sec(2, 'Глава 2', 300, 2),
    Sec(3, 'Глава 3', 400, 3),
    Sec(4, 'Глава 4', 350, 3),
    Sec(5, 'Глава 5', 250, 3),
]


Secs_Docs = [
    SecDoc(1,1),
    SecDoc(2,2),
    SecDoc(3,3),
    SecDoc(3,4),
    SecDoc(3,5),


    SecDoc(11,1),
    SecDoc(22,2),
    SecDoc(33,3),
    SecDoc(33,4),
    SecDoc(33,5),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(e.title, e.word, d.titl) 
        for d in Docs 
        for e in Secs 
        if e.Doc_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_tSec = [(d.titl, ed.Doc_id, ed.Sec_id) 
        for d in Docs 
        for ed in Secs_Docs 
        if d.id==ed.Doc_id]
    
    many_to_many = [(e.title, e.word, Doc_titl) 
        for Doc_titl, Doc_id, Sec_id in many_to_many_tSec
        for e in Secs if e.id==Sec_id]


    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все документы
    for d in Docs:
        # Список разделов документа
        d_Secs = list(filter(lambda i: i[2]==d.titl, one_to_many))
        # Если документ не пустой
        if len(d_Secs) > 0:
            # Число слов в документах
            d_words = [word for _,word,_ in d_Secs]
            # Суммарное число слов разделов документа
            d_words_sum = sum(d_words)
            res_12_unsorted.append((d.titl, d_words_sum))


    # Сортировка по суммарному количеству слов
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все документы
    for d in Docs:
        if 'Документ' in d.titl:
            # Список разделов документа
            d_Secs = list(filter(lambda i: i[2]==d.titl, many_to_many))
            # Только Название раздела
            d_Secs_titls = [x for x,_,_ in d_Secs]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.titl] = d_Secs_titls


    print(res_13)


if __name__ == '__main__':
    main()
