def reverse(s):
    z=""
    for i in s:
        z=i+z
    return z


print("Enter Word:")
s=input()
print(reverse(s))