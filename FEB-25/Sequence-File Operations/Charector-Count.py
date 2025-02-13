from collections import Counter
input_string= input()
char_count=Counter(input_string)
for char, count in char_count.items():
     print(f"{char},{count}")