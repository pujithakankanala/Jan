def count_letters_digits():
    sentence = input("Enter a sentence: ")
    letter_count = sum(map(str.isalpha, sentence))
    digit_count = sum(map(str.isdigit, sentence))
    
    print(f"Letters: {letter_count}")
    print(f"Digits: {digit_count}")

count_letters_digits()
