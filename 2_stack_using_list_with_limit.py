stack = []

def push():

    if (len(stack) == limit):
        print("Stack is full....!")
    else:
        x = int(input("Enter the element to add:"))
        stack.append(x)
        print("{} add to stack".format(x))
        print(stack)

def pop():
    if (len(stack) == 0):
        print("Can't remove from empty stack")
    else:
        x = stack.pop()
        print("{} removed from stack".format(x))
        print(stack)
def display():
    print(stack)
limit = int(input("Enter the stack limit:"))
print("Enter your choice 1.push 2.pop 3.Display 4.exit")
while 1:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct choice....")
