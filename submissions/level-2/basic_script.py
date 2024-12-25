print("Hello ML and Robotics")
def sq(n):
    return n**2
n = input("Enter a integer: ")
if type(n) == int:
    n = int(n)
else:
    print("USELESS")
print(sq(n))