class Stack:
    def __init__(self):
        self.data = []
        self.count = 0

    def push(self, element):
        self.data.append(element)
        self.count += 1

    def pop(self):
        if len(self.data) == 0:
            raise Exception("Stack is empty")
        self.count -= 1
        return self.data.pop(self.count)

    def see_top(self):
        if len(self.data) == 0:
            raise Exception("Stack is empty")
        return self.data[self.count-1]

    def is_empty(self):
        return self.count == 0

def main():
    p = '[[[[]]]][][][]]'
    s = Stack()
    is_match = True
    for c in p:
        if c == '[':
            s.push(c)
        elif c == ']':
            if s.is_empty():
                is_match = False
                break
            else:
                s.pop()
    if is_match:
        print ('Pattern Matched')
    else:
        print ('Pattern Mismatched')
    #s = Stack()
    #s.push(35)
    #s.push(56)
    #s.push(46)
    #print (s.pop())
    #print (s.pop())
    #print (s.see_top())
    #print (s.pop())
    #print (s.pop())

main()

