#i = 1

#while i != 4:
#    print("meow")
#    i = i + 1

#for i in range(3) or [0, 1, 2]: #range(3) is 0 to 2; 3 is not included
#    print("meow")
#i += 1

#print("meow\n" * 3,end="") #meowmeowmeow; because if dont use end="", it will print meow in 3 lines
"""
while True:
    n = int(input("What's n?"))
    if n > 0:
        break     

for _ in range(n):
    print("meow")           


def main():
    n = int(input("What's n? "))
    if n > 0:
        meow(n)
       

def meow(n):
    for _ in range(n):
        print("meow")

"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")


main()