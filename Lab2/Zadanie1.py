# Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne
# Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji
# analizy tekstu:

import re
from collections import Counter

# • Zlicza liczbę słów, zdań, i akapitów w tekście.
text = "In the heart of the bustling city, there existed a hidden alleyway, hidden in plain sight. Few knew of its existence, and even fewer dared to enter. Within its dim corners, ivy crept up ancient brick walls, and the faint hum of forgotten magic hummed in the air. At the very end of the alley stood an old wooden door, weathered but still sturdy. A small brass plaque above it read: 'For Seekers of the Unknown.' What lay beyond, only the bravest—or the most desperate—ever found out. The unknown awaited, always calling, always waiting."
def amount_of_everything():
    paragrapgh = "\n"
    print(f"Liczba słow:\t{len(text.split())} \nLiczba zdań:\t {text.count('.')}\nLiczba akapitów:\t{text.count(paragrapgh)}")

amount_of_everything()


# • Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. "i", "a", "the").
def most_common_words():
    stop_words = {"i", "a", "the", "to", "and", "is", "in", "it", "of", "on", "that", "this", "for", "with", "as", "at", "an", "be", "by", "or", "are", "was", "were", "but", "not", "from", "which"}
    translator = str.maketrans('.', ' ')
    list_of_words = ((text.translate(translator)).lower()).split()
    list_without_stop_words = list(filter(lambda x: x not in stop_words, list_of_words))

    word_counts = Counter(list_without_stop_words)
    most_common = word_counts.most_common(5)
    return most_common


result = most_common_words()
print("Najczęściej występujące słowa (bez stop words):")
for word, count in result:
    print(f"{word}: {count}")

# • Transformuje wszystkie wyrazy rozpoczynające się na literę "a" lub "A" do ich odwrotności (np."apple" → "elppa").

def reverse_words_starting_with_a():
    words = text.split()
    
    transformed_words = []
    for word in words:
        if word.lower().startswith('a'):
            transformed_words.append(word[::-1])
        else:
            transformed_words.append(word)
    return ' '.join(transformed_words)

transformation_result = reverse_words_starting_with_a()
print(f"Przekształcony tekst:\t {transformation_result}")