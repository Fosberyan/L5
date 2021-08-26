with open('test.txt', 'r', encoding='utf-8') as f:
    chel = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняк по хате = {round(sum(chel.values()) / len(chel), 3)}\n'
          f'Вот нищеброд(ы) {[e[0] for e in chel.items() if e[1] < 20000]}')