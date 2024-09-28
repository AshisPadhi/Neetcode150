def check_palin(str):
    tmp=str.replace(" ","").lower()

    if tmp == tmp[::-1]:
        return True
    else:
        return False

print(check_palin("wollow"))