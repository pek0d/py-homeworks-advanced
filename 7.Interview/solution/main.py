class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


def is_balanced(parentheses):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    for char in parentheses:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return "Несбалансированно"
            else:
                if opening.index(stack.pop()) != closing.index(char):
                    return "Несбалансированно"
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    input_string = "((([{}])))"
    print(is_balanced(input_string))

    input_string = "}{}"
    print(is_balanced(input_string))
