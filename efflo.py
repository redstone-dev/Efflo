import sys

code = None
stack = []
procedures = []

with open(sys.argv[1], 'rt', encoding='utf8') as file:
    code = file.read()
    
def _add(num):
    stack.append(num)
    
def _reverse():
    global stack
    stack = stack[::-1]
    
def _print():
    print(chr(int(stack.pop())), end='')
    
def _repeat_all(func):
    while stack:
        func(stack.pop())
    
code = code.split(';')
code = list(reversed(code))

def do_code(exec_):
    if exec_[0] == 'PUSH':
        _add(exec_[1])
    elif exec_[0] == 'POP':
        stack.pop()
    elif exec_[0] == 'REVERSE':
        _reverse()
    elif exec_[0] == 'PRINT_ASCII':
        _print()
    elif exec_[0] == 'PRINT_NUM':
        print(stack.pop())
    elif exec_[0] == 'REPEAT_ALL':
        while stack:
            if str(exec_[1]).startswith('$'):
                i = procedures.index(str(exec_[1][1:]))
                for instruction in procedures[i + 1]:
                    do_code(instruction.upper())
            else:
                do_code(exec_[1].upper())
    elif exec_[0] == 'PROC':
        procedures.append(exec_[1], exec_[2:])
    elif exec_[0] == '+':
        # first item + second item
        stack.append \
            (float(stack.pop()) + float(stack.pop()))
    elif exec_[0] == '-':
        # first item - second item
        stack.append \
            (float(stack.pop()) - float(stack.pop()))
    elif exec_[0] == '*':
        # first item * second item
        stack.append \
            (float(stack.pop()) * float(stack.pop()))
    elif exec_[0] == '/':
        # first item / second item
        stack.append \
            (float(stack.pop()) / float(stack.pop()))
    elif exec_[0] == '%':
        # first item % second item
        stack.append \
            (float(stack.pop()) % float(stack.pop()))
    elif exec_[0] == 'STRING':
        for char in str(exec_[1])[0:]:
            if char == '_':
                stack.append(ord(' '))
            else:
                stack.append(ord(char))
    else:
        print('Unknown Instruction "' + exec_ + '"')

while code:
    line = code.pop().lstrip()
    if line.startswith('//') \
    or line.isspace() \
    or line == '': 
        continue
    exec_ = line.upper().split(' ')
    do_code(exec_)
