def flip(n):
    if n//10==0:
        return n
    last=n%10
    rest=flip(n//10)
    return last*pow(10,len(str(rest)))+rest
input("Flip peels the last digit of a number with %10 then recurses //10  ")
print("flip(123)", flip(123))
print("flip(456)", flip(456))

n=int(input("enter a 3 digit number"))
print("flip(n)",flip(n))