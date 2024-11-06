def lengthOfLastWord(s: str) -> int:
        s = s.strip().split(" ")
        return len(s[-1])    
print(lengthOfLastWord("hello     world    "))