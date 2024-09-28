def freq_words(str) -> dict:
    words = str.split()
    word_count = {}

    for word in words:
        word_count[word]=word_count.get(word,0)+1
    return word_count

freq= freq_words("A ashis is better than multiple a ashis but why only single is not better than ashis")

for key, value in freq.items():
    print(f"{key} , {value}")

max_key=max(freq, key= lambda k : freq[k])

print(f"Max key = {max_key}")