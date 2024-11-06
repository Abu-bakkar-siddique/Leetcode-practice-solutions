import string 
def isPalindrome(s: str) -> bool:
    
    for c in string.punctuation:
        if c in s:
            s = s.replace(c, "")

    s = s.replace(" ", "")
    s = s.replace("  ", "")
    s = s.lower()
    to_comp = list(s)
    s = list(s)

    s.reverse()
    print(s)
    print(to_comp)
    return to_comp ==  s

print(isPalindrome("aa a t t a aa!"))