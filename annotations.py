def letter_multiply(text: str, symbol: str, repeat: int) -> str:
    result: str = text.replace(symbol, symbol*repeat)
    return result


text = 'python'
print(letter_multiply(text, 't', 5))
