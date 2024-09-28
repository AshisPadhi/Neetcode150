def find_word(file_path, target_word):
    try:
        with open(file_path,"r") as file:
            for line_num, line in enumerate(file,start=1):
                if target_word in line:
                    print(f"Target word '{target_word}' is found in line number {line_num}")
    # except FileNotFoundError:
    #     print("Required file doesn't exists in the mentioned path")
    
    except Exception as e:
        print (f"An exception has occured {e}")

find_word("/Users/aspadhi/projects/Neetcode150/arrays&hashing/not_exist.txt","Python")