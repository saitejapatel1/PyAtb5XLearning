import keyword

_a=1

print(type(3.14))
print("---------------------")
a=2+(33-1)/4*18-44
print(a)
print("------------------")
age=34
AGE=36
print(age)
print(AGE)
age="virat"
print(age)
print("--------------")
print("python keywords are:", keyword.kwlist)
print("------------------------------")
# Input a string
identifier = input("Enter a string: ")

# Check if it's a valid identifier
if identifier.isidentifier():
    print(f"'{identifier}' is a valid identifier.")
else:
    print(f"'{identifier}' is not a valid identifier.")