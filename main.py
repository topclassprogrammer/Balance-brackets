class Stack:
    def __init__(self):
        self.stack = []
        self.brackets_dict = {')': '(', ']': '[', '}': '{'}

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item: str):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def balance_brackets(self, brackets_str: str):
        for char in brackets_str:
            if char in self.brackets_dict.keys():
                if self.size() and self.peek() == self.brackets_dict[char]:
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
