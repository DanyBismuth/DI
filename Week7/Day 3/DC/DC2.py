str = input("enter a a String")
character = input("enter letter to count")

def count(s, character):
    res = 0

    for i in range(len(s)):
        if (s[i] == character):
            res = res + 1
    return res

print(count(str, character))