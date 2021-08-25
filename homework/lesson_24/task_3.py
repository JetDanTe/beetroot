"""Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element is not
found - raise ValueError with proper info Message"""



stack_lifo = []

for i in range(100):
    stack_lifo.append(i)


def get_from_stack(stack, element):
    element_name = 'letter'
    if element.isdigit():
        element_name = 'number'
        element = int(element)
    # splitter = int(len(stack)/2)
    # part_1 = stack[:splitter]
    # part_2 = stack[splitter:]
    ware_house_stack = []
    for _ in range(len(stack)):
        now = stack.pop()
        ware_house_stack.append(now)
        if now == element:
            goal = now
            ware_house_stack.pop()
            for _ in range(len(ware_house_stack)):
                stack.append(ware_house_stack.pop())
            return f"Your goal {goal} from stack:\n{stack}"
    raise ValueError(f"There is no {element_name} {element} in stack!\n")


print(get_from_stack(stack_lifo, input("Enter number or letter:\n")))



