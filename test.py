"""
# ask user for their name
name = input("What's your name? ")

# remove whitespace from string
name = name.strip()

# capitalize user's name
name = name.title()

# split user's name into first and last name
first, last = name.split(" ")

# say hello to user
print(f"hello,  {last}" )
"""
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
