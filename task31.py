def count_letters(text: str) -> dict[str, int]:

    result = {}
    
    for char in text.lower(): 
        if char.isalpha(): 
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    
    return result

text = "assalomu alaykum"
print(count_letters(text))
