def merge_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1, open(file2_path,'r') as file2, open(output_path,'w') as output:
        for line1, line2 in zip(file1, file2):
            output.write(f"{line1.strip()} {line2.strip()}\n")
    with open(output_path, 'r') as output:
        print(output.read())

f1_path = "/Users/aspadhi/projects/Neetcode150/arrays&hashing/merge1.txt"
f2_path = "/Users/aspadhi/projects/Neetcode150/arrays&hashing/merge2.txt"

merge_files(f1_path,f2_path, output_path="merged_file.txt")

