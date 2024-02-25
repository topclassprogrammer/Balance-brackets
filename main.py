class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def balance_brackets(self, str_):
        brackets = {')': '(', ']': '[', '}': '{'}
        for char in str_:
            if char in brackets.keys():
                if self.size() and self.peek() == brackets[char]:
                    self.stack.pop()
                else:
                    return "Несбалансированно"
            else:
                self.push(char)
        if self.stack:
            return "Несбалансированно"
        else:
            return "Сбалансированно"


if __name__ == '__main__':
    stack = Stack()
    target_brackets = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}',
                       '}{}', '{{[(])]}}', '[[{())}]']
    for target in target_brackets:
        res = stack.balance_brackets(target)
        print(f'{target} - {res}')
