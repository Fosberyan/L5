import json

aveprofit = 0
firms = {}
with open('che.json', 'w') as fw:
    with open('test.txt', encoding="utf-8") as f:
        entries = f.read().split('\n')
        entries = filter(lambda el: bool(el), entries)
        for entry in entries:
            [name, mfo_code, expenses, proceeds] = entry.split(' ')
            firm_profit = int(expenses) - int(proceeds)
            firms[name] = firm_profit
            if firm_profit > 0:
                aveprofit = firm_profit if aveprofit == 0 else (aveprofit + firm_profit) / 2
    itog = [firms, {aveprofit: aveprofit}]

    json.dump(itog, fw, ensure_ascii=False, indent=4)
