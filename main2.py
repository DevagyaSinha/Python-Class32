def flip(s):
    if len(s)==1:
        return s
    return flip(s[1:])+s[0]

input("flip recurrses on s[1:] and then adds s[0] at the end.")
print("flip('Amrutha')",flip('Amrutha'))

s=str(input("enter any of the noun or pronoun"))
print("flip(s)",flip(s))