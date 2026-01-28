def longest_film(film_1: str, film_2: str,film_3: str) -> str:

    list_film = max(len(film_1), len(film_2), len(film_3))
    if len(film_1) == list_film:
        return film_1
    elif len(film_2) == list_film:
        return film_2
    else:
        return film_3
    



if __name__ == '__main__':
    assert longest_film('Аладин', 'Мадагаскар', 'Бетховен') == 'Мадагаскар'
    assert longest_film('Железный Человек', 'Стражи Галактики 2', 'Капитан Америка') == 'Стражи Галактики 2'
    assert longest_film('Бумер', 'Бумер: Фильм второй', 'Бумеранг') == 'Бумер: Фильм второй'
    assert longest_film('Гарри Поттер и философский камень', 'Пираты Карибского моря: На странных берегах',
                        'ВАЛЛ·И') == 'Пираты Карибского моря: На странных берегах'
    assert longest_film('Ирония судьбы, или С легким паром!', 'Иван Васильевич меняет профессию ',
                        'Джентльмены удачи а') == 'Ирония судьбы, или С легким паром!'
    print("\nОтличная работа, отправляйте на проверку!")