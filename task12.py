inventory = {'olma','amor','banan','nok',"o'rik"}

quantity = 0

for i in inventory:
    if i not in inventory:
        quantity += 1

print(quantity)
