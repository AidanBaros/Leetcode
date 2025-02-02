def isPalindrome(x):
    x = str(x)
    return check(x,0,len(x)-1)

def check(seq,start,end):
    if start >= end:
        return True

    if seq[start] != seq[end]:
        return False
    else:
        return check(seq,start+1,end-1)
    

print(isPalindrome(10))