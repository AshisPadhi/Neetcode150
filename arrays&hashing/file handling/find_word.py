def find_word(file_path, target_word):
    with open(file_path,"r") as file:
        for line_num, line in enumerate(file,start=1):
            if target_word in line:
                print(f"Target word '{target_word}' is found in line number {line_num}")

find_word("/Users/aspadhi/projects/Neetcode150/arrays&hashing/find_word.txt","Python")