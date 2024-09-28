str = "hello world !"

print(str[1:5])
print(str[:5])
print(str[::-1])#prints string in reverse order
print(str[::-2]) #prints string in reverse order and skips one one character inbetween

print(str.find("world"))
print(str.replace("world","python")) #replaces world with python and just prints it, doesn't overwrites.
print(str.isdigit()) # checks if the string is digits only
print(str.isalpha()) # checks if the string is alphabets only
print(str.isalnum()) # checks if string is alpha numeric

print (str.split(",")) # splits texts and uses ',' as delimiter




