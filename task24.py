def most_common_char(text: str) -> str:
    text = text.lower()
    max_leter = text[0]

    for i in text:
        if text.count(i) > text.count(max_leter):
            max_leter = i

    return max_leter



text = 'salom dunyo'

print(most_common_char(text=text))