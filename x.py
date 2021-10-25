stack = []
while True:
    ch = input("enter character: ")
    if ch == 's':
        i = int(input("enter value"))
        push(stack,i)
    elif ch == 'p':
        pop(stack)
    elif ch == 'e':
        empty(stack)
    elif ch == 'q':
        print('Goodbye!')
        break

def push(stack, val):
    stack.append(val)

def pop(stack):
    if len(stack) > 0:

        return stack.pop()
    else:
        print("stack underflow!")

def empty(stack):
    print("emptying stack")
    while len(stack) > 0:
        print(f"Popping Element {pop(stack)}")
