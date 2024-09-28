def find_perm(str):
    if len(str)==1:
        return str
    perms=[]
    for i in range(len(str)):
        fixed=str[i]

        remaining = str[:i]+str[i+1:]

        for perm in find_perm(remaining):
            perms.append(fixed + perm )