def count_lines(file_path):
    with open(file_path,"r") as file:
        count=0
        for line in file:
            count+=1
    print(count)

def advanced_count(file_path):
    with open(file_path,"r") as file:
        count = sum(1 for line in file)
    print(count)

advanced_count("/Users/aspadhi/projects/Neetcode150/arrays&hashing/log copy.txt")