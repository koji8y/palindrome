# %%
def isPalindrome(val: int) -> bool:
    vals = str(val)
    for i in range(len(vals) // 2):
        if vals[i] != vals[-i - 1]:
            return False
    return True
def extend(val: int) -> int:
    return int(str(val)[::-1]) + val

def makePalindrome(val: int, count=1, verbose=True, maxCount=300) -> int:
    if count > maxCount:
        raise Exception('Cannot determine!')
    if isPalindrome(val):
        return val
    if verbose:
        print(f'Intermediate #{count}: {val}')
    return makePalindrome(extend(val), count=count+1, maxCount=maxCount)
# %%
makePalindrome(121)
# %%
makePalindrome(123)
# %%
makePalindrome(98)
# %%
makePalindrome(196)
# %%
