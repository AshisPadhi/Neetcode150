def find_largest_word(file_path):
    longest_word=""
    with open(file_path,"r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word=word
    return longest_word

print(f"Longest word in file: {find_largest_word("/Users/aspadhi/projects/Neetcode150/arrays&hashing/log copy.txt")}")