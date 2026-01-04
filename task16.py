person = {"name": "Ali", "age": 25, "city": "Tashkent"}

key = input('key :')

if key in person:
    person.pop(key)
else :
    print("Bunday kalit yo‘q")
print(person)