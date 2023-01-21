# Efflo
Efflo is a very basic programming language that I work on in my free time.

Features:
- Stack-based
- Procedures
- Basic arithmetic

Example code:
```
rem Add "Hello, World!" to the stack.;
string Hello,_World!;

rem Reverse the stack;
reverse;

rem Print every character;
repeat_all print_ascii;
```

`rem` is a comment.
`string` pushes all the characters as their ASCII values to the stack.
`repeat_all` repeats an instruction until the stack is empty. In this case, it runs `print_ascii` which takes an ASCII value and prints it as a character.
