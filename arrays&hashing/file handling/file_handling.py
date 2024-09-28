def read_file(file_name):
    file = open(file_name,"r")
    content=file.read() #reads entire file as single content, not line by line.
    print(content)
    file.close()

def write_file(file_name):
    file = open(file_name, "a")
    file.write("\nAppending one line")
    file.close()

def write_with():
    #with statement handles file closing automatically.
    with open("akp.txt","w") as file:
        file.write("AKP is good. \n")

# write_file("/Users/aspadhi/projects/Neetcode150/arrays&hashing/log_copy.txt")
# read_file("/Users/aspadhi/projects/Neetcode150/arrays&hashing/log_copy.txt")
