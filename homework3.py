text = input("Enter your text: ")

word_1, word_2 = text.split()

formatted_1 = f"{word_2.upper()} {word_1.capitalize()}"
formatted_2 = '{} {}'.format(word_2.capitalize(), word_1.upper())
formatted_3 = '{1} {0}'.format(word_2.capitalize(), word_1.upper())

print("<<<>>>".join(["!", text, "?", "!", formatted_1, "?", "!", formatted_2, "?", "!", formatted_3, "?", text[::-1], "?"]))

