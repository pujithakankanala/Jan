def sort_words():
    words = input("Enter a sequence of words separated by spaces: ").split()
    sorted_words = sorted(words)
    print("Sorted words:", " ".join(sorted_words))

# Run the function
sort_words()