def freq_counter(str1) -> dict:
    if str1 is not None:
        word_counter={}
        for char in str1:
            word_counter[char]=word_counter.get(char,0)+1 # get function retrieves value of a key if not found, replaces the value with 0 
        return word_counter

def check_anagram(str1, str2):
    str1_freq=freq_counter(str1.lower())
    str2_freq=freq_counter(str2.lower())

    if sorted(str1_freq) == sorted(str2_freq):
        return True
    else:
        return False

    # for key, value in str1_freq.items():
    #     print(f"{key}, {value}")

print(check_anagram("Ashis", "Sisha"))