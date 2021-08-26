with open('test.txt', 'r', encoding='utf-8') as f:
    use = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*use, f'Cтрок - {len(use)}.', sep='\n')
