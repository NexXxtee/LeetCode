def isPalindrome(s) -> bool:
    s = [d for d in s.lower() if d.isalnum()]
    l = 0
    r = len(s) - 1
    while r > l:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))