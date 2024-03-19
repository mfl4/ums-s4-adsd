def find_longest_word(sentence):
    """
    Find the longest word in the given sentence.
    Args:
        sentence (str): The input sentence to find the longest word from.
    Returns:
        str: A string indicating the longest word found.
    """
    # Mengembalikan pesan berupa kata terpanjang yang dapat dengan
    # Mencari kata terpanjang dalam kalimat yang diberikan
    # Dengan cara membagi kalimat menjadi kata-kata
    # Dan kemudian mencari kata terpanjang berdasarkan panjangnya
    return f"The longest word is: {max(sentence.split(), key=len)}"

print(find_longest_word('I love to learn python'))
print("\nProgram Completed!\n\n--- By L200220277 ---")