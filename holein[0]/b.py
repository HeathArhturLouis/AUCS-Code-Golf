class DoublyNode():
    def __init__(self, prev, _next):
        self.val = 0
        self.prev = prev
        self.next = _next

current = DoublyNode(None, None)
_input = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

def interpret(idx):
    char = _input[idx]
    global current
    if char == ">":
        if not current.next:
            new = DoublyNode(current, None)
            current.next = new
            current = new
        else:
            current = current.next
    if char == "<":
        if not current.prev:
            new = DoublyNode(None, current)
            current.prev = new
            current = new
        else:
            current = current.prev
    if char == "+":
        current.val += 1
        current.val %= 256
    if char == "-":
        current.val -= 1
        current.val %= 256
    if char == ".":
        print(chr(current.val))
    if char == ",":
        current.val = ord(input()) % 256
    if char == "[":
        if not current.val:
            while idx < len(_input) and _input[idx] != ']':
                idx += 1
            return (interpret(idx+1) if idx < (len(_input) - 1) else None)
    if char == "]":
        if current.val:
            while idx > 0 and _input[idx] != '[':
                idx -= 1
            return (interpret(idx+1) if idx >= 0 else None)
    if idx < (len(_input) - 1):
        interpret(idx + 1)

interpret(0)