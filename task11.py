config = {}

for i in range(1):
    key = input(f'key {i+1} = ')     
    value = input(f'value {i+1} = ')     

    config[key] = value

print(config.keys())