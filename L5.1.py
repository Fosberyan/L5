with open('test.txt', 'w', encoding='utf-8') as f:
    while True:
        a = input('Пиши сюда - ')
        if not a:
            break

        print(a, file=f)