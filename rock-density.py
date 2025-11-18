concentration_treshold = 250
grid = ("enter your grid values")
print(grid)
northings = (int(input("enter grid Northings value _ ")))
eastings = (int(input("enter grid Eastings value _ ")))
concentration = int(input("what is the concentration value of Fe in this point? _ "))
if concentration < concentration_treshold:
    print(f"low concentration value at Point {northings} {eastings}")
elif concentration > concentration_treshold:
    print(f"high concentration value at Point {northings} {eastings}")
