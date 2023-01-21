import sys

code = None
stack = []

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

while code:
    line = code.pop().lstrip()
    if line.startswith('*') and line.endswith('*'): continue
    exec_ = line.split(' ')
    if exec_[0] == '//':
        continue
    elif exec_[0] == 'ADD':
        _add(exec_[1])
    elif exec_[0] == 'POP':
        stack.pop()
    elif exec_[0] == 'REVERSE':
        _reverse()
    elif exec_[0] == 'PRINT_ASCII':
        _print()
    elif exec_[0] == 'REPEAT_ALL':
        while stack:
            if exec_[1] == 'ADD':
                _add(stack.pop())
            elif exec_[1] == 'REVERSE':
                _reverse()
            elif exec_[1] == 'PRINT_ASCII':
                _print()
    else:
        print('UNKNOWN FUNCTION')