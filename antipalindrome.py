def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    return False

def iterateSubstrings(s):
    for start in range(0, len(s)):
        for end in range(start+2, 1+len(s)):            
            print(s[start:end])
            if isPalindrome(s[start:end]):
                return True
               
    return False
    
s = input().replace(" ", "").replace(".", "").replace(",", "").lower()
#s = "abcdefgh"

if iterateSubstrings(s):
    print("Palindrome")
else:
    print("Anti-palindrome")