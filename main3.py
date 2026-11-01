def power4(n):
    if n<0:
        return False
    if n==1:
        return True
    if n%4==0:
        return power4(n//4)
    return False

input("power4 divides the number by 4 then recurses //4 ")
print("power4(64)",power4(64))
print("power4(12)",power4(12))

n=int(input("enter your number and we will check if its is power of 4 or not "))
print("power4(n)",power4(n))