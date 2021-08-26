a = {}
with open("test.txt", encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        s = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        a[name] = s
print(f"{a}")
