# Dictionary with English words as keys and their Nepali meanings as values
nepali_dict = {
    "hello": "नमस्ते",
    "world": "संसार",
    "apple": "स्याउ",
    "book": "किताब",
    "computer": "कम्प्युटर"
}

# Function to get the Nepali meaning of an English word
def translate_to_nepali(word):
    return nepali_dict.get(word.lower(), "शब्द फेला परेन")

# Main program
if __name__ == "__main__":
    while True:
        english_word = input("Enter an English word (or 'exit' to quit): ")
        if english_word.lower() == 'exit':
            break
        nepali_meaning = translate_to_nepali(english_word)
        print(f"The Nepali meaning of '{english_word}' is: {nepali_meaning}")