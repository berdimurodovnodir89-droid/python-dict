def most_common_char(text: str) -> str:
    text = text.lower()
    max_lower = text[0]

    for i in text:
        if text.count(i) > text.count(max_lower):
            max_lower = i

    return max_lower

text = 'Hello world'

print(most_common_char(text=text))