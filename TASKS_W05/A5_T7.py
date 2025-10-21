DELIMITER = ','

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    all_words = DELIMITER.join(words)
    return all_words

def analyseWords(words_string):
    if not words_string:
        print("No words entered.")
        return
    words_list = words_string.split(DELIMITER)
    num_words = len(words_list)
    total_chars = sum(len(word) for word in words_list)
    avg_length = total_chars / num_words if num_words > 0 else 0

    print(f"- {num_words} Words")
    print(f"- {total_chars} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    
def main():
    print("Program starting.")
    collected_words = collectWords()
    analyseWords(collected_words)
    print("Program ending.")

    main()