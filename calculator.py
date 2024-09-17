'''
x = float(input("What is X?"))
y = float(input("What is Y?"))

z = round(x / y, 2)  # ,2 can round to 小數後第2位

print (z)



# int is 整數, float can be 小數

# f"{z:,}" can help you 整齊 ur numbers

'''

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square (n):
     return n**2

main()