import re

text = "The rain in Spain"
match = re.search(r"rain", text) #Search a particular word

if match:
    print("Match Found")

