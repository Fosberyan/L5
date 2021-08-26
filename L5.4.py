replace_parts = {
    'One': 'Один',
    'Two': 'Тор',
    'Three': 'Фрея',
    'Four': 'Локи'
}

with open('test2.txt', 'r') as input_file:
    with open('test3.txt', 'w') as output_file:
        for line in input_file:
            parts = line.split('-')
            parts = list(map(lambda el: str(el).strip(), parts))

            for key in replace_parts.keys():
                parts[0] = str(parts[0]).replace(key, replace_parts[key])

            output_file.write(f'{parts[0]} - {parts[1]}\n')
