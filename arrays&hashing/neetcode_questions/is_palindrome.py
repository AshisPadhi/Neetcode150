def isPalindrome(s: str) -> bool:
    tmp=""
    s=s.lower()
    if s is not None:
        for char in s:
            if char.isalnum():
                tmp+=char
    # print(tmp)
    # print(tmp[::-1])
    if tmp[::-1] == tmp:
        return True
    else:
        return False
    
print(isPalindrome("Was it a car or a cat I saw?"))

