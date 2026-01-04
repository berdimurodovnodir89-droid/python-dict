inventory = {
    'olma': 10,
    'anor': 5,
}
products = ['nok','uzum'] 
for product in products:
    if product not in inventory:
     inventory[product] = 0



print(inventory)
