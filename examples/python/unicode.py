from unidecode import unidecode

def remove_unicode_and_replace_with_ascii(text):
    return unidecode(text)

# Example usage
unicode_text = "Héllø, thïs ís ünícødè tèxt."
ascii_text = remove_unicode_and_replace_with_ascii(unicode_text)
print(ascii_text)